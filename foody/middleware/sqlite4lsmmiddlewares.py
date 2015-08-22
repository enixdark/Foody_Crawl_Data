from lsm import LSM
from scrapy.conf import settings
import os 

class LSMEngine(object):
	# create lsm key-value database to cache key for update data in other DB
    db = LSM('.'.join([settings['LSM_PATH'],settings['LSM_DBNAME']]))