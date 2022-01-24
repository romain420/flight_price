import pymongo
import json

def recup():
    client = pymongo.MongoClient()
    database = client['dataEngineering']
    collection = database['app_db']
    return next(collection.find())

def flight_number():
    client = pymongo.MongoClient()
    database = client['dataEngineering']
    collection = database['app_db']
    cur = collection.aggregate([{"$group" : {"_id" : "$id_flight"}}])
    return len(list(cur))

def mining_time():
    client = pymongo.MongoClient()
    database = client['dataEngineering']
    collection = database['app_db']
    first = collection.find({}, {"date recup data":1, }).distinct("date recup data")[0]
    last = collection.find({}, {"date recup data":1, }).distinct("date recup data")[len(list(collection.find({}, {"date recup data":1, }).distinct("date recup data")))-1]
    diff = last - first
    return diff




    