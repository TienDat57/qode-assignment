from candidateProfile import settings
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from candidateProfile.parsers.JobgoParser import JobGoParser

from bs4.dammit import UnicodeDammit
from urllib.parse import unquote_plus
import time
from random import uniform
from candidateProfile.db import MongoDBClient

class JobgoSpider(scrapy.Spider):
   name = 'Jobgo'
   allowed_domains = ['jobsgo.vn']
   start_urls = []
   login_page = 'https://employer.jobsgo.vn/site/login'

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
         'LoginForm[username]': self.settings['LINKEDIN_ACCOUNT'], 
         'LoginForm[password]': self.settings['PASSWORD_CRAWL']
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
      personProfile = JobGoParser.extract_person_profile(hxs)
      self.mongodb_candidate.collection.update_one({'profile_link': response.url}, {'$set': personProfile}, upsert=True)
      yield personProfile

   def __init__(self):
      self.init_links()
      pass


