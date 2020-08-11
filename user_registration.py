from getpass import getpass
def account_creation():
	enter_password = getpass("Enter Your Password to Register : ")
	password_lst.append(enter_password)
	print("Your password has been stored")

account_creation()