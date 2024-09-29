from flask import Flask, json, make_response
from flask import request, jsonify
from src.common.firebaseObj import FireBaseObj
from src.db_accessor import add_to_db
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)
app.config.from_file('config.json', load=json.load)

cred = credentials.Certificate(app.config['FIREBASE_KEY'])
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/")
def index():
    return "Finance Tracker"

@app.route("/add-spending", methods = ['POST'])
def add_spending():
    data = request.get_json()
    obj = FireBaseObj(**data)
    response = add_to_db.add_to_db(db, obj)

    return response.to_dict()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)