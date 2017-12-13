import datetime
import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()

def insert_mongo(database_name, collection_name, json):
    """Insert MongoDB"""
    database = client[database_name]
    collection = database[collection_name]
    collection.insert_one(json)
