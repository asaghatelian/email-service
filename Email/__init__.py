from flask import Flask, url_for
import os

Email = Flask(__name__)

Email.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

from Email import views
