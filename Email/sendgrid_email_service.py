import sendgrid,traceback
from sendgrid import SendGridError, SendGridClientError, SendGridServerError

class SendgridEmailService(object):
	def __init__(self,config):
		self.config = config
		self.sg = sendgrid.SendGridClient(config['username'], config['password'], raise_errors=True)

	def send(self,data):
		message = sendgrid.Mail()
		message.add_to(data['to'])
		message.set_from(data['from'])
		
		if 'cc' in data and data['cc'] != '':
			message.add_to(data['cc'])

		if 'bcc' in data and data['bcc'] != '':
			message.add_bcc(data['bcc'])

		if 'subject' in data and data['subject'] != '':
			message.set_subject(data['subject'])

		if 'message' in data and data['message'] != '':
			message.set_text(data['message'])

		else:
			message.set_text('')

		try:
			self.sg.send(message)
			return True
		
		except SendGridClientError:
			print traceback.format_exc()
			return False
		
		except SendGridServerError:
			print traceback.format_exc()
			return False

