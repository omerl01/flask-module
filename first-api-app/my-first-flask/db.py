from pymongo import MongoClient
import os
from dotenv import load_dotenv

# get mongo uri from .env
load_dotenv()

# set global variables client and db
_client = None
_db = None

#establish a connection with mongo
def init_db():
    global _client, _db
    mongo_uri = os.getenv("MONGO_URI")
    _client = MongoClient(mongo_uri)
    _db = _client["prod"]

# get a db information
def get_collection(name):
    return _db[name]
    