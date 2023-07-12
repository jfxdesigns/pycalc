import os
def add():
	x = input("First Integer to Add:")
	if (x.isalpha() == "True"):
		print("invalid input, try again.")
		add()
	y = input("Second Integer to Add:")
	if (y.isalpha() == "True"):
		print("invalid input, try again.")
		add()
	x = int(x)
	y = int(y)
	output = (x + y)
	print("The Answer Is")
	print(output)
	print("------------------------------------------------------------------------")
	print("Press Enter to Continue...")
	input()
	os.system("cls")
	prompt()

def multiply():
	x = input("First Integer to Multiply:")
	if (x.isalpha() == "True"):
		print("invalid input, try again.")
		multiply()
	y = input("Second Integer to Multiply:")
	if (y.isalpha() == "True"):
		print("invalid input, try again.")
		multiply()
	x = int(x)
	y = int(y)
	output = (x * y)
	print("The Answer Is")
	print(output)
	print("------------------------------------------------------------------------")
	print("Press Enter to Continue...")
	input()
	os.system("cls")
	prompt()

def subtract():
	x = input("First Integer to Subtract:")
	if (x.isalpha() == "True"):
		print("invalid input, try again.")
		subtract()
	y = input("Second Integer to Subtract:")
	if (y.isalpha() == "True"):
		print("invalid input, try again.")
		subtract()
	x = int(x)
	y = int(y)
	output = (x - y)
	print("The Answer Is")
	print(output)
	print("------------------------------------------------------------------------")
	print("Press Enter to Continue...")
	input()
	os.system("cls")
	prompt()

def divide():
	x = input("First Integer to Divide:")
	if (x.isalpha() == "True"):
		print("invalid input, try again.")
		divide()
	y = input("Second Integer to Divide:")
	if (y.isalpha() == "True"):
		print("invalid input, try again.")
		divide()
	x = int(x)
	y = int(y)
	output = (x / y)
	print("The Answer Is")
	print(output)
	print("------------------------------------------------------------------------")
	print("Press Enter to Continue...")
	input()
	os.system("cls")
	prompt()

def prompt():
	print("Here is a basic Calculator!")	
	print("What would you like to do?")
	print("Options: Add, Subtract, Multiply, Divide")
	option = input()
	if option == "Add":
		add()
	elif option == "Subtract":
		subtract()
	elif option == "Multiply":
		multiply()
	elif option == "Divide":
		divide()
	else:
		print("Invalid Input, Try Again:")
		prompt()
prompt()