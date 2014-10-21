import json
import mandrill
from Email import *
from EmailServiceFactory import *

class SMPP:
	def __init__(self, config):
		service_factory = EmailServiceFactory(config)

		email_service_list = [service_factory.create(config, 'mandrill'), service_factory.create(config, 'sendgrid')]

		print email_service_list
	
	def send_email(data):
		print data
		return ''
	