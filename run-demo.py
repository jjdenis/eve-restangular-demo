#!/bin/env python2.7
from eve import Eve
import os

from flask import request

import textwrap


# set folder for static data
PWD = os.environ.get("PWD")
static_folder = os.path.join(PWD, "static")

app = Eve(static_folder=static_folder)


import logging
# log = logging.getLogger('werkzeug')

# These funcitions show the full request and response.

# logging.basicConfig(level=logging.WARNING)


@app.before_request
def before():
    print('')
    print '  > %s %s' % (request.method, request.url)
    for k, v in request.headers:
        print wrap_header(k, v, '>')

    print(request.headers['content-type'])
    print('')


@app.after_request
def after(response):
    print '  < %s' % response.status
    for k, v in response.headers:
        print wrap_header(k, v, '<')

    if response.mimetype == 'application/json':
        print response.data

    return response


def wrap_header(header, value, sign):
    interm = '%s: %s' % (header, value)
    indent = len(header) + 2
    wrapped = textwrap.wrap(interm, 60, subsequent_indent=' ' * indent)
    spaced = ['  {} {}'.format(sign, l) for l in wrapped]

    return '\n'.join(spaced)


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
