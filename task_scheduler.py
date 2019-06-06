import schedule
import time
import datetime

def fun_minute():
	print("current time is")
	print(datetime.datetime.now())
	print("schedular executed after minute")

def fun_hour():
	print("current time is")
	print(datetime.datetime.now())
	print("schedular executed after hour")

def fun_day():
	print("current time is")
	print(datetime.datetime.now())
	print("schedular executed after day")

def fun_Afternoon():
	print("current time is")
	print(datetime.datetime.now())
	print("schedular executed at 6")

def main():

	print("python job scheduler")
	print(datetime.datetime.now())
	
	schedule.every(1).minutes.do(fun_minute)
	
	schedule.every().hour.do(fun_hour)
	
	schedule.every().day.at("00:00").do(fun_Afternoon)

	schedule.every().sunday.do(fun_day)

	schedule.every().saturday.at("18:30").do(fun_day)


	while True:
		schedule.run_pending()
		time.sleep(1)

if __name__=="__main__":

	main()	
