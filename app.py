import json
from typing import OrderedDict
from flask import Flask, Response, jsonify
from flask_cors import CORS
import pandas as pd
from flask import send_from_directory


app = Flask(__name__)
CORS(app)

@app.route('/male_box_scores', methods=['GET'])
def get_box_scores():
    df = pd.read_csv("men.csv")
    df = df.fillna(value=0)
    records = df.apply(lambda row: OrderedDict(row), axis=1).tolist()
    response = Response(json.dumps(records), mimetype='application/json')
    return response

@app.route('/female_box_scores', methods=['GET'])
def get_box_scores():
    df = pd.read_csv("women.csv")
    df = df.fillna(value=0)
    records = df.apply(lambda row: OrderedDict(row), axis=1).tolist()
    response = Response(json.dumps(records), mimetype='application/json')
    return response


@app.route('/women/')
def serve_women_app():
    return send_from_directory('women_build', 'index.html')

@app.route('/women/<path:path>')
def static_proxy_women(path):
    return send_from_directory('women_build', path)

@app.route('/men/')
def serve_men_app():
    return send_from_directory('men_build', 'index.html')

@app.route('/men/<path:path>')
def static_proxy_men(path):
    return send_from_directory('men_build', path)

if __name__ == '__main__':
    app.run(debug=True)