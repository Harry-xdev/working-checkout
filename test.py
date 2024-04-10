import webbrowser
import time
import datetime
import psutil


def open_browser():
	link = 'https://working-history.onrender.com'
	delay_time = 3
	time.sleep(delay_time)
	webbrowser.open(link)


def close_browser():
   for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in ['chrome.exe', 'firefox.exe', 'msedge.exe']:
            proc.kill()

def check_time():
	time.sleep(2)
	current = datetime.datetime.now()
	min = current.minute
	print('current min: ' , min)
	return min

while True:
	min = check_time()
	t = 0
	if min % 10 == t:
		print('t: ', t)
		open_browser()
		time.sleep(500)
		close_browser()