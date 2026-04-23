from pymongo import MongoClient
import os
from dotenv import load_dotenv

# get mongo uri from .env
load_dotenv()

# set global client and db variables
_client = None
_db = None

# initialize db connection
def init_db(app):
    global _client, _db
    mongo_uri = os.getenv("MONGO_URI")
    _client = MongoClient(mongo_uri)
    _db = _client["prod"]
    app.config["DB"] = _db
    
# get db information 
def get_collection(name):
    return _db[name]
    