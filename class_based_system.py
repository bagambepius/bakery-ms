from __future__ import division
from colored import fg, bg, attr
import os
import colored
from colored import stylize
import popup
from previous_prod import previous_production
import products
from datetime import datetime,timedelta
from calculation_date_reader import date_reader
from system_time_out import time_tracker
print("")
date_reader()
now = datetime.now()

#print(now)
#from products import stock_manager
time_tracker()
print (""".................................................................................

	Welcome to Cake Recip and Stock Management System...
	The Application Does the following

	* Calculates cake recip according to used flour(in Kgs).
	* Calculates the total cash in available cake stock.
	* Calculates the total cost of production.
	* Perfectly Aids managers in profit calculation.

	 """)

#print("	*** Choose One of Options Below ***")
print("	.."*5)

class Recip_and_Production_Cost:
	#defining class variables
	entry = 'yes'
	wrong_entries = 0
	## preset values for one killogram of flour(1kg)
	eggs = 11
	citric = 10
	salt = 5
	sorbate = 20
	viniger = 10
	water = 390
	cooking_oil = 625
	sugar = 550
	gel = 50
	soda_bi = 5
	xanthangum = 3
	baking_powder = 50
	cornflour = 25
	tam_cookies = 200
	sugar_cookies = 400
	eggs_cookies = 5.2 #pcs of eggs
	Flour = 1000 #grams
	electricity = 1700

	
	#unit cost per item in uganda shilling(everything in grams)
	one_egg = 326 #cost per egg 
	#sorbate_cost
	one_gram_sorbate = 18 #cost per gram 
	citric_cost = 7  #cost per gram
	salt_cost = 2  #cost per gram
	viniger_cost = 5  #cost per gram
	water_cost = 0.02  #cost per gram
	one_gram_cooking_oil = 4.8  #cost per gram
	one_gram_sugar = 2.88  #cost per gram
	gel_cost = 20  #cost per gram
	soda_bi_cost = 4  #cost per gram
	xanthangum_cost = 12  #cost per gram
	baking_powder_cost = 10  #cost per gram
	cornflour_cost = 5  #cost per gram
	flour_cost = 2.52 #cost per gram (1000grams cost 2520ugx)
	electricity_cost = 1700 #cost per kg

	#initialising instance variable using class constuctor
	def __ini__(self,entry='yes'):

		#declaring instance variables 
		self.entry = entry
		#self.gel = gel

	def user_entry(self):

	
		while self.entry is not 'No': #NB entry variable being picked from class variaables

			entry = input(" Enter yes/y to continue or No/n to logout : ")
			if entry == "yes" or entry=="y" or entry=="YES":
				user_choice = int(input("""
	(1) For Recip Calculation :
	(2) For Cake Cost of Production :
	(3) For Stock Calculation and Cash Management :
	(4) For Profit Calculation : """))
				print("")

				#print(type(user_choice))
				if user_choice ==1:
					print("")
					flour_input=float(input(" Enter flour(Ngano) in killograms to mix:  "))
					gel = flour_input*Recip_and_Production_Cost.gel
					soda_bi = flour_input*Recip_and_Production_Cost.soda_bi
					xanthangum = flour_input*Recip_and_Production_Cost.xanthangum
					baking_powder = flour_input*Recip_and_Production_Cost.baking_powder
					eggs = flour_input*Recip_and_Production_Cost.eggs
					sorbate = flour_input*Recip_and_Production_Cost.sorbate
					citric = flour_input*Recip_and_Production_Cost.citric
					salt = flour_input*Recip_and_Production_Cost.salt
					viniger = flour_input*Recip_and_Production_Cost.viniger
					water = flour_input*Recip_and_Production_Cost.water
					cooking_oil = flour_input*Recip_and_Production_Cost.cooking_oil
					sugar = flour_input*Recip_and_Production_Cost.sugar
					print("")
					print("Eggs..........",eggs,"(pcs)")
					print("sorbate.......",sorbate,"(grams)")
					print("citric........",citric,"(grams)")
					print("salt..........",salt,"(grams)")
					print("viniger.......",viniger,"(grams)")
					print("water.........",water,"(grams)")
					print("cooking_oil...",cooking_oil,"(grams)")
					print("sugar.........",sugar,"(grams)")
					print("CakeGel.......",gel,"(grams)")
					print("Soda_bi.......",soda_bi,"(grams)")
					print("xanthangum....",xanthangum,"(grams)")
					print("baking_powder.",baking_powder,"(grams)")
					print("")

				elif user_choice == 2:
					print("")
					print(" *** User Guide Notes for Stock Management System ***")
					print("""

	*)- Enter overall flour(Ngano) used in production eg 24(kg)

	*)- The system will calculate the exact recip
	   used in that amount & total cost of production in(ugx)
		""")

					input_used_flour=float(input(stylize(" Enter flour(Ngano) in killograms Used in Production:  ", colored.fg("green"))))
					#total calculation per item
					total_cost_sorbate = (Recip_and_Production_Cost.sorbate*input_used_flour)*Recip_and_Production_Cost.one_gram_sorbate
					total_cost_eggs = (Recip_and_Production_Cost.eggs*input_used_flour)*Recip_and_Production_Cost.one_egg
					total_cost_citric_acid = (Recip_and_Production_Cost.citric*input_used_flour)*Recip_and_Production_Cost.citric_cost
					total_cost_salt = (Recip_and_Production_Cost.salt*input_used_flour)*Recip_and_Production_Cost.salt_cost
					total_cost_viniger = (Recip_and_Production_Cost.viniger*input_used_flour)*Recip_and_Production_Cost.viniger_cost
					total_cost_water = (Recip_and_Production_Cost.water*input_used_flour)*Recip_and_Production_Cost.water_cost
					total_cost_cooking_oil = (Recip_and_Production_Cost.cooking_oil*input_used_flour)*Recip_and_Production_Cost.one_gram_cooking_oil
					total_cost_sugar = (Recip_and_Production_Cost.sugar*input_used_flour)*Recip_and_Production_Cost.one_gram_sugar
					total_cost_cakegel = (Recip_and_Production_Cost.gel*input_used_flour)*Recip_and_Production_Cost.gel_cost
					total_cost_soda_bi = (Recip_and_Production_Cost.soda_bi*input_used_flour)*Recip_and_Production_Cost.soda_bi_cost
					total_cost_xanthangum = (Recip_and_Production_Cost.xanthangum*input_used_flour)*Recip_and_Production_Cost.xanthangum_cost
					total_cost_baking_powder = (Recip_and_Production_Cost.baking_powder*input_used_flour)*Recip_and_Production_Cost.baking_powder_cost
					total_cost_cornflour = (Recip_and_Production_Cost.cornflour*input_used_flour)*Recip_and_Production_Cost.cornflour_cost
					total_cost_of_flour = (Recip_and_Production_Cost.Flour*input_used_flour)*Recip_and_Production_Cost.flour_cost
					total_cost_electricity = (Recip_and_Production_Cost.electricity_cost*input_used_flour)

					print("")
					print("This is the total cost of production for ",input_used_flour,"killograms used")
					print("")
					print("Item...........Quantity.............Total Cost")
					print("")
					print("Eggs..........",Recip_and_Production_Cost.eggs*input_used_flour,"(pcs)","..........",total_cost_eggs,"ugx") 
					print("sorbate.......",Recip_and_Production_Cost.sorbate*input_used_flour,"(grams)","........", total_cost_sorbate,"ugx")
					print("citric........",Recip_and_Production_Cost.citric*input_used_flour,"(grams)","........",total_cost_citric_acid,"ugx")
					print("salt..........",Recip_and_Production_Cost.salt*input_used_flour,"(grams)","........",total_cost_salt,"ugx")
					print("viniger.......",Recip_and_Production_Cost.viniger*input_used_flour,"(grams)","........",total_cost_viniger,"ugx")
					print("water.........",Recip_and_Production_Cost.water*input_used_flour,"(grams)","......",total_cost_water,"ugx")
					print("cooking_oil...",Recip_and_Production_Cost.cooking_oil*input_used_flour,"(grams)","......",total_cost_cooking_oil,"ugx")
					print("sugar.........",Recip_and_Production_Cost.sugar*input_used_flour,"(grams)","......",total_cost_sugar,"ugx")
					print("CakeGel.......",Recip_and_Production_Cost.gel*input_used_flour,"(grams)",".......",total_cost_cakegel,"ugx")
					print("Soda_bi.......",Recip_and_Production_Cost.soda_bi*input_used_flour,"(grams)","........",total_cost_soda_bi,"ugx")
					print("xanthangum....",Recip_and_Production_Cost.xanthangum*input_used_flour,"(grams)","........",total_cost_xanthangum,"ugx")
					print("baking_powder.",Recip_and_Production_Cost.baking_powder*input_used_flour,"(grams)",".......",total_cost_baking_powder,"ugx")
					print("Cornflour.....",Recip_and_Production_Cost.cornflour*input_used_flour,"grams",".........",total_cost_cornflour,"ugx")
					print("Flour(Engano).",Recip_and_Production_Cost.Flour*input_used_flour,"(grams)-->",Recip_and_Production_Cost.Flour*input_used_flour/1000,"kgs",total_cost_of_flour,"ugx")
					print("Electricity------------------->",Recip_and_Production_Cost.electricity*input_used_flour,"(ugx)")
					print("")

					Total_cost_of_production =total_cost_electricity + total_cost_of_flour + total_cost_cornflour +total_cost_baking_powder+total_cost_xanthangum+total_cost_soda_bi+total_cost_cakegel+total_cost_sugar+total_cost_cooking_oil+total_cost_water+total_cost_viniger+total_cost_salt+total_cost_citric_acid+total_cost_sorbate+total_cost_eggs
					print("Total Cost Of Production for",input_used_flour,"kgs = ",Total_cost_of_production,'ugx (Saved for profit calculation)')
					
					print("-"*50)
					#saving data in file to read from during profit calculation
					file_name = 'text_files/cost_of_prod.txt'
					#opening file
					try:
						with open(file_name,'w') as file_object:
							costofproduction = file_object.write(str(Total_cost_of_production))
						#print("Done saving your information!!")

					#declaring date variable
						costofproduction_date = datetime.now()
					except FileNotFoundError:
						
						print("Done Creating data files ",file_name)
						f = open(file_name, 'w')

					#file containing date of production
					filename = 'text_files/production_date.txt'
					try:
						with open(filename,'w') as file_date:
							date_of_production = file_date.write(str(costofproduction_date))


					except FileNotFoundError:

						print("Done Creating data files ",filename)
						production_date = open(filename, 'w')



				elif user_choice == 3:

					'''calling the imported module'''
					print("Welcome to Stock Calculation and Cash Management.")
					print("Please Enter stock Numbers to Calculate")
					print("-----------------------------------------------------------")
					products.stock_manager()

				elif user_choice == 4:
					print('-'*60)

					"""
					we can to read from two txt files ..
					1 - file storing total cost of production
					2 - from file storing total cash in stock
					"""
					date_reader()
					#reading from the fast file(cost_of_prod.txt)
					try:

						with open('text_files/cost_of_prod.txt','r') as cost_of_production:
							for line in cost_of_production:#reading per line
								if line.strip(): #removing the last space per line
									total_cost_of_prod = int(float(line)) #converting to float then to string as desired
								#return total_cost_of_prod
								#print(type(total_cost_of_prod))
					except FileNotFoundError:

						print("Done Creating data files cost_of_prod.txt")
						production_date = open('text_files/cost_of_prod.txt', 'w')

					#reading from cash_in_stock file
					try:

						with open('text_files/cash_in_stock.txt','r') as cash_in_stock:
							for lines in cash_in_stock:
								if lines.strip():
									Total_cash_in_stock = int(float(lines))
					
					except FileNotFoundError:

						print("Done Creating data files cash_in_stock.txt")
						production_date = open("text_files/cash_in_stock.txt", 'w')

					'''
					We need to check if current date is 
					equal to dates when total cost of production
					and total cash in stock were generated. if not 
					warn the user about it......
					'''
					#....................................................
					#reading from production_date.txt file
					with open('text_files/production_date.txt','r') as date_file:
						for line_of_date in date_file:
							if line_of_date.strip():
								formated_date = line_of_date[:10]
							#	print(line_of_date[:10])
					#reading from calculation_date
					with open('text_files/calculation_date.txt','r') as calculation_date_file:
						for lines_of_date in calculation_date_file:
							if lines_of_date.strip():
								current_date = lines_of_date[:10]

					#converting current date to string and triming it
					today = str(now)

					#..........................................................

					if today[:10] == line_of_date[:10] and today[:10] == current_date and Total_cash_in_stock > total_cost_of_prod :
					#profit calculation
						profits = Total_cash_in_stock - total_cost_of_prod

						print(

	"""
	Profit calculation depends on :
	1) Cost of production .
	2) Total cash in stock.

	(Profit = Total cash in stock - cost of production)
	""")
						print("Today's profit is ",profits,"ugx")
						print("---"*12)

						print(" ")

					elif today[:10] == line_of_date[:10] and today[:10] == current_date and Total_cash_in_stock < total_cost_of_prod :
						print("")
						print("You have made a lose of",Total_cash_in_stock - total_cost_of_prod,'(ugx)')
						print("---"*12)

					else:
						
						import tkinter.messagebox as mb
						mb.showinfo("You are Using Out Dated Figures", "You are Using Out Dated Figures ,Make sure the DataBase is up todate. This may lead to wrong calculations fast run (2) and (3)")

						print(
							"""

	NB: WARNING ..This may lead to wrong calculations.
	Fast generate "Cost of Production(2)" and "Total Cash in Stock(3)"
							""")
						#print('You last updated your database on',current_date)
						cal_input = input(" Do you realy want to Calculate profits for previous Production? : Y)es , N)o : "  )
						print("")
						if cal_input == 'y' or cal_input == 'Y' or cal_input == "yes" or cal_input == "YES":
							#print("invoking another module")
							previous_production()


			elif entry is not "n" and entry is not "NO" and entry is not "no" and entry is not "N" and Recip_and_Production_Cost.wrong_entries < 3:
				
				print(" Wrong Entry Please Try Again ..",)
				Recip_and_Production_Cost.wrong_entries +=1
				#print(Recip_and_Production_Cost.wrong_entries)

				if Recip_and_Production_Cost.wrong_entries >= 3:
					exit("You have entered three(3) wrong entries.. system locked")

			elif entry == "no" or entry =="n" or entry == "NO" or entry == "N":
						exit("**** You have loged out  ****")
calling_class = Recip_and_Production_Cost() #creating new class object
calling_class.user_entry()