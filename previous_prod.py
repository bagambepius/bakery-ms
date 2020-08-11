def previous_production():
	
	#reading from both previous production_cost file and cash_stock_file
	with open('text_files/cost_of_prod.txt','r') as cost_of_production:
		for line in cost_of_production:#reading per line
			if line.strip(): #removing the last space per line
				total_cost_of_prod = int(float(line)) 
			#converting to float then to string as desired

	with open('text_files/cash_in_stock.txt','r') as cash_in_stock:
		for lines in cash_in_stock:
			if lines.strip():
				Total_cash_in_stock = int(float(lines))

	previous_profits = Total_cash_in_stock - total_cost_of_prod 

	#tracking date the last production was made
	with open('text_files/production_date.txt','r') as date_file:
		for line_of_date in date_file:
			if line_of_date.strip():
				formated_date = line_of_date[:10]
	print("Your profit is",previous_profits,"(ugx) as of Date..",(formated_date))
	print('...'*15)