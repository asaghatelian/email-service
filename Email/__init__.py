from flask import Flask, url_for
from smpp import SMPP
import os,config

Email = Flask(__name__)

Email.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

from Email import views
