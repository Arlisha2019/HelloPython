#snake case = first_number
#camel case =firstNumber

print("Hello")
#input function ALWAYS returns a String data type
#a = 10 # integer
#b = "hello" # String
#c = 10.45 # float
#d = True # boolean
#convert the input from string to int
#first_number = float(input("Enter first number: "))
#second_number = float(input("Enter second number: "))
#third_number = float(input("Enter third number: "))

#number = int("45")

#first_number_as_int = int("45")
#second_number_as_int = int("70")

#some_result = first_number_as_int + second_number_as_int
#result = first_number + second_number + third_number
#result = int(first_number) + int(second_number)
#print(result)

#name = input("Enter your name: ")

#print(name)

#name = "John"
#age = 20
#version = 3.35
# Print will print the value of name variable to tthe screen
#print(name)

#name = "Mary"

#print(name)

#string concatcentration

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter city: ")
state = input("Enter State: ")
zip_code = input("Enter Zip Code: ")

message = "My name is {0},{1} and I live in {2}, {3}, {4}".format(first_name,last_name,city,state,zip_code)
#message = "My name is " + first_name + ", " + last_name + ", " + " and I live in " + city + ", " + state + " " + zip_code
print(message)
