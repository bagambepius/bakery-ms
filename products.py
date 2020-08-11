from datetime import datetime,timedelta
#number_trucker = 0
#stock list
stock = ['Enter Number of Square Cakes: ','Enter Number of Medium Cakes: ','Enter Number of Roll Cakes: ','Enter Number of Queen Cakes: ',
			'Enter Number of Special Cookie: ','Number of Ordinally Cookie Small: ',
			'Enter Number of Ordinally Cookie Big: ','Enter Number of T.Cakes: ','Enter Number of Marble Cakes: ']

stock_price = [800,2000,2500,2500,2000,2500,2500,800,2000]
def stock_manager():
	for_loop_testing = 0

	for cakes in range(len(stock)):		

	#this holders stock capched by for loop
		print("You Have",len(stock)-cakes, "Items to Enter")
		input_list_of_stock = int(input(stock[cakes]))
		#total money in stock after overall entry

		for_loop_testing = for_loop_testing +(input_list_of_stock*stock_price[cakes])
		#print(for_loop_testing)
		#sum_of_entered_stock = sum_of_entered_stock + input_list_of_stock
		#print(sum_of_entered_stock)

		#calculating cash per number of item entered
		calculate_cash_per_item = input_list_of_stock*stock_price[cakes]
		#return(calculate_cash_per_item)
		print("Amount of Cash for stock of",input_list_of_stock,"Cakes = ",calculate_cash_per_item,"ugx")
		print("Total Amount of Overall Stock = ",for_loop_testing,"ugx")
		print("---"*14)

		#tracking stock calculation date (writing date to file)
		calculation_date = datetime.now()
		file_name = 'text_files/calculation_date.txt'
		with open(file_name,'w') as file_date:
			date_of_calculation = file_date.write(str(calculation_date))

	#saving total cash in stock for profit calculation.
	file_name = 'text_files/cash_in_stock.txt'
	with open(file_name,'w') as file_obj:
		content = file_obj.write(str(for_loop_testing) + '\n')
		print("Your Stock is Done Thanks")
		print("Total Cash in Stock is ",for_loop_testing,"ugx (Saved to database)")
		print("--"*28)
		print("")

#stock_manager()
import class_based_system
