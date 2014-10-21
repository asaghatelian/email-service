import mandrill

class MandrillEmailService(object):

    def __init__(self,config):
    	self.config = config
    	self.mandrill_client = mandrill.Mandrill(config['api_key'])

	def send(data):
		try:
			message = {
				'from_email' : data['from_email'],

				'to': [
					{
						'email': data['to'],
						'type': 'to'
					},
					{
						'email': data['cc'],
						'type': 'cc'
					},
					{
						'email': data['bcc'],
						'type': 'bcc'
					}

				],

				'subject' : data['subject'],

				'text' : data['text']
			}

			result = mandrill_client.messages.send(message=message, async=False)
		
		except mandrill.Error, e:
		
			print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
			
			raise