from candidateProfile.items import PersonProfileItem
from bs4 import UnicodeDammit
from w3lib.url import url_query_cleaner
import random
from candidateProfile.parsers import LinkedinParser


class HtmlParser:    
    @staticmethod
    def extract_person_profile(hxs):
        personProfile = PersonProfileItem()

        # id = HtmlParser.get_linkedin_id()
        # name = hxs.xpath("//*[@id='ember2272']").extract()
        # title = hxs.xpath("//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]//text()").extract()
        # location = hxs.xpath("//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]//text()").extract()
        # industry = hxs.xpath('//dd[@class="industry"]/a//text()').extract()

        # overview_summary_current = hxs.xpath('//tr[@id="overview-summary-current"]/td//text()').extract()
        # overview_summary_past = hxs.xpath('//tr[@id="overview-summary-past"]/td//text()').extract()
        # overview_sumary_education = hxs.xpath('//tr[@id="overview-summary-education"]/td//text()').extract()

        # linkedin_link = hxs.xpath('//div[@id="contact-public-url-view"]//text()').extract()
        # linkedin_link2 = hxs.xpath('//dd[@class="view-public-profile"]/a/@href').extract()
        # linkedin_link3 = hxs.xpath('//a[@class="view-public-profile"]/@href').extract()

        # big_summary = hxs.xpath('//div[@class="summary"]//text()').extract()
        # number_connection = hxs.xpath('//div[@class="member-connections"]/strong//text()').extract()

        # email = hxs.xpath('//div[@id="relationship-emails-view"]/li/a//text()').extract()
        # birthday = hxs.xpath('//div[@id="relationship-birthday-view"]//text()').extract()
        # phone = hxs.xpath('//div[@id="relationship-phone-numbers-view"]/li//text()').extract()

        # website = hxs.xpath('//div[@id="relationship-sites-view"]/li/a/@href').extract()

        # span_skill = hxs.xpath('//span[@class="endorse-item-name"]//text()').extract()
        # span_past_experience = hxs.xpath('//div[@class="editable-item section-item past-position"]/div/header//text()').extract()

        # image = hxs.xpath('//div[@class="profile-picture"]/a/img/@src').extract()

        # twitter = hxs.xpath('//div[@id="twitter-view"]/li/a/@href').extract()

        # personProfile['twitter'] = ';'.join(twitter)
        
        
        # personProfile['name_linkedin'] = ' '.join(name)
        # personProfile['title'] = ' '.join(title) if len(title) > 0 else ''
        # personProfile['location'] = ';'.join(location)
        # personProfile['industry'] = ';'.join(industry)
        # personProfile['current_company'] = ';'.join(overview_summary_current)
        # personProfile['past_company'] = ';'.join(overview_summary_past)
        # personProfile['education'] = ';'.join(overview_sumary_education)
        # personProfile['url'] = ';'.join([linkedin_link[0] if len(linkedin_link) > 0 else '',
        #                                  linkedin_link2[0] if len(linkedin_link2) > 0 else '',
        #                                  linkedin_link3[0] if len(linkedin_link3) > 0 else ''])

        # personProfile['summary'] = ' '.join(big_summary)
        # personProfile['connection'] = number_connection[0] if len(number_connection) > 0 else ''
        # personProfile['email'] = ';'.join(email)
        # personProfile['website'] = ';'.join(website)
        # personProfile['birthday'] = ';'.join(birthday)
        # personProfile['phone'] = ';'.join(phone)

        # personProfile['skill'] = ';'.join(span_skill)
        # personProfile['experience'] = ';'.join(span_past_experience)
        # personProfile['image'] = image[0] if len(image) > 0 else ''
        # Extracting name
        
        name = hxs.xpath("//*[@id='ember2272']")
        if name:
            personProfile['name_linkedin'] = name[0].xpath(".//text()").extract_first()

        # Extracting title
        title = hxs.xpath("//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]")
        if title:
            personProfile['title'] = title[0].xpath(".//text()").extract_first()

        # Extracting location
        location = hxs.xpath("//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]")
        if location:
            personProfile['location'] = location[0].xpath(".//text()").extract_first()
        print(personProfile)
        return personProfile

    @staticmethod
    def get_also_view_item(dirtyUrl):
        item = {}
        url = HtmlParser.remove_url_parameter(dirtyUrl)
        item['linkedin_id'] = url 
        item['url'] = HtmlParser.get_linkedin_id(url)
        return item
        
    @staticmethod
    def remove_url_parameter(url):
        return url_query_cleaner(url)
    
    @staticmethod
    def get_linkedin_id(url):
        find_index = url.find("linkedin.com/")
        if find_index >= 0:
            return url[find_index + 13:].replace('/', '-')
        return None
