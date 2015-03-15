#!/bin/env python2.7
from eve import Eve
import os

from flask import request

import textwrap


# set folder for static data
PWD = os.environ.get("PWD")
static_folder = os.path.join(PWD, "static")

app = Eve(static_folder=static_folder)


# These funcitions show the full request and response.

@app.before_request
def before():
    print
    print '  > %s %s' % (request.method, request.url)
    for k, v in request.headers:
        print wrap_header(k, v)
    print


@app.after_request
def after(response):
    print '  < %s' % response.status
    for k, v in response.headers:
        print wrap_header(k, v)
    return response


def wrap_header(header, value):
    interm = '  > %s: %s' % (header, value)
    indent = len(header) + 6
    wrapped = textwrap.fill(interm, 60, subsequent_indent=' ' * indent)
    return wrapped


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
