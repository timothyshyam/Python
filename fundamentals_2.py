#1.define a list containing three different data types.

list = [1,1.5,"hello"]
print(list)
print(type(list))

#########################################################################################################################

#2.define a set containing employee id.

employee_id = {1,5,9}
print(employee_id)
print(type(employee_id))

###########################################################################################################################

#3.repeat a string 3 times and display the output.

str_var = "hello"
print(str_var*3)

##########################################################################################################################

#4.create a variable with a name that is a python keyword.what happens?observation.

'''python keyword = "hello"
it throws an syntax error here ,
when we give spaces while declaring a variable name.
'''
python_keyword = "hello"
print(python_keyword)

#########################################################################################################################3

#5.convert a float to an integer and print the result.

float_value = 1.5
print (float_value)
print(type(float_value))
print(int(float_value))
print(type(int(float_value)))

##########################################################################################################################

#6.convert a  integer to a string and display the output.

int_value = 9
print(int_value)
print(type(int_value))
print(str(int_value))
print(type(str(int_value)))

###########################################################################################################################

#7.implement a program that uses a dictionary to store and display about a book.

book = {"book name":"mission impossible","author":"Tom cruise","publication":2025}
print(book)
print(type(book))

#########################################################################################################################

#8.write a python program that takes a string as input(35) and return a float value.

str_input =input("enter a number:")
print(float(str_input))

##########################################################################################################################

#9.write a program to take two names as input and print them together.

input_1 = input("enter first name:")
input_2 = input("enter second name:")
print(input_1+input_2)