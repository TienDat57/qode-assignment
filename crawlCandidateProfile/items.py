
from scrapy.item import Item, Field
from scrapy.loader import XPathItemLoader
from scrapy.loader.processors import TakeFirst
import scrapy


class CandidateProfileItem(scrapy.Item):
    personal_information = scrapy.Field()
    education_background = scrapy.Field()
    work_experience = scrapy.Field()
    skills_and_expertise = scrapy.Field()
    social_media_presence = scrapy.Field()
    publications_and_projects = scrapy.Field()
    professional_interests = scrapy.Field()
    additional_information = scrapy.Field()

class PersonalInformationItem(scrapy.Item):
    name = scrapy.Field()
    contact_information = scrapy.Field()
    date_of_birth = scrapy.Field()
    gender = scrapy.Field()
    nationality = scrapy.Field()
    languages_spoken = scrapy.Field()

class ContactInformationItem(scrapy.Item):
    phone = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()

class EducationItem(scrapy.Item):
    degree = scrapy.Field()
    institution = scrapy.Field()
    major = scrapy.Field()
    graduation_year = scrapy.Field()

class WorkExperienceItem(scrapy.Item):
    company_name = scrapy.Field()
    job_title = scrapy.Field()
    employment_duration = scrapy.Field()
    responsibilities = scrapy.Field()
    skills_acquired = scrapy.Field()
    employment_type = scrapy.Field()

class SkillsAndExpertiseItem(scrapy.Item):
    technical_skills = scrapy.Field()
    soft_skills = scrapy.Field()
    certifications = scrapy.Field()

class SocialMediaPresenceItem(scrapy.Item):
    linkedin_profile = scrapy.Field()
    twitter_handle = scrapy.Field()
    github_profile = scrapy.Field()

class PublicationProjectItem(scrapy.Item):
    title = scrapy.Field()
    type = scrapy.Field()

class ProfessionalInterestsItem(scrapy.Item):
    industry_interests = scrapy.Field()
    career_goals = scrapy.Field()


