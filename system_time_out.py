import datetime
import os
from dateutil.parser import parse
import colored
from colored import stylize
from colored import fg, bg, attr
def time_tracker():
	
	#trucking todays date
	today = datetime.date.today()
	#converting today's date to string so as to compare if with one from the file
	today_to_string = str(today)
	
	expiry_date = today + datetime.timedelta(days = 5)
	#print("expiry date is ",expiry_date)
	
	installation_date_file = 'text_files/installation_date.txt'
								
	with open(installation_date_file,'w') as today_date_file_obj:
		date_content = today_date_file_obj.write(str(today))

	with open(installation_date_file,'r') as today_date:
		for installation_date in today_date:#reading per line
			date_of_installation = parse(installation_date.strip(), fuzzy=True).now()

		
	file_name = 'text_files/expiry_date.txt'
	
	#storing date the system was installed (storage is done in text file)
	try:
		#try reading from the file to check if the user can access the system
		with open(file_name,'r') as expiry_date_obj:
			for expiry_string_date in expiry_date_obj:
				date_of_depresion = parse(expiry_string_date.strip(),fuzzy=True)

				#....................
				remaining_date = date_of_depresion - date_of_installation

				date_changed_to_string = str(remaining_date.days)

				if int(date_changed_to_string) > 0:
					print("Hi",os.getlogin().upper(),"You have",date_changed_to_string,"days of Trial version Please upgrade to premium, Today is ")
					#print(stylize("Hi",os.getlogin().upper(),"You have",date_changed_to_string,"days of Trial version Please upgrade to premium",colored.fg("red")))
					import class_based_system
					import todays_time_in_words


				elif int(date_changed_to_string) <= 0:


					print( stylize("""
Your subscription expired

Please upgrade to premium version
contact Systems Admin at piusbagambe@gmail.com 
OR Call : +256 754523742 (Developer)
			""",colored.fg("red")))
					input()
					exit()
				
				#global date_of_depresion
	except FileNotFoundError:
		#if file containing dates is not found, then create as below
		with open(file_name, 'w') as file_name_obj:
			print("Done creating all necesary files")
			expiry_date = file_name_obj.write(str(expiry_date))

#time_tracker()
