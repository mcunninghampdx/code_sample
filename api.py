#!/usr/bin/python3


import requests
import flask
import json
#from flask import jsonify, request

app=flask.Flask(__name__)
app.config["DEBUG"]=True




blog_entries= [
   {'post_id': 1,
    'title': 'Still Raining Today',
    'body': 'First blog entry'},
   {'post_id': 2,
    'title': 'Sun Came Out',
    'body': 'This is the second blog entry'}
]




@app.route('/',methods=['GET'])
def home():
    web_string="<h1>Desmond is the COOLEST!!!</h1><p>He loves pizza and LEGOS!</p>"
    return web_string
    #return "<h1>Desmond is the COOLEST!!!</h1><p>He loves pizza and LEGOS!</p>"

@app.route('/api/v1/blog_entries/all',methods=['GET'])
def dictionary():
    return json.dumps(blog_entries, sort_keys=False)
    #Json has better formatting below but is sorted
    #return jsonify(blog_entries)

app.run()
