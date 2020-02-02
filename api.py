#!/usr/local/bin/python3

# Coding Sample for NWEA by Melissa Cunningham
# Contents: A blog post API that 1)writes single posts to a database and
# 2)retrieves a list of all posts from a database.

import requests
import flask
import json
import sqlite3
from flask import jsonify, request, abort, make_response

app=flask.Flask(__name__)
app.config["DEBUG"]=True

# Route for /posts
@app.route('/posts',methods=['GET'])
def get():
    blog_entries=database_get()
    return blog_entries

# Route for /post
@app.route('/post',methods=['POST'])
def post():
    # requiring title, body and a json type request
    if not request.json or not 'title' in request.json or not 'body' in request.json:
        abort(400)
    new_post = {
        'title': request.json['title'],
        'body': request.json['body']
    }
    database_post(new_post["title"], new_post["body"])
    return jsonify({'post_list': new_post}), 201

# Routing for all other cases
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Dictionary for row_factory use in database_get
def database_dictionary(cursor,row):
    posts_dictionary={}
    for index, column in enumerate(cursor.description):
        posts_dictionary[column[0]]=row[index]
    return posts_dictionary

# Connect to db and get all posts
def database_get():
    db_connection=sqlite3.connect("blog.db")
    db_connection.row_factory=database_dictionary
    cursor=db_connection.cursor()
    all_records=cursor.execute("select * from posts;").fetchall()
    return jsonify({'blog_entries' : all_records})
    db_connection.close()

# Connect to db and insert new post
def database_post(title,body):
    db_connection=sqlite3.connect("blog.db")
    db_connection.execute("insert into posts('title','body') values('" + title + "','" + body + "');")
    db_connection.commit()
    db_connection.close()

if __name__ == '__main__':
    app.run()

