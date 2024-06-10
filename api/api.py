#!/usr/bin/python3
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HBnB"

if __name__ == "__main__": app.run()
