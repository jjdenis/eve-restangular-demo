#!/bin/env python2.7
from eve import Eve
import os

from flask import request


# set folder for static data
PWD = os.environ.get("PWD")
static_folder = os.path.join(PWD, "static")

app = Eve(static_folder=static_folder)


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
