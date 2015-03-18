#!/bin/env python2.7
from eve import Eve
import os

from flask import request

import textwrap
import json
import pprint

# set folder for static data
PWD = os.environ.get("PWD")
static_folder = os.path.join(PWD, "static")

app = Eve(static_folder=static_folder)

LINE_LENGTH = 80

# import logging
# log = logging.getLogger('werkzeug')
# logging.basicConfig(level=logging.WARNING)

# These functions show the full request and response.


@app.before_request
def before():
    print('\n\n')
    print '< %s %s' % (request.method, request.url)
    for k, v in request.headers:
        print wrap_header(k, v, '<')

    # print(request.headers['content-type'])
    # print('')

    if request.mimetype == 'application/json':
        print wrap_json(request.data, '<')

    print('')


@app.after_request
def after(response):
    print '> %s' % response.status
    for k, v in response.headers:
        print wrap_header(k, v, '>')

    if response.mimetype == 'application/json':
        print wrap_json(response.data, '>')

    return response


def wrap_json(json_string, sign):
    pprinted = pprint.pformat(
        json.loads(json_string), width=LINE_LENGTH).split('\n')
    spaced = ['{} {}'.format(sign, l) for l in pprinted]
    finished = []
    for line in spaced:
        indent = line.find(':') + 4
        line_wrapped = textwrap.fill(
            line, LINE_LENGTH, subsequent_indent=' ' * indent)
        finished.append(line_wrapped)
        # spaced = ['{} {}'.format(sign, l) for l in line_wrapped]

    return '\n'.join(finished)


def wrap_header(header, value, sign):
    interm = '%s: %s' % (header, value)
    indent = len(header) + 2
    wrapped = textwrap.wrap(
        interm, LINE_LENGTH, subsequent_indent=' ' * indent)
    spaced = ['{} {}'.format(sign, l) for l in wrapped]

    return '\n'.join(spaced)


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()


#     elif response.mimetype == 'text/html':
#         print wrap_html(response.data, '<')

# def wrap_html(html_string, sign):
#     separated = html_string.split('\n')
#     space = '\n {}'.format(sign)

#     return space.join(separated[0:10])
