#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/index', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World from vineet'}), mimetype='application/json', status=200)


if __name__ == '__main__':
    flaskrun(application)
