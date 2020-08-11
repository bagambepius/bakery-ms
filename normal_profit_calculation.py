def normal_profit():
	#reading from the fast file(cost_of_prod.txt)
	with open('cost_of_prod.txt','r') as cost_of_production:

		for line in cost_of_production:#reading per line
			if line.strip(): #removing the last space per line
				total_cost_of_prod = int(float(line))

				#print(Total_cash_in_stock)
				#print(type(Total_cash_in_stock)) 

				'''
				We need to check if current date is 
				equal to dates when total cost of production
				and total cash in stock were generated. if not 
				warn the user about it......
				'''
				#....................................................
				#reading from production_date.txt file
	with open('production_date.txt','r') as date_file:
		for line_of_date in date_file:
			if line_of_date.strip():
				formated_date = line_of_date[:10]
				#	print(line_of_date[:10])
				#reading from calculation_date

						#reading from production_date.txt file
					
	with open('calculation_date.txt','r') as calculation_date_file:
		for lines_of_date in calculation_date_file:
			if lines_of_date.strip():
				current_date = lines_of_date[:10]

	today = str(now)

	if today[:10] == line_of_date[:10] and today[:10] == current_date and Total_cash_in_stock > total_cost_of_prod :
		#profit calculation
		profits = Total_cash_in_stock - total_cost_of_prod
						
		print(current_date)
		print(formated_date)

		print(

	"""
	Profit calculation depends on :
	1) Cost of production .
	2) Total cash in stock.

	(Profit = Total_cash_in_stock - cost_of_production)
	""")
		print("Today's profit is ",profits,"ugx")

def previous_production():

	#reading from both previous production_cost file and cash_stock_file
	with open('cost_of_prod.txt','r') as cost_of_production:
		for line in cost_of_production:#reading per line
			if line.strip(): #removing the last space per line
				total_cost_of_prod = int(float(line)) 
			#convertingtofloat then to string as desired
			#return total_cost_of_prod
	#			print(type(total_cost_of_prod))
	#print(total_cost_of_prod)

	with open('cash_in_stock.txt','r') as cash_in_stock:
		for lines in cash_in_stock:
			if lines.strip():
				Total_cash_in_stock = int(float(lines))
			#return Total_cash_in_stock
			#print(Total_cash_in_stock)
	#			print(type(Total_cash_in_stock))
	#print(Total_cash_in_stock)
	previous_profits = Total_cash_in_stock - total_cost_of_prod 

	#tracking date the last production was made
	with open('production_date.txt','r') as date_file:
		for line_of_date in date_file:
			if line_of_date.strip():
				formated_date = line_of_date[:10]
	print("Your profit is",previous_profits,"as of Date..",formated_date)
	print('...'*15)
