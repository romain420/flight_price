from lib2to3.pgen2 import token
from flask import Flask, render_template, jsonify
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongo_db_action import *

app = Flask(__name__)

@app.route("/")
def home():
    token = "pk.eyJ1Ijoicm9tYXgxIiwiYSI6ImNreXBxcGl5MTBjcWoycm1tMzNiMnozOGsifQ.m7f5Grd8oEAIONeVUT4bww"
    text_content = '''
        nhabit hearing perhaps on ye do no. It maids decay as there he. Smallest on suitable disposed do although blessing he juvenile in. Society or if excited forbade. Here name off yet she long sold easy whom. Differed oh cheerful procured pleasure securing suitable in. Hold rich on an he oh fine. Chapter ability shyness article welcome be do on service.

Full age sex set feel her told. Tastes giving in passed direct me valley as supply. End great stood boy noisy often way taken short. Rent the size our more door. Years no place abode in ﻿no child my. Man pianoforte too solicitude friendship devonshire ten ask. Course sooner its silent but formal she led. Extensive he assurance extremity at breakfast. Dear sure ye sold fine sell on. Projection at up connection literature insensible motionless projecting.

Oh he decisively impression attachment friendship so if everything. Whose her enjoy chief new young. Felicity if ye required likewise so doubtful. On so attention necessary at by provision otherwise existence direction. Unpleasing up announcing unpleasant themselves oh do on. Way advantage age led listening belonging supposing.

Be at miss or each good play home they. It leave taste mr in it fancy. She son lose does fond bred gave lady get. Sir her company conduct expense bed any. Sister depend change off piqued one. Contented continued any happiness instantly objection yet her allowance. Use correct day new brought tedious. By come this been in. Kept easy or sons my it done.
    '''
    nb_flight = flight_number()
    mining= mining_time()
    return render_template("index.html", token = token, text_content = text_content, nb_flight = nb_flight, mining = mining)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/price_comp.html")
def price_comp():
    test = recup()
    price, hours = list_price()
    price_day, day_week = mean_price_day()
    return render_template("price_comp.html",title='Flight price hour-per-hours', max=1250, test = test, price = price, hours=hours, price_day=price_day, day_week=day_week)

@app.route('/bonjour')
def bonjour():
    jaaj = '<h1>Bonjour</h1>'
    return jaaj

@app.route('/mongo')
def data_recup():
    client = pymongo.MongoClient('mongo')
    database = client['dataEngineering']
    collection = database['project_collection']
    first = collection.find()
    first = str(next(first))
    #first = str(first)
    # for i in first:
    #     i = str(i)
        
    return first


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000) 

# app.config["MONGO_URI"] = "mongodb://localhost:27017/dataEngineering"
# app.config['MONGO_DBNAME'] = 'project_collection'
# # app.config['SECRET_KEY'] = 'secret_key'

# mongo = PyMongo(app)
# db = mongo.db
# collection = mongo.db["project_collection"]
# print("MongoDB Database:", mongo.db)


# Declare an app function that will return some HTML
# @app.route("/mongo")
# def connect_mongo():
#     # Setup the webpage for app's frontend
#     html_str = '''
#     <!DOCTYPE html>
#     <html lang="fr">
    

#     <body bgcolor = "#979DAC">'''
      
   

#     # Have Flask return some MongoDB information
#     html_str = html_str + '''

#     <h1> Flight price dashboard </h1>

#     '''

#     # Get a MongoDB document using PyMongo's find_one() method
#     html_str = html_str + """

#     """ + str(collection.find_one()) + """

#     </html>
#     </body>"""

#     return html_str



















# @app.route('/')
# def hello_world():
#     return 'Hello World!'
    

