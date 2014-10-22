from flask import render_template, request, json, jsonify
from Email import Email, config
from smpp import SMPP

@Email.route('/')
def index():
    return render_template('index.html')

@Email.route('/email', methods=['POST'])
def email():
	try:
		data = json.loads(request.data)
	except Exception:
		return get_error('Invalid json object')

	if not isValid(data):
		return get_error('Invalid json object')

	if SMPP.email_service_list == None:
		smpp = SMPP(config.CONFIG)
	
	return smpp.send_email(data)

def get_error(error_txt):	
	return jsonify(error=400, text=error_txt), 400

def isValid(data):
	if 'to' not in data or 'from' not in data:
		return False
	return True
