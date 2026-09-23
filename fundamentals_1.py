#1.create a python script with both single-line and multi-line comments ,explaining the purpose of the script.

#SINGLE-LINE COMMENTS-
#This line is a single-line comment.
# It starts with a "#" symbol
#python ignores anything written after "#" on the same line.

'''MULTI-LINE COMMENTS:
you can also use triple quotes (single or double) to write multi-line comments.
these are often used for long explanation.
'''

###########################################################################################################################

#2.declare two variables,one storing an integer and the other a string.print their values.

var_1 = 3
print(var_1)
print(type(var_1))
var_2 = "hello"
print(var_2)
print(type(var_2))

###########################################################################################################################

#3.write a program that prints a pattern using multiple print statements.

print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

###########################################################################################################################

#4.create a python script for a simple task and add comments to explain each step.

num_1 = 9 #declaring a variable and assigning a value to it.
num_2 = 18 #declaring another variable and assigning a value to it.
result = num_2-num_1  #performing and subtraction operation to get the result.
print(result) #applying print function to display the output/result.

''''The above python script performs the 
substraction operation by declaring two variables and
 display the output/result of the operation by using print function.'''

##########################################################################################################################

#5.create variables of different data types(int,float,str) and print their values.

var_1 = 1
print(var_1)
print(type(var_1))

var_2 = 1.5
print(var_2)
print(type(var_2))

var_3 = "hello"
print(var_3)
print(type(var_3))

########################################################################################################################

#6.determine the datatype of a variable.

variable = "datatype" #declare a variable and assigning an datatype value to it.
print(variable)
print("the data type of variable is:")
print (type(variable))

##########################################################################################################################

#7.display the memory address.

num  = 1   #declare a variable and assigning a value.
print(num) #using print function to display the variable.
print(id(num)) #using an "id()" function to display the memory address.

##########################################################################################################################

#8.create a program that takes user input for their age,converts it to an integer,add 5,and then prints the result.

age = int(input("enter your age:"))
print(age+5)

##########################################################################################################################

#9.concatenate two strings and print the result.

string_1 = "hello"
string_2 = "world"
print(string_1+string_2)