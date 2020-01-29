#!/usr/bin/python3

# Coding Sample for NWEA by Melissa Cunningham
# Objective: Build a blog post API
# Provide an API that will write single posts to the database and retrieve a list of all posts from the database.


import requests
import sqlite3

def get():
    db_connection=sqlite3.connect("blog.db")
    print("Database connection was successful\n")

    all_records=db_connection.execute("select * from posts;")

    return_json=""
    return_json="{'blog_entries': ["
    for record in all_records:
        return_json+="{'post_id': " + str(record[0]) + ", 'title': '" + str(record[1]) + "', 'body': '" + str(record[2]) + "'}, "
    #remove trailing space and comma off the end of the string
    return_json=(return_json.rstrip(" ,"))
    return_json+="]\n"
    print(return_json + "\n\n")

    db_connection.close()


def post(title,body):
    print(title + " " + body)

    db_connection=sqlite3.connect("blog.db")
    print("Database connection was successful\n")

    db_connection.execute("insert into posts('title','body') values('" + title + "','" + body + "');")
    db_connection.commit()
    #get exit code
    print("Insertion was successful\n\n")

    db_connection.close()


post("some_title1", "some_body1") #title, body
#post("http://api.superblog.com/blog-posts.json?form") #form gives title, body
get()
#"http://api.superblog.com/blog-posts.json"