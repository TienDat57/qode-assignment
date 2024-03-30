from candidateProfile.items import PersonProfileItem
from w3lib.url import url_query_cleaner

class LinkedInProfileParser:    
    @staticmethod
    def extract_person_profile(hxs):
        personProfile = PersonProfileItem()

        # Extracting name
        name = hxs.xpath("//*[@id='ember2272']")
        if name:
            personProfile['fullname'] = name[0].xpath(".//text()").extract_first()

        # Extracting title
        title = hxs.xpath("//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]")
        if title:
            personProfile['title'] = title[0].xpath(".//text()").extract_first()

        # Extracting location
        location = hxs.xpath("//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]")
        if location:
            personProfile['location'] = location[0].xpath(".//text()").extract_first()

        # Extracting industry
        industry = hxs.xpath('//dd[@class="industry"]/a//text()').extract()
        personProfile['industry'] = ';'.join(industry)

        # Extracting overview summary - current company, past companies, education
        overview_summary_current = hxs.xpath('//tr[@id="overview-summary-current"]/td//text()').extract()
        personProfile['current_company'] = ';'.join(overview_summary_current)

        overview_summary_past = hxs.xpath('//tr[@id="overview-summary-past"]/td//text()').extract()
        personProfile['past_company'] = ';'.join(overview_summary_past)

        overview_sumary_education = hxs.xpath('//tr[@id="overview-summary-education"]/td//text()').extract()
        personProfile['education'] = ';'.join(overview_sumary_education)

        # Extracting LinkedIn profile URL
        linkedin_links = hxs.xpath('//div[@id="contact-public-url-view"]//text()').extract()
        cleaned_links = [url_query_cleaner(link) for link in linkedin_links]
        personProfile['url'] = ';'.join(cleaned_links)

        # Extracting summary
        summary = hxs.xpath('//div[@class="summary"]//text()').extract()
        personProfile['summary'] = ' '.join(summary)

        # Extracting email, website, birthday, phone
        personProfile['email'] = ';'.join(hxs.xpath('//div[@id="relationship-emails-view"]/li/a//text()').extract())
        personProfile['website'] = ';'.join(hxs.xpath('//div[@id="relationship-sites-view"]/li/a/@href').extract())
        personProfile['birthday'] = hxs.xpath('//div[@id="relationship-birthday-view"]//text()').extract_first()
        personProfile['phone'] = ';'.join(hxs.xpath('//div[@id="relationship-phone-numbers-view"]/li//text()').extract())

        # Extracting skills and past experiences
        personProfile['skill'] = ';'.join(hxs.xpath('//span[@class="endorse-item-name"]//text()').extract())
        personProfile['experience'] = ';'.join(hxs.xpath('//div[@class="editable-item section-item past-position"]/div/header//text()').extract())

        # Extracting image URL
        personProfile['image'] = hxs.xpath('//div[@class="profile-picture"]/a/img/@src').extract_first()
        return personProfile
