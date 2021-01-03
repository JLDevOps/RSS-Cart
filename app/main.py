from flask import Flask, make_response, render_template, send_from_directory, Response
from app.rss import create_rss_feed
import multiprocessing
import os
import os.path
from os import path
import threading
import time

app = Flask(__name__, static_folder='/app/', static_url_path='')
app_start = time.time()

@app.before_first_request
def execute_job():
    def create_rss_file():
        while True:
            create_rss_feed()
            time.sleep(120)
    threading.Thread(target=create_rss_file).start()

@app.route('/feed', methods=['GET'])
def rss_feed():
    if not path.exists("rss.xml"):
        create_rss_feed(filename='rss.xml')

    if path.exists("rss-new.xml"):
        os.remove("rss.xml")
        os.rename('rss-new.xml','rss.xml')

    with open('rss.xml', encoding="utf8") as file:
        response = make_response(file.read())
        response.headers["Content-type"] = "application/rss+xml"
        return response

