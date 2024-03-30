from candidateProfile import settings
import pymongo

class MongoDBClient(object):
   def __init__(self, col, index=None):        
      connection = pymongo.MongoClient(settings.MONGODB_URI)
      self.name_col = col
      self.db = connection[settings.MONGODB_DB]
      self.collection = self.db[col]
      if index:
         self.collection.create_index(index, unique=True) 
         
   def refresh_collection(self):
      self.collection.drop()
      self.collection = self.db[self.name_col]
   
   def get_collection(self):
      return self.collection
   
   def _walk(self):
      skip = 0
      limit = 1000
      hasMore = True
      while hasMore:
         res = self.collection.find(skip=skip, limit=limit)
         hasMore = (res.count(with_limit_and_skip=True) == limit)
         for x in res:
               yield x
         skip += limit
      
   def walk(self):
      docs = []
      for doc in self._walk():
         docs.append(doc)
      return docs
    
