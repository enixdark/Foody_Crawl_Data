from mongoengine import Document, StringField
from ..middleware.mongomiddlewares import MongoEngine
class FoodyModel(Document):
    DEFAULT_CONNECTION_NAME = 'foody'
    name = StringField(max_length=255)
    address = StringField(max_length=255)
    lane = StringField(max_length=255)
    city = StringField(max_length=255)
    phone = StringField(max_length=255)
    price_start = StringField(max_length=255)
    price_end = StringField(max_length=255)

