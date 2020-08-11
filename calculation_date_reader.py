def date_reader():

	try:

		with open('text_files/calculation_date.txt','r') as calculation_date_file:
			for lines_of_date in calculation_date_file:
				if lines_of_date.strip():
					current_date = lines_of_date[:10]

	except FileNotFoundError:
		production_date = open("text_files/calculation_date.txt", 'w')
