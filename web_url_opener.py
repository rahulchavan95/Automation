from sys import *
from urllib.request import *
import re
import webbrowser

def is_connected():
	try:
		urlopen('http://216.58.192.142',timeout=1)
		return True

	except Exception as err:
		return False

def Find(string):
	url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
	return url



def WebLauncher(path):
	with open(path) as fp:
		for line in fp:
			print(line)
			url=Find(line)
			print(url)
			for str in url:
				webbrowser.open(str,new=2)
	



def main():
	if(len(argv)!=2):
		print('invalid number of arguments')
		exit()

	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("this script is used to open url from file")
		exit()
	
	if(argv[1]=="-u") or (argv[1]=="-U"):
		print("Application Name ",argv[0])
		exit()

	try:
		connected=is_connected()
		
		if connected:
			WebLauncher(argv(1))
		else:
			print("unable to connect to internet")

	except ValueError:
		print("invalid datatype of input")
	
	except Exception as E:
		print("invalid input",E)


if __name__=="__main__":
	main()
