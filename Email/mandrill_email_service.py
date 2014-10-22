import mandrill

class MandrillEmailService(object):

	def __init__(self,config):
		self.config = config
		self.mandrill_client = mandrill.Mandrill(config['api_key'])

	def send(self,data):
		try:
			message = {}
			
			message['from_email'] = data['from']
			message['to'] = []
			message['to'].append({
				'email': data['to'],
				'type': 'to'
			})

			if 'cc' in data and data['cc'] != '':
				message['to'].append({
					'email': data['cc'],
					'type': 'cc'
				})

			if 'bcc' in data and data['bcc'] != '':
				message['to'].append({
					'email': data['bcc'],
					'type': 'bcc'
				})

			if 'subject' in data and data['cc'] != '':
				message['subject'] = data['subject']

			if 'text' in data and data['cc'] != '':
				message['text'] = data['message']
			else:
				message['text'] = ''
			
			result = self.mandrill_client.messages.send(message=message, async=False)

			return result[0]['status'] == 'sent'
		
		except mandrill.Error, e:
			print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
			return False