from scrapy.item import Item, Field

class CrawlertestItem(Item):
    pass

class PersonProfileItem(Item):
    id = Field()
    fullname = Field()
    title = Field()
    location = Field()
    industry = Field()
    current_company = Field()
    past_company = Field()
    education = Field()
    profile_link = Field()
    summary = Field()
    website = Field()
    skill = Field()
    email = Field()
    image = Field()
    experience = Field()
    birthday = Field()
    phone = Field()