# Scrapy settings for crawlCandidateProfile project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "crawlCandidateProfile"

SPIDER_MODULES = ["crawlCandidateProfile.spiders"]
NEWSPIDER_MODULE = "crawlCandidateProfile.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = True


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

MONGODB_SERVER = '145.24.222.238'
MONGODB_PORT = 27017
MONGODB_DB = 'linkedin_crawl_full'
MONGODB_COLLECTION = 'profiles'

LOG_FILE = 'log.txt'
LOG_LEVEL = log.INFO