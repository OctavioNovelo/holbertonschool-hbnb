#!/usr/bin/python3
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/hbnb/api')
def home():
    return "Welcome to HBnB"

if __name__ == "__main__":
    # Added `host` and `port` so it can be accesible from any IP in port 5000
    app.run(host='0.0.0.0', port=5000)
