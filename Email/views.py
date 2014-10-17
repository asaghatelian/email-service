from flask import render_template
from Email import Email

@Email.route('/')
def index():
    return render_template('index.html')

@Email.route('/compose')
def compose():
    return render_template('email.html')
