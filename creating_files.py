file_name = 'file_checker.txt'
try:
	with open(file_name) as file_obj:
		content = file_obj.read()
		print(content)
except FileNotFoundError:
	print("Done Creating data files ",file_name)
	f = open(file_name, 'w')

