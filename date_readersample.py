from system_time_out import  time_tracker
def date_comparison():
	try:

		with open('today_date.txt','r') as today_date:
			for line in today_date:#reading per line
				if line.strip(): #removing the last space per line
					print(line)
								
	except FileNotFoundError:
	
		print("Done Creating data files cost_of_prod.txt")
		with open(today_date_file,'w') as today_date_file_obj:
			date_content = today_date_file_obj.write(str(today))
	
	
	try:

		with open('expiry_date.txt','r') as expiry_date:
			for linedate in expiry_date:#reading per line
				if linedate.strip(): #removing the last space per line
					print(linedate)
								
	except FileNotFoundError:

		print("Done Creating data files cost_of_prod.txt")
	
	if line == linedate:
		print("we are ok now !!!! ")
	
	else:
		print("check your if blocks very well")
		
date_comparison()
						
