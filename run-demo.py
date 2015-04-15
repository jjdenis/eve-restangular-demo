#!/bin/env python2.7
from eve import Eve
import os

import curl

# set folder for static data
PWD = os.environ.get("PWD")
static_folder = os.path.join(PWD, "static")

app = Eve(static_folder=static_folder)

LINE_LENGTH = 80

# This adds curl-like logging
curl.add_curl(app)


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
