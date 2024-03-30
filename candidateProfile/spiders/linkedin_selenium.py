import time
from selenium import webdriver
from candidateProfile.db import MongoDBClient
from candidateProfile import settings
import random

if __name__ == "__main__":
   client = MongoDBClient(settings.MONGODB_COLLECTION)
   start_urls = []

   chromedriver = webdriver.Firefox()
   chromedriver.get("https://www.linkedin.com/in/login")
   
   start_urls.append("https://www.linkedin.com/search/results/people/?keywords=data%20engineer&origin=SWITCH_SEARCH_VERTICAL&sid=uyv")
   chromedriver.get(start_urls[0])

   username = chromedriver.find_element_by_id("session_key")
   password = chromedriver.find_element_by_id("session_password")
   username.send_keys(settings.LINKEDIN_ACCOUNT)
   password.send_keys(settings.LINKEDIN_PASSWORD)

   chromedriver.find_element_by_name("signin").click()

   time.sleep(2)

   while True:
      for i in range(1, 11):
         try:
               string_query = '//*[@class="search-results"]/li[' + str(i) + ']/a'
               profiles = chromedriver.find_element_by_xpath(string_query)
               linkedin = profiles.get_attribute('href')
               print(linkedin)
               # rel_coll.insert({'linkedin':linkedin})
               client.collection.insert({'linkedin':linkedin})
         except Exception as e:
               print(e)

      try:
         string_query = '//*[@class="next"]/a'
         next = chromedriver.find_element_by_xpath(string_query)
         next.click()
      except Exception as e:
         print(e)

      time.sleep(random.uniform(5, 10))