from mandrill_email_service import MandrillEmailService
from sendgrid_email_service import SendgridEmailService

class EmailServiceFactory:

	def __init__(self, config):
		self.config = config

	def create(self, config, type):

		if config[type] != '':
			if type == 'mandrill':
				service = MandrillEmailService(config[type])
				return service
			elif type == 'sendgrid':
				service = SendgridEmailService(config[type])
				return service
			else:
				print "not found!"