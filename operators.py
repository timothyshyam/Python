#1.write a python program to calculate the area of the rectangle using the given formula(area=length*width).
# take the values of length and width as input from the user. 

length = int(input("enter the length:"))
width  = int(input("enter the width:"))
print (f"length and width of a rectangle are {length} and {width}.the area is {length*width}")

###########################################################################################################################

#2.write a python program to demonstrate incrementing and decrementing of a variable.

input = int(input("enter the variable:"))
print(f"the increment of a variable is : {input+1} and decrement of a variable is : {input-1}")

#########################################################################################################################

#3.write a python program to convert temperature from celsius to farenheit.the formula for conversion is:F = (c*9/5)+32.
#  take the temperature in celsius as input from the user.

temperature = int(input("enter the temperature celsius: "))
conversion = ((temperature*9/5)+32)
print(conversion)

#########################################################################################################################

#4.write the python program to calculate the simple interest given the principal amount,rate,and time(in years).

principal_amount_p = int(input("enter principal amount:"))
rate_r = int(input("enter the rate:"))
time_t = int(input("enter the time:"))
print(f"the simple interest is : {principal_amount_p*rate_r*time_t}")

##############################################################################################################################

#5.write a python program to concatenate two strings and display the results.
#the strings should be taken as input from the user.

str_1 = input("enter 1st string :")
str_2 = input("enter 2nd string :")
print(str_1+str_2)

##########################################################################################################################

#6.write a python program to convert a distance from kilometers to miles.

kilometers = float(input("enter the km :"))
print(f"distance in kilometre is {kilometers} . distance in miles is {kilometers*0.62}")

##############################################################################################################################

#7.create a program that takes user input for their name and age.
# use formatted strings (f-strings) to print a message and welcoming the user and stating their age.

name = input("enter your name:")
age  = input("enter your age:")
print(f"Hi {name}! you are {age}years old. welcome to python life.")

###########################################################################################################################

#8.create a list called numbers that contains integers from 1 to 10. 
#--->check if the number 5 is in the list.
#--->check if the number 15 is not in the list.

numbers = (1,2,3,4,5,6,7,8,9,10)
print (5 in numbers)
print (15 not in numbers)