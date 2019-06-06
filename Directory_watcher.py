from sys import *
import os


def DirectoryWatcher(path):
	
	flag=os.path.isabs(path)
	if flag==False:
		path=os.path.abspath(path)
		
	exists=os.path.isdir(path)

	if exists:

		for foldername,subfolder,filename in os.walk(path):
			print('current folder is: '+foldername)
			#for subf in subfolder:
			#	print('subfolder of '+foldername+'is'+subf)
				
			for filen in filename:
				print("files are ",filen)
			print('')

	else:
		print('invalid path')




def main():
	
	if(len(argv)!=2):
		print("invalid number of arguments")

	if(argv[1]=='-h') or (argv[1]=='-H'):
		print("traverse directory")
		exit()		

	if(argv[1]=='-u') or (argv[1]=='-U'):
		print("traverse directory")
		exit()
	

	try:
		DirectoryWatcher(argv[1])

	except Exception as E:
		print("invalid input",E)



if __name__=="__main__":
	main()
