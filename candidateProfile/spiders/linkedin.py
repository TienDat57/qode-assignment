from typing import Iterable
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from pymongo import MongoClient
from candidateProfile.parsers.HtmlParser import HtmlParser
from bs4.dammit import UnicodeDammit
from urllib.parse import unquote_plus
import time
from random import uniform

class Mongodb():
    client = None
    rel_coll = None

    def __init__(self, uri=None, db=None, col=None):
        self._client = MongoClient(uri)
        self._db = self._client[db]
        self.name_col = col
        self.rel_coll = self._db[col]

    def refresh_collection(self):
        self.rel_coll.drop()
        self.rel_coll = self._db[self.name_col]

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    start_urls = []
    login_page = 'https://www.linkedin.com/login'

    def init_links(self):
        self.mongodb_candidate = Mongodb(uri='mongodb+srv://TienDat57:Tiendat572k2@qode.agtuohy.mongodb.net/', db='qodeworld', col='candidateProfile')
        for row in self.mongodb_candidate.rel_coll.find():
            self.start_urls.append(row['url'])
        print('start_urls: ', self.start_urls)

    def start_requests(self):
        yield Request(url=self.login_page, callback=self.login)

    def login(self, response):
        print('linkedin account:', self.settings['LINKEDIN_ACCOUNT'])
        print('session_password:', self.settings['LINKEDIN_PASSWORD'])
        
        formdata = {
            'session_key': self.settings['LINKEDIN_ACCOUNT'], 
            'session_password': self.settings['LINKEDIN_PASSWORD']
        }
        
        print('Form Data:', formdata)
        
        return FormRequest.from_response(
                response,
                formdata=formdata,
                callback=self.check_login_response)
    
    def check_login_response(self, response):
        print('response: ', response)
        if "Sign In" in response.body:
            self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
            # Now the crawling can begin..
            return self.initialized() # ****THIS LINE FIXED THE LAST PROBLEM*****

        else:
            self.log("\n\n\nFailed, Bad times :(\n\n\n")

    def parse(self, response):
        """
        default parse method, rule is not useful now
        """
        time.sleep(uniform(1, 10))
        # response = response.replace(url=HtmlParser.remove_url_parameter(response.url))
        # hxs = HtmlXPathSelector(response)
        hxs = Selector(response)
        index_level = self.determine_level(response)
        if index_level == 1:
            relative_urls = self.get_top_profile(2, hxs)
            if relative_urls is not None:
                for url in relative_urls:
                    yield Request(url, callback=self.parse)
        elif index_level == 2:
            personProfile = HtmlParser.extract_person_profile(hxs)
            linkedin_id = self.get_linkedin_id(response.url)
            linkedin_id = UnicodeDammit(unquote_plus(linkedin_id)).markup
            if linkedin_id:
                personProfile['id'] = linkedin_id
                # personProfile['url'] = UnicodeDammit(response.url).markup
                self.mongodb_candidate.rel_coll.update_one({'url': response.url}, {'$set': personProfile}, upsert=True)
                print(personProfile)
                yield personProfile

    def determine_level(self, response):
        """
        determine the index level of current response, so we can decide wether to continue crawl or not.
        level 1: people/[a-z].html
        level 2: people/[A-Z][\d+].html
        level 3: people/[a-zA-Z0-9-]+.html
        level 4: search page, pub/dir/.+
        level 5: profile page
        """
        import re
        url = response.url
        if 'search=Search' in url:
            return 2
        elif 'profile' in url:
            return 2
        return 2

    def __init__(self):
        self.init_links()
        # self.init_request()
        pass

    @staticmethod
    def get_linkedin_id(url):
        find_index = url.find("www.linkedin.com/in/")
        if find_index >= 0:
            return url[find_index + 20:].replace('/', '')
        return None

    @staticmethod
    def get_follow_links(level, hxs):
        if level in [1, 2, 3]:
            relative_urls = hxs.select("//ul[@class='column dual-column']/li/a/@href").extract()
            relative_urls = ["http://www.linkedin.com" + x for x in relative_urls if 'linkedin.com' not in x]
            return relative_urls
        elif level == 4:
            relative_urls = relative_urls = hxs.select("//ol[@id='result-set']/li/h2/strong/a/@href").extract()
            relative_urls = ["http://www.linkedin.com" + x for x in relative_urls]
            return relative_urls

    @staticmethod
    def get_top_profile(number_profiles, hxs):
        profile_links = hxs.select('//div[@id="results-container"]/ol/li/a/@href').extract()
        return profile_links[0:number_profiles]

