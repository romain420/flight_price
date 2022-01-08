import pymongo
import json
import pandas as pd

def data_pipe(df):
    client = pymongo.MongoClient()
    database = client['dataEngineering']
    collection = database['flight_info']
    flights = df.to_dict(orient = 'records')
    collection.insert_many(flights)

    return print("les données sont pipe dans la collectionn 'flight_info'")
