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

   username = chromedriver.find_element_by_id("username")
   password = chromedriver.find_element_by_id("password")
   username.send_keys(settings.LINKEDIN_ACCOUNT)
   password.send_keys(settings.PASSWORD_CRAWL)

   chromedriver.find_element_by_css_selector('button.btn__primary--large').click()

   start_urls.append("https://www.linkedin.com/search/results/people/?keywords=data%20engineer&origin=SWITCH_SEARCH_VERTICAL&sid=uyv")
   chromedriver.get(start_urls[0])

   time.sleep(2)

   while True:
      list_search_element = chromedriver.find_element_by_css_selector('ul.reusable-search__entity-result-list')
      list_profile_element = list_search_element.find_elements_by_tag_name('li')
      for i in range(1, len(list_profile_element)):
         try:
            string_query = '//*[@class="reusable-search__entity-result-list"]/li[' + str(i+1) + ']/descendant::a'
            profiles = chromedriver.find_element_by_xpath(string_query)
            # Get the href attribute value
            profile_link = profiles.get_attribute('href')
            
            # Insert into MongoDB collection
            client.collection.insert_one({'profile_link': profile_link})
         except Exception as e:
               print(e)
      try:
         next_button = chromedriver.find_element_by_xpath('//button[contains(@class, "artdeco-pagination__button--next")]')
         next_button.click()
         print("Clicked the Next button successfully!")
      except Exception as e:
         print("Failed to click the Next button:", e)

      time.sleep(random.uniform(5, 10))