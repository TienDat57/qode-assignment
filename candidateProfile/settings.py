import logging
import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

LOG_FILE = 'logs/LOG_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.log'
LOG_LEVEL = 'DEBUG'

BOT_NAME = "candidateProfile"

SPIDER_MODULES = ["candidateProfile.spiders"]
NEWSPIDER_MODULE = "candidateProfile.spiders"

DOWNLOADER_MIDDLEWARES = {
   'candidateProfile.middlewares.CustomHttpProxyMiddleware': 543,
   'candidateProfile.middlewares.CustomUserAgentMiddleware': 545,
}

# NOTE: Fill account and password for LinkedIn and JobGo
LINKEDIN_ACCOUNT = 'dangtiendat1135@gmail.com'
PASSWORD_CRAWL = ''

JOBGO_ACCOUNT = 'dangtiendat1135@gmail.com'

# ITEM_PIPELINES = {
#     "candidateProfile.pipelines.MongoDBPipeline",
# }

# NOTE: Fill in the following fields with your MongoDB connection details
MONGODB_URI = 'mongodb+srv://TienDat57:<password>@qode.addyuj.mongodb.net/'
MONGODB_PORT = 27017
MONGODB_DB = 'qodeworld'
MONGODB_COLLECTION = 'candidateProfile'
MONGODB_UNIQ_KEY = '_id'

# AUTOTHROTTLE_ENABLED = True

# COOKIES_ENABLED = False

# RETRY_TIMES = 100

# RETRY_HTTP_CODES = [999, 500, 503, 504, 400, 403, 408]

# DUPEFILTER_CLASS = "candidateProfile.dupefilter.CustomDupeFilter"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "candidateProfile (+http://www.yourdomain.com)"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True


# REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "utf-8"


