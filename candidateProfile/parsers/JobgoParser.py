from candidateProfile.items import PersonProfileItem

class JobgoParser:    
    @staticmethod
    def extract_person_profile(hxs):
        personProfile = PersonProfileItem()

        # Extracting name
        
        name = hxs.xpath('//*[@id="header"]/div/div/h1/a')
        if name:
            personProfile['fullname'] = name[0].xpath(".//text()").extract_first()

        # Extracting title
        title = hxs.xpath('//*[@id="header"]/div/div/p/span')
        if title:
            personProfile['title'] = title[0].xpath(".//text()").extract_first()

        # Extracting location
        location = hxs.xpath('//*[@id="about"]/div/div[2]/div/div/div[2]/ul/li[3]/span')
        if location:
            personProfile['location'] = location[0].xpath(".//text()").extract_first()

        # Extracting industry
        industry = hxs.xpath('//*[@id="header"]/div/div/p/span').extract()
        personProfile['industry'] = ';'.join(industry)

        # Extracting overview summary - current company, past companies, education
        overview_summary_current = hxs.xpath('//*[@id="resume"]/div/div/div[1]/div[1]/small//text()').extract()
        personProfile['current_company'] = ';'.join(overview_summary_current)

        overview_summary_past = hxs.xpath('//*[@id="resume"]/div/div/div[1]/div[2]/small//text()').extract()
        personProfile['past_company'] = ';'.join(overview_summary_past)

        overview_sumary_education = hxs.xpath('//*[@id="resume"]/div/div/div[2]/div/p[1]/em//text()').extract()
        personProfile['education'] = ';'.join(overview_sumary_education)

        # Extracting summary
        summary = hxs.xpath('//*[@id="about"]/div/div[1]/div[2]/p//text()').extract()
        personProfile['summary'] = ' '.join(summary)

        # Extracting email, website, birthday, phone
        personProfile['email'] = ';'.join(hxs.xpath('//*[@id="about"]/div/div[2]/div/div/div[1]/ul/li[4]/span//text()').extract())
        personProfile['birthday'] = hxs.xpath('//*[@id="about"]/div/div[2]/div/div/div[1]/ul/li[1]/span//text()').extract_first()
        personProfile['phone'] = ';'.join(hxs.xpath('//*[@id="about"]/div/div[2]/div/div/div[1]/ul/li[3]/span//text()').extract())

        # Extracting skills and past experiences
        personProfile['skill'] = ';'.join(hxs.xpath('//*[@id="skills"]/div/div[2]//text()').extract())

        # Extracting image URL
        personProfile['image'] = hxs.xpath('//*[@id="header"]/div/div/img/@src').extract_first()
        return personProfile
