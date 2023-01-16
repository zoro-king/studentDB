from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MONGO_URI'] = "mongodb+srv://vetrivel-smartail:slayer007@cluster0.4l2dkrl.mongodb.net/?retryWrites=true&w=majority"

#setup mongodb
#mongodb_client = PyMongo(app)
client=MongoClient("mongodb+srv://vetrivel-smartail:slayer007@cluster0.4l2dkrl.mongodb.net/?retryWrites=true&w=majority")
db=client['studentdb']
collection=db['stud_flask']

from application import routes
