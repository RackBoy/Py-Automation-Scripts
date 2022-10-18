'''
this class is only used with
passGeneratorSendMail in order to send
passwords generated to an especific mail address
when its required
'''
# old port 587
import smtplib 
import ssl 
from email.message import EmailMessage

class mailer:
	def __init__(self, SENDER_EMAIL, SENDER_PASS):
		self.SENDER_EMAIL = SENDER_EMAIL
		self.SENDER_PASS = SENDER_PASS

	def send_mail(self, receptor, rsubject, rcontent):
		self.receptor = receptor
		self.rsubject = rsubject
		self.rcontent = rcontent
		email = EmailMessage()
		email['from'] = self.SENDER_EMAIL
		email['to'] = self.receptor
		email['subject'] = self.rsubject
		email.set_content(self.rcontent)
		contexto = ssl.create_default_context()
		with smtplib.SMTP_SSL('smtp.gmail.com', port = 465, context = contexto) as smtp:
			smtp.login(self.SENDER_EMAIL, self.SENDER_PASS)
			smtp.sendmail(self.SENDER_EMAIL, self.receptor, email.as_string())
			print(f"email send to {self.receptor}")
