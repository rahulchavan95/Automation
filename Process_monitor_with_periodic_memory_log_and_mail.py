import psutil
import os
import time
import urllib2
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def is_connected():
	try:
		urlopen('http://216.58.192.142',timeout=1)
		return True

	except Exception as err:
		return False



def MailSender(filename,time):
	try:
		fromaddr="abc@gmail.com"
		toaddr="xyz@gmail.com"
		
		msg=MIMEMUltipart()
		msg['From']=fromaddr
		msg['To']=toaddr

		body="""
		HEllo %s,
		PFA.
		Log file is created at %s.

		This is auto generated main.
		
		Thanks & Regards,
		Rahul Chavan
		"""%(toaddr,time)

		subject="""
		Process log of system generated at %s"""%(time)
	
		msg['Subject']=subject
		
		msg.attach(MIMEText(body,'plain'))
		attachment=open(filename,"rb")
		p=MIMEBase('application','octet-stream')

		p.set_payload((attachment).read())
		encoders.encode_base64(p)
	
		p.add_header('Content-Disposition',"attachment; filename= %s"%filename)

		msg.attach(p)
		s=smtplib.SMTP('smtp.gmail.com',587)

		s.starttls()
		s.login(fromaddr,"passwd")                          #enter your password at "passwd"
		text=msg.as_string()

		s.sendmail(fromaddr,toaddr,text)
		s.quit()

		print("Log file successfully sent through mail")
	
	except Exception as E:
		print("unable to send mail",E)

	

def ProcessLog(log_dir="log_file"):
	listprocess=[]

	if not os.path.exists(log_dir):
		try:
			os.mkdir(log_dir)
		except:
			pass

	separator="-"*80
	log_path=os.path.join(log_dir,"log_file%s.log"%(time.ctime())
	f=open(log_path,'w')
	f.write(separator+"\n")
	f.write("Process Logger "+time.ctime()+"\n")
	f.write(separator+"\n")
	f.write("\n")

	for proc in psutil.process_iter():
		
		try:
			pinfo=proc.as_dict(attrs=['pid','name','username'])
			
			listprocess.append(pinfo)

		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
			pass


	for element in listprocess:
		f.write("%s\n"%element)

	print("log file is generated at location %s "%(log_path))

	connected=is_connected()

	if connected:
		starttime=time.time()
		MailSender(log_path,time.ctime())
		endtime=time.time()




def memory_usage_display():

	listprocess=[]

	for proc in psutil.process_iter():
		
		try:
			pinfo=proc.as_dict(attrs=['pid','name','username'])
			pinfo['vms']=proc.memory_info().vms/(1024*1024)
			
			listprocess.append(pinfo)

		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
			pass
	
	return listprocess	






def process_display():

	listprocess=[]

	for proc in psutil.process_iter():
		
		try:
			pinfo=proc.as_dict(attrs=['pid','name','username'])
			
			listprocess.append(pinfo)

		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
			pass
	
	return listprocess	




def main():

	print("Process Monitor Log")

	#listprocess=process_display()
	if(len(argv)!=2):
		print("invalid no of arguments")
	
	if(argv[1]=="-h" or argv[1]=="-H"):
		print("this script is used to generate log of processes of system")


	try:
		schedule.every(int(argv[1])).minutes.do(ProcessLog)
		while(True):
			schedule.run_pending()
			time.sleep(1)

	except Exception as E:
		print("invalid datatype of input")
	
	

	
if __name__=="__main__":
	main()
