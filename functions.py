# conditions

if(1 == 1):
    print("EQUAL")
    a = 10
    b = 10
    c = a + b
else:
    print("NOT EQUAL")







#functions or methods

def validate_age(age):
    if(age >= 18):
        print("age is greater than 18")
    elif(age < 13):
        print("age is less than 13")
    else:
        print("age is not greater than 18 and not less than thirteen")


validate_age(15)

def evenOrOdd(number):
    if (number % 2 == 0):
        print("Even")
    else:
        print("ODD")
evenOrOdd(7)




#def = defines a function
#JavaScrit
#function greet() {}

#python
#def greetJohn():
    #print("Hello John!")
#def greetMary():
    #print("Hello Mary!")

#greetJohn()
#greetMary()
#make = "Honda" is the defaukt value for make if make is not provided. If you crate a default variable it has to be the last one or it will not work
def display_car_information(model, make):
    print("--------------")
    print("Make {0} - Model {1}".format(make,model))


def add(first_number, second_number):
    return first_number + second_number
    print("Hey what about me! ") # this line is completly ignored after the return line has beeen written, you can have multiple returns

def greet(name, age):
    print("Hello, " + name)

#display_car_information("Honda","Accord")
#explicity specify the name of the parameter
display_car_information(model = "Accord", make = "Honda")

#greet("John", 32)

#result = add(2,3)

#print(result)


#this is not the correct order to pass a String
#greet(32,"John")
