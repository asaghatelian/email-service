from flask import render_template, request, json, jsonify
from Email import Email, config
from SMPP import *

@Email.route('/')
def index():
    return render_template('index.html')

@Email.route('/email', methods=['POST'])
def email():
	try:
	    data = json.loads(request.data)
	except Exception:
		return get_error('Invalid json object')

	smpp = SMPP(config.CONFIG)
	#smpp.send_email(data)

	return ''

def get_error(error_txt):	
	return jsonify(error=400, text=error_txt), 400