from sys import *
import time
import smtplib
from urllib.request import *


def is_connected():
	try:
		urlopen('http://216.58.192.142',timeout=1)
		return True

	except Exception as err:
		return False


def MailSender(gmail_user,gmail_password):

	sent_from=gmail_user
	to=['abc@gmail.com']                                          #enter recepient email id

	email_text='Hello.........'


	try:
		server=smtplib.SMTP_SSL('smtp.gmail.com',465)
		server.ehlo()
		server.login(gmail_user,gmail_password)
		server.sendmail(sent_from,to,email_text)
		server.close()

		print('mail sent successfully')

	except Exception as E:
		print('unable to send mail',E)


def main():
	
	try:
		gmail_user='xyz@gmail.com'                                #enter sender email id
		gmail_password='*******'

		connected=is_connected()

		if connected:
			starttime=time.time()
			MailSender(gmail_user,gmail_password)
			endtime=time.time()
		
			print('took %s seconds to evaluate' % (endtime-starttime))

		else:
			print('there is no internet connection')

	except Exception as E:
		
		print('error:invalid input',E)





if __name__=="__main__":
	main()		
