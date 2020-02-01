#!/usr/bin/python3

# Coding Sample for NWEA by Melissa Cunningham
# Objective: Build a blog post API
# Provide an API that will write single posts to the database and retrieve a list of all posts from the database.

import requests
import flask
import json
import sqlite3
from flask import jsonify, request, abort, make_response

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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/',methods=['GET'])
def home():
    web_string="<h1>Desmond is the COOLEST!!!</h1><p>He loves pizza and LEGOS!</p>"
    return web_string
    #return "<h1>Desmond is the COOLEST!!!</h1><p>He loves pizza and LEGOS!</p>"

@app.route('/api/v1/blog_entries/all',methods=['GET'])
def get():
    #return json.dumps(blog_entries, sort_keys=False)
    #Json has better formatting below but is sorted
    database_get()
    return jsonify({'blog_entries': blog_entries})

@app.route('/api/v1/blog_entries',methods=['POST'])
def post():
    if not request.json or not 'title' in request.json:
        abort(400)
    new_post = {
        'title': request.json['title'],
        'body': request.json.get('body', "")
    }
    database_post("some_title1", "some_body1")
    return jsonify({'post_list': new_post}), 201
    #return "status.HTTP_201_CREATED and new post is "

def database_get():
    db_connection=sqlite3.connect("blog.db")
    print("Database connection was successful\n")

    all_records=db_connection.execute("select * from posts;")

    return_json=""
    return_json="{'blog_entries': ["
    for record in all_records:
        return_json+="{'post_id': " + str(record[0]) + ", 'title': '" + str(record[1]) + "', 'body': '" + str(record[2]) + "'}, "
    #remove trailing space and comma off the end of the string
    return_json=(return_json.rstrip(" ,"))
    return_json+="],}\n"
    print(return_json + "\n\n")

    db_connection.close()

def database_post(title,body):
    print(title + " " + body)

    db_connection=sqlite3.connect("blog.db")
    print("Database connection was successful\n")

    db_connection.execute("insert into posts('title','body') values('" + title + "','" + body + "');")
    db_connection.commit()
    #get exit code
    print("Insertion was successful\n\n")

    db_connection.close()

if __name__ == '__main__':
    app.run()
