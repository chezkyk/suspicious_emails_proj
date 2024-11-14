from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'email_messages'
COLLECTION_NAME = "all_messages"



def get_mongo_connection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]