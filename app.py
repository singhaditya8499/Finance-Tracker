from flask import Flask
from flask import request, jsonify
from src.db_accessor.add_spending_to_db import add_to_db

app = Flask(__name__)

@app.route("/")
def index():
    return "Finance Tracker"

@app.route("/add-spending", methods = ['POST'])
def add_spending():
    add_to_db("spending", )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)