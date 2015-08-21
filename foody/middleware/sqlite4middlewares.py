from lsm import LSM
from scrapy.conf import settings
import os 

class LSMEngine(object):
    db = LSM('.'.join([setings['LSM_PATH'],settings['LSM_DBNAME']]))