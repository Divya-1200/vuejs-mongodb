from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
import pymongo
from bson.json_util import dumps
from flask_pymongo import PyMongo
import os
from decouple import config

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['MONGO_URI'] = config('MONGO_URI') 
mongo = PyMongo(app)
dbenter = mongo.db.data_collection

@app.route("/dataentry", methods=["POST","GET"])
def submit_data():
    response_object = {'status':'success'}
    if request.method == "POST":

        post_data = request.get_json()
        
        data = {

            "company"        : post_data.get('company'),
            "designation"    : post_data.get('designation'),
            "review"    : post_data.get('review')
        }

        print(data)
        
        dbenter.insert_one(data)
        
        response_object['message'] ='Data added!'
        return jsonify(response_object)


@app.route("/view", methods=["POST","GET"])
def view_data():



    return "Hello"


if __name__ == '__main__':
    
    app.run(debug=True)