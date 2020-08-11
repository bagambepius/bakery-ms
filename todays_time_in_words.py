from datetime import datetime

def print_today():

	today = datetime.now()
	nice_time = datetime.strftime(today,'%A %B %d, %Y')
	print(nice_time)

print_today()
