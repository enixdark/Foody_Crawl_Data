from mongoengine import connect
from scrapy.conf import settings
import os 
class MongoEngine(object):
    connection = connect('mongo', host=os.path.join(settings.get('MONGODB_URI'),settings['MONGODB_DATABASE']))
