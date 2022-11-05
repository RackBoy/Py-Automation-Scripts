from mailer import Mailer

class mailer:
	def __init__(self, SENDER_EMAIL, SENDER_PASS):
		self.SENDER_EMAIL = SENDER_EMAIL
		self.SENDER_PASS = SENDER_PASS
		#Mailer(self.SENDER_EMAIL, self.SENDER_PASS)

	def send_mail(self, receptor, rsubject, rcontent):
		self.receptor = receptor
		self.rsubject = rsubject
		self.rcontent = rcontent

		mail = Mailer(self.SENDER_EMAIL, self.SENDER_PASS)

		mail.send (receiver = self.receptor,
        subject = self.rsubject,
        message = self.rcontent)
	
	def send_file(self, receptor, rsubject, rcontent, file):
		self.receptor = receptor
		self.rsubject = rsubject
		self.rcontent = rcontent
		self.file = file

		mail = Mailer(self.SENDER_EMAIL, self.SENDER_PASS)

		mail.send (receiver = self.receptor,
        subject = self.rsubject,
        message = self.rcontent,
        files = self.file)
		 #image="angry.png")

	def send_image(self, receptor, rsubject, rcontent, file):
		self.receptor = receptor
		self.rsubject = rsubject
		self.rcontent = rcontent
		self.file = file

		mail = Mailer(self.SENDER_EMAIL, self.SENDER_PASS)

		mail.send (receiver = self.receptor,
        subject = self.rsubject,
        message = self.rcontent,
		image = self.file) 

	def send_audio(self, receptor, rsubject, rcontent, file):
		self.receptor = receptor
		self.rsubject = rsubject
		self.rcontent = rcontent
		self.file = file

		mail = Mailer(self.SENDER_EMAIL, self.SENDER_PASS)

		mail.send (receiver = self.receptor,
        subject = self.rsubject,
        message = self.rcontent,
		audio = self.file)  

	#this method allows to send multiples type of files, audio, file and image at once
	def send_stuff(self, receptor, rsubject, rcontent, file, img, audio):
		self.receptor = receptor
		self.rsubject = rsubject
		self.rcontent = rcontent
		self.file = file
		self.img = img
		self.audio = audio

		mail = Mailer(self.SENDER_EMAIL, self.SENDER_PASS)

		mail.send (receiver = self.receptor,
        subject = self.rsubject,
        message = self.rcontent,
		image = self.img,  
		audio = self.audio, 
		file = self.file )

	def multi_mail(self, multi):
		self.multi = multi
		mail = Mailer(self.SENDER_EMAIL, self.SENDER_PASS)
		if(multi):
			mail.settings(multi=True)
		else:
			return
