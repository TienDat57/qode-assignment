import pymongo
import logging
from twisted.enterprise import adbapi
from itemadapter import ItemAdapter

class CandidateprofilePipeline:
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
    def __init__(self, mongo_uri, mongodb_server, mongodb_port, mongodb_db, mongodb_collection, mongodb_uniq_key,
                 mongodb_item_id_field, mongodb_safe):
        connection = pymongo.Connection(mongodb_server, mongodb_port)
        self.mongodb_uri = mongo_uri
        self.mongodb_db = mongodb_db
        self.db = connection[mongodb_db]
        self.mongodb_collection = mongodb_collection
        self.collection = self.db[mongodb_collection]
        self.uniq_key = mongodb_uniq_key
        self.itemid = mongodb_item_id_field
        self.safe = mongodb_safe

        if isinstance(self.uniq_key, str) and self.uniq_key == "":
            self.uniq_key = None

        if self.uniq_key:
            self.collection.ensure_index(self.uniq_key, unique=True)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings.get('MONGODB_SERVER', 'localhost'), settings.get('MONGODB_PORT', 27017),
                   settings.get('MONGODB_DB', 'scrapy'), settings.get('MONGODB_COLLECTION', None),
                   settings.get('MONGODB_UNIQ_KEY', None), settings.get('MONGODB_ITEM_ID_FIELD', '_id'),
                   settings.get('MONGODB_SAFE', False), settings.get('MONGODB_URI', None))

    def process_item(self, item, spider):
        if self.uniq_key is None:
            self.collection.insert(dict(item), safe=self.safe)
        else:
            logging.debug("Process item %s" % item)
            self.collection.update(
                            {self.uniq_key: item[self.uniq_key]},
                            dict(item),
                            upsert=True) 
            self.collection.update({ self.uniq_key: item[self.uniq_key] }, { '$set': dict(item) }, upsert=True, safe=self.safe)

        logging.debug("Item %s wrote to MongoDB database %s/%s" % (item['_id'], self.mongodb_db, self.mongodb_collection), spider=spider)
        return item
