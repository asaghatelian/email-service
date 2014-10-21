from MandrillEmailService import *
from SendgridEmailService import *

class EmailServiceFactory:

	def __init__(self, config):
		self.config = config

	def create(self, config, type):
		print "creating a service of type " + type + " with configuration of:"
		print config[type]
		print ''
		if config[type] != '':
			if type == 'mandrill':
				service = MandrillEmailService(config[type])
				return service
			elif type == 'sendgrid':
				service = SendgridEmailService(config[type])
				return service
			else:
				print "not found!"