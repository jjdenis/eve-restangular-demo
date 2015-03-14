#!/bin/env python2.7
from eve import Eve
from flask import redirect, send_from_directory, render_template
import os

from flask import request


PWD = os.environ.get("PWD")

# set folder for static data
static_folder = os.path.join(PWD, "static")

# set path for settings file
settings = os.path.join(PWD, "settings.py")

app = Eve(settings=settings, static_folder=static_folder)

# get servername and port from settings file
serverdata = app.config["SERVER_NAME"].split(":")
host = serverdata[0]
port = serverdata[1]


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(static_folder, "images"), "openterm.ico")


@app.route('/index.html')
@app.route('/')
def index_html():
    return send_from_directory(static_folder, "index.html")


@app.route('/entrada.html')
def entrada_html():
    return send_from_directory(static_folder, "entrada.html")


def main():
    app.run(host=host, port=int(port), debug=True)

if __name__ == "__main__":
    main()
