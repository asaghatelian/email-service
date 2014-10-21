import sendgrid
from sendgrid import SendGridError, SendGridClientError, SendGridServerError

class SendgridEmailService(object):
	def __init__(self,config):
		self.config = config
		self.sendgrid = sendgrid.SendGridClient(config['username'], config['password'], raise_errors=True)

	def send(data):
		message = sendgrid.Mail()
		message.add_to(data['to'])
		message.set_subject(data['subject'])
		message.set_text(data['text'])
		message.set_from(data['from'])
		message.add_to(data['cc'])
		message.add_bcc(data['bcc'])

		try:
			sg.send(message)
		except SendGridClientError:
			print SendGridClientError
		except SendGridServerError:
			print SendGridServerError

