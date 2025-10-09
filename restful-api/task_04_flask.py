#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request


PORT = 5000

app = Flask(__name__)


@app.route('/')
def home(self):
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(list(USERS.keys())), 200


@app.route('/status')
def status():
    response = make_response("OK", 200)
    response.header["Content-Type"] = "text/plain"
    return response


@app.route('/users/<username>')


@app.route('/users')


if __name__ == "__main__":
    app.run()
