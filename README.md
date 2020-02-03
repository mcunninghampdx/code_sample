# Blog Post API

This repository contains the elements of a simple blog post api with two endpoints. One endpoint will write a single blog post to a database and a second endpoint will retrieve all blog posts from a database.

# Included in the Repository

* blog.db: SQLite database file that contains a few entries already 
* api.py: Python api script
* index.html: HTML file for webpage that contains info about the endpoints including examples
* styles.css: Stylesheet file to support the webpage index.html
* LICENSE: Apache license (in case it's needed)
* README.md: Self-explanatory
* testscript.py: An early file that was merged into api.py mid-way through development

# Prerequisites

Apache, SQLite, Python, Flask, git, and an internet browser have to be installed on your environment. My personal set up: 
* Apache 2.4.33, SQLite 3.19.3, Python 3.7.6, Flask 1.1.1, git 2.17.2, Google Chrome 79.0.3945.130

# Assumptions

1. This api runs locally.
2. The /post endpoint does not check for the validity or security of the input before entering title and body strings into the SQLite database. 

# API Installation and Verification

1. Clone this repository to intended host:
* git clone https://github.com/mcunninghampdx/code_sample.git

2. Move or copy the following files to the Apache site file location that you use such as the default location of /Library/WebServer/Documents (this may require moving current files such as index.html out of the way). My personal Sites folder was at /Users/mcunninghampdx/Sites, for example:
* api.py, blog.db, index.html, styles.css
* Edit the api.py file so that the routes are correct for your Apache location

3. Verify the Python/Flask/SQLite set up:
* Run the python api script: python3 api.py
* At the command line, try to use the /posts endpoint using the POSTS CURL COMMAND below 
* At the command line, try to use the /post endpoint using the POST CURL COMMAND below

4. Verify the Apache/index.html/styles.css set up
* With the python api script still running
* Start apache: sudo apachectl start
* Open an internet browser and navigate to http://localhost:5000/. You should see the Blog API homepage with information about each available endpoint
* On the homepage, click the link to expose the /posts endpoint. The returned JSON should match the response from the /posts curl command tried in a previous step. 
* At the command line, both the /posts and /post endpoints using curl should still work
* Success! Start freely using the Blog API endpoints.

5. Issues?
* Load the index.html Blog API page for general endpoint information. NOTE: This can be done without being connected (by using File->Open in your internet browser).
* Check the Apache logs: /var/log/apache2/ directory
* Python issues (including SQLite issues) will print to the screen that is running python3 api.py

POSTS CURL COMMAND: curl -i http://localhost:5000/posts 

POST CURL COMMAND: curl -i -H "Content-Type: application/json" -X POST -d '{"title":"This is a blog title","body":"This is a blog entry"}' http://localhost:5000/post

# Authors

Melissa Cunningham

# Comments

I thought a nice touch would be to create a webpage exposing the 2 endpoints for people to use. I was able to wire up the /posts endpoint (see the link in index.html). The /post endpoint was a little problematic and is still a WIP.
