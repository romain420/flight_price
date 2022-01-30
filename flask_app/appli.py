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
    text_per_day = '''
    Il s'agit là d'un histogramme qui donne le prix moyen d'un billet par jour sur tout la durée du temps de scrapping.  

    A l'aide de cet histogramme on peut déduire les jours pour lesquels il est le plus intérressant d'acheter son billet d'avion.

    Dans notre cas il s'agit du Mardi et du Samedi.
    '''
    text_per_hour = '''
    Les deux graphes de gauche nous permettent d'avoir une vision plus précise sur le prix des billets à chaque heure de la journée.

    Dans le premier graphe, en rose, nous avons les informations du pris moyen d'un billet avec un arrêt heure par heure.
    C'est la même lecture pour le graphe violet qui lui montre l'évolution au niveau de la journée du samedi.

    Sur c'est 2 journées la quantité de vol sans arrêt et trop peu importante pour être affiché dans nos graphes, c'est la raison pour laquelle vous ne les voyez donc pas.
    En revanche, nous pouvons déduire un grand nombre de choses de ces 2 graphes. Pour ce qui est du Mardi, on constate que l'heure la plus propice 
    pour acheter un billet et soit le matin à certaines heures précise, soit dans toute la durée de l'après midi/début de soirée (de 14 à 21h), avec un minimum à 16h.
    En revanche pour ce qui est du samedi, il vaut mieux prendre son billet le matin (entre 5h et 13h), même si le moment le moins cher de la journée est à 17h.
    Mais cette heure est assez approximative au vu de la moyenne des prix des heures qui l'entoure.    
    '''
    test = recup()
    price, hours = list_price()
    price_day, day_week = mean_price_day()
    price_nbstop, heure_nbstop, nb_stop = mean_price_day_nbvol()
    color_nbstop = ['rgba(255, 205, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)']
    price_s, hour_s, price_t, hour_t = hour_mean_price()
    aucun_stop = 'nonstop'
    arret_1 = '1stop'
    list_san_arret = flinght_info(aucun_stop)
    list_1_arret = flinght_info(arret_1)
    # comp_alle_sans_arret = list_san_arret[1]
    # comp_alle_1_arret = list_1_arret[1]
    # comp_retour_sans_arret = list_san_arret[2]
    # comp_retour_1_arret = list_1_arret[2]
    # heur_depart_aller_sa = list_san_arret[5]
    # heur_depart_retour_sa = list_san_arret[6]
    # heur_depart_aller_aa = list_1_arret[5]
    # heur_depart_retour_aa = list_1_arret[6]
    # temps_trajet_alle_sa = list_san_arret[7]
    # temps_trajet_retour_sa = list_san_arret[8]
    # temps_trajet_alle_aa = list_1_arret[7]
    # temps_trajet_retour_aa = list_1_arret[8]
    # price_sa = list_san_arret[9]
    # price_aa = list_1_arret[9]

    return render_template("price_comp.html",
                            title='Flight price hour-per-hours',
                            max=1250,
                            test = test, 
                            price = price, 
                            hours=hours, 
                            price_day=price_day, 
                            day_week=day_week, 
                            text_per_day = text_per_day,
                            price_nbstop = price_nbstop,
                            heure_nbstop = heure_nbstop,
                            nb_stop = nb_stop,
                            color = color_nbstop,
                            price_s=price_s,
                            hour_s = hour_s,
                            price_t=price_t,
                            hour_t=hour_t,
                            text_per_hour = text_per_hour,
                            comp_alle_sans_arret=list_san_arret[1],
                            comp_alle_1_arret = list_1_arret[1],
                            comp_retour_sans_arret = list_san_arret[2],
                            comp_retour_1_arret = list_1_arret[2],
                            heur_depart_aller_sa = list_san_arret[5],
                            heur_depart_retour_sa = list_san_arret[6],
                            heur_depart_aller_aa = list_1_arret[5],
                            heur_depart_retour_aa = list_1_arret[6],
                            temps_trajet_alle_sa = list_san_arret[7],
                            temps_trajet_retour_sa = list_san_arret[8],
                            temps_trajet_alle_aa = list_1_arret[7],
                            temps_trajet_retour_aa = list_1_arret[8],
                            price_sa = list_san_arret[9],
                            price_aa = list_1_arret[9])


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
    

