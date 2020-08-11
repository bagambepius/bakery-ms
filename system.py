print ("""...Welcome to BANA Bakers Recip and Stock Management System...
	The Application Does the following

	* Asks user the amount of flour(in Kgs)
	* Calculates the Recip or total cost of operation
	 """)

print("	*** Choose One of Options Below ***")
print("	.."*5)

while True:
	user_input = int(input("""
	(1) For Recip Calculation :
	(2) For Cake Cost of Production :
	(3) For Cookie Cost of Production :
	(4) For Profit Calculation : """))
	print("")
	#if user_input =="":
	#	print("User input required")
	def recip_calculation():
		## preset values for one killogram of flour(1kg)
		eggs = 11
		sorbate = 20
		citric = 10
		salt = 5
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

		if user_input == 1:

			print("")
			flour_input=int(input(" Enter flour(Ngano) in killograms to mix:  "))
			gel = flour_input*gel
			soda_bi = flour_input*soda_bi
			xanthangum = flour_input*xanthangum
			baking_powder = flour_input*baking_powder
			eggs = flour_input*eggs
			sorbate = flour_input*sorbate
			citric = flour_input*citric
			salt = flour_input*salt
			viniger = flour_input*viniger
			water = flour_input*water
			cooking_oil = flour_input*cooking_oil
			sugar = flour_input*sugar
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
			#print("Flour(Engano).",Flour,"(grams)")


		elif user_input == 2:

			print("")

			print("***** Bana Bakery Stock Management System*****")
			print("")
			print(" ...User Guide Notes...")
			print("""

	-->Enter overall flour(Ngano) used in production eg 24(kg) and press enter
	-->The system will calculate the exact recip used in that amount and there total cost 

			""")

			#unit cost per item in uganda shilling(everything in grams)
			one_egg = 266 #cost per egg 
			#sorbate_cost
			one_gram_sorbate = 18 #cost per gram 
			#............................................
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
			electricity_cost = 1700

			input_used_flour=int(input(" Enter flour(Ngano) in killograms Used:  "))
			
			#............opening price holders....................
			total_cost_sorbate = (sorbate*input_used_flour)*one_gram_sorbate
			total_cost_eggs = (eggs*input_used_flour)*one_egg
			total_cost_citric_acid = (citric*input_used_flour)*citric_cost
			total_cost_salt = (salt*input_used_flour)*salt_cost
			total_cost_viniger = (viniger*input_used_flour)*viniger_cost
			total_cost_water = (water*input_used_flour)*water_cost
			total_cost_cooking_oil = (cooking_oil*input_used_flour)*one_gram_cooking_oil
			total_cost_sugar = (sugar*input_used_flour)*one_gram_sugar
			total_cost_cakegel = (gel*input_used_flour)*gel_cost
			total_cost_soda_bi = (soda_bi*input_used_flour)*soda_bi_cost
			total_cost_xanthangum = (xanthangum*input_used_flour)*xanthangum_cost
			total_cost_baking_powder = (baking_powder*input_used_flour)*baking_powder_cost
			total_cost_cornflour = (cornflour*input_used_flour)*cornflour_cost
			total_cost_of_flour = (Flour*input_used_flour)*flour_cost
			total_cost_electricity = (electricity_cost*input_used_flour)
			#............closing of price holhers..........
			print("")
			print("This is the total amount of Ingredients used in",input_used_flour,"killograms used")
			print("")
			print("Item...........Quantity............Cost")
			print("")
			print("Eggs..........",eggs*input_used_flour,"(pcs)","..........",total_cost_eggs,"ugx") 
			print("sorbate.......",sorbate*input_used_flour,"(grams)","........", total_cost_sorbate,"ugx")
			print("citric........",citric*input_used_flour,"(grams)","........",total_cost_citric_acid,"ugx")
			print("salt..........",salt*input_used_flour,"(grams)","........",total_cost_salt,"ugx")
			print("viniger.......",viniger*input_used_flour,"(grams)","........",total_cost_viniger,"ugx")
			print("water.........",water*input_used_flour,"(grams)","......",total_cost_water,"ugx")
			print("cooking_oil...",cooking_oil*input_used_flour,"(grams)","......",total_cost_cooking_oil,"ugx")
			print("sugar.........",sugar*input_used_flour,"(grams)","......",total_cost_sugar,"ugx")
			print("CakeGel.......",gel*input_used_flour,"(grams)",".......",total_cost_cakegel,"ugx")
			print("Soda_bi.......",soda_bi*input_used_flour,"(grams)","........",total_cost_soda_bi,"ugx")
			print("xanthangum....",xanthangum*input_used_flour,"(grams)","........",total_cost_xanthangum,"ugx")
			print("baking_powder.",baking_powder*input_used_flour,"(grams)",".......",total_cost_baking_powder,"ugx")
			print("Cornflour.....",cornflour*input_used_flour,"grams",".........",total_cost_cornflour,"ugx")
			print("Flour(Engano).",Flour*input_used_flour,"(grams)-->",Flour*input_used_flour/1000,"kgs",total_cost_of_flour,"ugx")
			print("Electricity------------------->",electricity*input_used_flour,"(ugx)")
			print("")
			
			#print(total_cost_electricity)
			#Total_cost_of_proction

			Total_cost_of_proction =total_cost_electricity + total_cost_of_flour + total_cost_cornflour +total_cost_baking_powder+total_cost_xanthangum+total_cost_soda_bi+total_cost_cakegel+total_cost_sugar+total_cost_cooking_oil+total_cost_water+total_cost_viniger+total_cost_salt+total_cost_citric_acid+total_cost_sorbate+total_cost_eggs

			print("Total Cost Of Production for",input_used_flour,"kgs = ",Total_cost_of_proction,'ugx')
			print("-"*50)

		elif user_input == 3:
			enter_cookie_flour = int(input(" Enter Flour(kg) You Used to Make Cookies: "))
			sugar_for_cookies = enter_cookie_flour*sugar_cookies
			print("****************** Not Complete *******************")
			print("Cost of Sugar = ",sugar_for_cookies)
			#tam_cookies = 200
			#sugar_cookies = 400
			#eggs_cookies = 5.2 #pcs of eggs

			#calculating ingredients for cookies

		elif user_input == 4:

			print(".."*30)
			print("We Shall Need Cost of Production so as to Calculat Total Profits")
			exit("...............")
			

		else:
			print("Please provide right input")

	recip_calculation()
	another_recip = int(input(" Do You Want to Perform another Operation?? 1(Yes) 2(No)"))

	if another_recip == 1 or another_recip == "yes" or another_recip=="Yes" or another_recip=="YES":
		#print("..........You have entered another loop..........")
		recip_calculation()
		#exit()
	elif another_recip == 2:
		exit("You have ended the Application")