from getpass import getpass
import popup
fast_entry = True
import colored
from colored import stylize

while fast_entry:

	def password_validator():
		password_lst = ['admin@dw']
		#print(password_lst)
		#pwd = "admin@dw"

		print("")
		user_password = getpass("Enter password to login :  ")

		if user_password in password_lst:
			#print("Login success")
			print(stylize("Login success.", colored.fg("green")))
			import class_based_system

		else:

			import tkinter.messagebox as mb
			mb.showinfo("Login failed please try again", "Login failed please try again ")
			#print("Login failed please try again")
			print(stylize("Login failed please try again.", colored.fg("red")))


	password_validator()
