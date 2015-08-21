from redis import Redis, ConnectionPool
from scrapy.conf import settings
import os 

class RedisEngine(object):
    redis = Redis(connection_pool= ConnectionPool(host=settings.get('REDIS_URL'),port=settings['REDIS_PORT'],db=settings['REDIS_DBNAME']))