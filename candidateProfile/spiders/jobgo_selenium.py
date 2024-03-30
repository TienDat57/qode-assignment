import time
from selenium import webdriver
from candidateProfile.db import MongoDBClient
from candidateProfile import settings
import random

if __name__ == "__main__":
   client = MongoDBClient(settings.MONGODB_COLLECTION)
   start_urls = []

   chromedriver = webdriver.Firefox()
   chromedriver.get("https://employer.jobsgo.vn/site/login")

   username = chromedriver.find_element_by_id("loginform-user_name")
   password = chromedriver.find_element_by_id("loginform-password")
   username.send_keys(settings.LINKEDIN_ACCOUNT)
   password.send_keys(settings.PASSWORD_CRAWL)

   chromedriver.find_element_by_name("signin").click()

   start_urls.append("https://employer.jobsgo.vn/search-cv/index?SearchCv%5Bgeneral%5D=&SearchCv%5Bin%5D=&SearchCv%5Bin%5D%5B%5D=all&SearchCv%5Brole%5D=&SearchCv%5Brole%5D%5B%5D=Nh%C3%A2n+Vi%C3%AAn+X%E1%BB%AD+L%C3%BD+D%E1%BB%AF+Li%E1%BB%87u&SearchCv%5Bjob_category%5D=&SearchCv%5Bplace%5D=&SearchCv%5Bplace%5D%5B%5D=H%E1%BB%93+Ch%C3%AD+Minh&range_age=&checkbox1=on&showhide=10")
   chromedriver.get(start_urls[0])

   time.sleep(2)

   while True:
      tbody_element = chromedriver.find_element_by_css_selector('tbody')
      tr_elements = tbody_element.find_elements_by_tag_name('tr')
      
      for profile_element in tr_elements:
         try:
            # Find the anchor tag within the <td> element
            profile_anchor = profile_element.find_element_by_css_selector('td.colorgb-pjax a')
            
            # Get the href attribute value
            profile_link = profile_anchor.get_attribute('href')
            
            # Insert into MongoDB collection
            client.collection.insert_one({'profile_link': profile_link})
         except Exception as e:
            print("Error:", e)
      try:
         next_button = chromedriver.find_element_by_css_selector('div.kv-panel-pager ul.pagination li.next a')
         next_button.click()
         print("Clicked the Next button successfully!")
      except Exception as e:
         print("Failed to click the Next button:", e)

      time.sleep(random.uniform(5, 10))