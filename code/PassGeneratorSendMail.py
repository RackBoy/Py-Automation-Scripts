import string 
import random
from mailerrr import mailer

SENDER_EMAIL = ''
SENDER_PASS = ''

#set up parameters
email_receptor = ''
subject = "Password:"
lengPass = 15

m = mailer(SENDER_EMAIL, SENDER_PASS)

#decorator function here
def sendByMail(flag): #bool type
	def decorator(func): #receive Genpass function
		def wrapper(*args, **kwargs):
			if(flag):
				m.send_mail(email_receptor, subject, GenPass(*args))
			else: 
				return
		return wrapper
	return decorator

#using decorators by deafult
#@sendByMail(*args)
def GenPass(leng):
	passs = []
	listChar = ""
	listChar +=  string.digits
	listChar +=  string.ascii_letters
	listChar +=  string.punctuation
	for i in range(leng):
		randoVal = random.choice(listChar)
		passs.append(randoVal)
	return "".join(passs)


def main():
	sendByMail(True)(GenPass)(lengPass) # this is another way of using decorators
	#print("new pass: ",GenPass(15)) #use this when aint necessary to send by mail


if __name__ == '__main__':
	main()
