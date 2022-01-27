import pymongo
import json
from pymongo import MongoClient
import pandas as pd


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

#################################################################
#fonction de requetes page d'interpretation des prix
def list_price():
    client = pymongo.MongoClient('mongo')
    database = client['dataEngineering']
    collection = database['app_db']
    price_list = [doc['price'] for doc in collection.aggregate([{"$group" : {"_id" : "$date recup data", "price" : {"$avg" : "$price"}}}])]
    hours = [doc['date recup data'] for doc in collection.find()]
    hours_df = pd.DataFrame(hours, columns = ['hours'])
    hours_df = hours_df.drop_duplicates()
    hours_list = hours_df['hours'].tolist()
    hours_list = [str(i) for i in hours_list] 
    for i in range(len(hours_list)):
        hours_list[i] = hours_list[i][:16]
    return price_list, hours_list

def df_price_builder():
    # client = pymongo.MongoClient('mongo')
    # database = client['dataEngineering']
    # collection = database['app_db']
    # price_list = [doc['price'] for doc in collection.find()]
    # hours = [doc['date recup data'] for doc in collection.find()]
    # df = pd.DataFrame({"heure_recup": hours,
    #                "price" : price_list
    #                })
    # return df
    client = pymongo.MongoClient("mongo")
    database = client['dataEngineering']
    collection = database['app_db']
    price_list = [doc['price'] for doc in collection.find()]
    hours = [doc['date recup data'] for doc in collection.find()]
    nb_stop = [doc['Nb stop alle'] for doc in collection.find()]
    df = pd.DataFrame({"heure_recup": hours,
                   "price" : price_list,
                   "nb_stop" : nb_stop
                   })
    return df

def mean_price_day():
    df = df_price_builder()
    df_gb_day = df.groupby(pd.Grouper(key='heure_recup', axis=0, freq='1d')).mean()
    df_gb_day_new = df_gb_day.reset_index() 
    df_gb_day_new['day_of_week'] = df_gb_day_new['heure_recup'].dt.day_name()
    price_list = df_gb_day_new['price'].tolist()
    heure_recup_list = df_gb_day_new['day_of_week'].tolist()
    return price_list, heure_recup_list 

def mean_price_day_nbvol():
    df = df_price_builder()
    df_gb_day_nbstop = df.groupby([pd.Grouper(key='heure_recup', axis=0, freq='1d'), 'nb_stop']).mean()
    df_gb_day_nbstop_new = df_gb_day_nbstop.reset_index()
    df_gb_day_nbstop_new['day_of_week'] = df_gb_day_nbstop_new['heure_recup'].dt.day_name()
    price_list = df_gb_day_nbstop_new['price'].tolist()
    heure_recup_list = df_gb_day_nbstop_new['day_of_week'].tolist()
    nb_stop_list = df_gb_day_nbstop_new['nb_stop'].tolist()
    return price_list, heure_recup_list, nb_stop_list

def hour_mean_price():
    df = df_price_builder()
    df_gb_day_nbstop = df.groupby([pd.Grouper(key='heure_recup', axis=0, freq='1h'), 'nb_stop']).mean()
    df_gb_day_nbstop_new = df_gb_day_nbstop.reset_index()
    df_gb_day_nbstop_new['day_of_week'] = df_gb_day_nbstop_new['heure_recup'].dt.day_name()
    df_gb_day_nbstop_new['time'] = df_gb_day_nbstop_new["heure_recup"].dt.time
    df_gb_day_nbstop_new = df_gb_day_nbstop_new[df_gb_day_nbstop_new['nb_stop'] == '1stop']
    satuday_df = df_gb_day_nbstop_new[df_gb_day_nbstop_new['day_of_week'].isin(['Saturday'])]
    tuesday_df = df_gb_day_nbstop_new[df_gb_day_nbstop_new['day_of_week'].isin(['Tuesday'])]
    price_saturday = satuday_df['price'].tolist()
    hours_saturday = satuday_df['time'].tolist()
    price_tuesday = tuesday_df['price'].tolist()
    hours_tuesday= tuesday_df['time'].tolist()
    return price_saturday, hours_saturday, price_tuesday, hours_tuesday
    