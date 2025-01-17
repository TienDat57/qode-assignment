from candidateProfile import settings
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from candidateProfile.parsers.LinkedinParser import LinkedInProfileParser
from bs4.dammit import UnicodeDammit
from urllib.parse import unquote_plus
import time
from random import uniform
from candidateProfile.db import MongoDBClient

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    start_urls = []
    login_page = 'https://www.linkedin.com/login'

    def init_links(self):
        self.mongodb_candidate = MongoDBClient(settings.MONGODB_COLLECTION)
        for row in self.mongodb_candidate.collection.find():
            self.start_urls.append(row['url'])
        print('start_urls: ', self.start_urls)

    def start_requests(self):
        yield Request(url=self.login_page, callback=self.login)

    def login(self, response):
        print('linkedin account:', self.settings['LINKEDIN_ACCOUNT'])
        print('session_password:', self.settings['PASSWORD_CRAWL'])
        
        form_data = {
            'session_key': self.settings['LINKEDIN_ACCOUNT'], 
            'session_password': self.settings['PASSWORD_CRAWL']
        }
        
        print('Form Data:', form_data)
        
        return FormRequest.from_response(
                response,
                formdata=form_data,
                callback=self.check_login_response
            )
    
    def check_login_response(self, response):
        if "Sign In" in response.body:
            self.log("\n\n\nSuccessfully logged in.\n\n\n")
        else:
            self.log("\n\n\nFailed\n\n\n")

    def parse(self, response):
        time.sleep(uniform(1, 10))
        hxs = Selector(response)
        index_level = self.determine_level(response)
        if index_level == 1:
            relative_urls = self.get_top_profile(2, hxs)
            if relative_urls is not None:
                for url in relative_urls:
                    yield Request(url, callback=self.parse)
        elif index_level == 2:
            personProfile = LinkedInProfileParser.extract_person_profile(hxs)
            linkedin_id = self.get_linkedin_id(response.url)
            linkedin_id = UnicodeDammit(unquote_plus(linkedin_id)).markup
            if linkedin_id:
                personProfile['id'] = linkedin_id
                self.mongodb_candidate.collection.update_one({'profile_link': response.url}, {'$set': personProfile}, upsert=True)
                yield personProfile

    def determine_level(self, response):
        import re
        url = response.url
        if 'search=Search' in url:
            return 2
        elif 'profile' in url:
            return 2
        return 2

    def __init__(self):
        self.init_links()
        pass

    @staticmethod
    def get_linkedin_id(url):
        find_index = url.find("www.linkedin.com/in/")
        if find_index >= 0:
            return url[find_index + 20:].replace('/', '')
        return None

    @staticmethod
    def get_top_profile(number_profiles, hxs):
        profile_links = hxs.select('//div[@id="results-container"]/ol/li/a/@href').extract()
        return profile_links[0:number_profiles]

