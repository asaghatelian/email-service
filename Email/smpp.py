import mandrill
from flask import render_template, request, json, jsonify
from mandrill_email_service import MandrillEmailService
from sendgrid_email_service import SendgridEmailService
from email_service_factory import EmailServiceFactory

class SMPP:
	
	email_service_list = None

	def __init__(self, config):
		service_factory = EmailServiceFactory(config)
		global email_service_list
		email_service_list = [service_factory.create(config, 'mandrill'), service_factory.create(config, 'sendgrid')]
	
	def send_email(self, data):
		failure_count = 0
		for service in email_service_list:
			if service.send(data) == True:
				return self.get_response('Email has been successfully sent with ' + str(failure_count) + ' failures.')
			failure_count += 1
			print 'Service Failed'
		
		return self.get_error('All services have failed!')

	def get_response(self,message):	
		return jsonify(status=200, text=message), 200

	def get_error(self,message):	
		return jsonify(error=400, text=message), 400
