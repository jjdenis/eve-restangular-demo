#!/bin/env python2.7
from eve import Eve
import os

# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.DEBUG)


from flask import request


# set folder for static data
PWD = os.environ.get("PWD")
static_folder = os.path.join(PWD, "static")

app = Eve(static_folder=static_folder)

app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')


def main():
    app.run(debug=False)

if __name__ == "__main__":
    main()
