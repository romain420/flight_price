from flask import Flask, render_template
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/price_comp.html")
def price_comp():
    return render_template("price_comp.html")

@app.route('/bonjour')
def bonjour():
    jaaj = '<h1>Bonjour</h1>'
    return jaaj

@app.route('/mongo')
def data_recup():
    client = pymongo.MongoClient()
    database = client['dataEngineering']
    collection = database['project_collection']
    first = collection.find()
    first = str(next(first))
    #first = str(first)
    # for i in first:
    #     i = str(i)
        
    return first


if __name__ == '__main__':
    app.run(debug=True, port=2745) 

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
    

