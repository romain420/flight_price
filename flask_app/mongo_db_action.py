import pymongo
import json
from pymongo import MongoClient


#################################################################
#fonction de la page racine
def recup():
    client = MongoClient('mongo')
    database = client['dataEngineering']
    collection = database['app_db']#test
    return next(collection.find())

def flight_number():
    client = MongoClient('mongo')
    database = client['dataEngineering']#"mongo:27018"
    # database = client['dataEngineering']
    collection = database['app_db']#test
    cur = collection.aggregate([{"$group" : {"_id" : "$id_flight"}}])
    return len(list(cur))

def mining_time():
    client = MongoClient('mongo')
    database = client['dataEngineering']
    # database = client['dataEngineering']
    collection = database['app_db']#test
    first = collection.find({}, {"date recup data":1, }).distinct("date recup data")[0]
    last = collection.find({}, {"date recup data":1, }).distinct("date recup data")[len(list(collection.find({}, {"date recup data":1, }).distinct("date recup data")))-1]
    diff = last - first
    return diff
#################################################################



    