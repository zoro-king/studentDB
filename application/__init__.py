from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['SECRETE_KEY'] = "ZORO"
app.config['MONGO_URI'] = "mongodb+srv://vetrivel-smartail:slayer007@cluster0.4l2dkrl.mongodb.net/?retryWrites=true&w=majority"

#setup mongodb
mongodb_client = PyMongo(app)

from application import routes
