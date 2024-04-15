import datetime


def get_time_2():
	current_time = datetime.datetime.now()
	hour = current_time.time().hour
	minute = current_time.time().minute
	time = current_time.strftime('%H:%M')
	if 10 < minute and minute < 45:
		minute = 30
	if 45 < minute or minute < 15:
		minute = 0
	time_stamp = str(hour) + ':' + str(minute)
	return time_stamp

time_stamp = get_time_2()
print(time_stamp)