#VOWEL CHECKER.
#1.write a python program that takes character as input and checks whether it is a vowel or not.use the if-else statement.
"""
character = input("enter the character:")
vowels = ("a,e,i,o,u")
if character in vowels:
    print(f"The character {character} is vowel.")
else:
    print(f"The character {character} is not a vowel.")
"""
#############################################################################################################################

#AGE GROUP CLASSIFICATION.
#2.write a program that takes age as an input and classifies the person into one of the following age groups:
#child - 0 to 12yrs, teenager - 13 to 17yrs, adult - 18 to 64yrs, elder - 65yrs and older.
"""
age = int(input("enter your age:"))
if age>=65:
    print(f"Age is {age},you are an elder.")
elif age>=18 and age<=64:
    print(f"Age is {age},you are an adult.")
elif age>=13 and age<=17:
    print(f"Age is {age},you are an teenager.")
elif age>=0 and age<=12:
    print(f"Age is {age},you are an child.")
else:
    print("invalid input")
"""
##########################################################################################################################

#NUMBER CLASSIFIER.
#3.write a program that takes an integer as input and classifies it as positive,negative or zero.use if-elif-else statement.
"""
int_value = int(input("enter the integer value:"))
if int_value>0:
    print(f"The {int_value} value is positive.")
elif int_value<0:
    print(f"The {int_value} value is negative.")
else:
    print(f"The {int_value} value is zero.")
"""
########################################################################################################################

#LEAP YEAR CHECKER.
#4.create a program that checks whether a given year is a leap year or not. A leap year is divisible by 4,
#but not by 100 unless it is divisible by 400.
"""
year = int(input("enter the year:"))
if year%4 ==0 and year%100 ==0 and year%400==0:
      print(f"{year} is an leap year.")
else:
    print(f"{year} is not an leap year.")  """

###########################################################################################################################

#CALCULATOR.
#5.build a simple calculator program that takes two numbers and an operator(+ - * /) 
# as inputs and perform the corresponding operations.
"""
inp_1 = int(input("enter the 1st number:"))
inp_2 = int(input("enter the 2nd number:"))
operator= input("enter the operator to perform arithmetic operation (+ - * /):")
if operator== "+":
    print(f"result is {inp_1}+{inp_2} = {inp_1+inp_2}")
elif operator== "-":
    print(f"result is {inp_1}-{inp_2} = {inp_1-inp_2}")
elif operator=="*":
    print(f"result is {inp_1}*{inp_2} = {inp_1*inp_2}")
elif operator=="/":
    print(f"result is {inp_1}/{inp_2} = {inp_1/inp_2}")
else:
    print("invalid operation.")  """

#####################################################################################################################################

#SHORT HAND IF:
#6.rewrite the following code using the short hand if statement:
#x=8
#if x%2 == 0: result ="even"
#else: result = "odd"
"""
x = 8
result ="even" if x%2 ==0 else "odd"         #short hand if else is used to simplify lines of code.
print(result)
"""
#######################################################################################################################

#DISCOUNT CALCULATOR:
#7.create a program that calculates the final price after applying a discount.
#the program should take the original price and discount percentage as input.
"""
original_price = int(input("enter the original price:"))
discount_percentage = int(input("enter the discount percentage:"))
discounted_price = original_price*(discount_percentage/100)
print(f"The final price is {int(original_price-discounted_price)}")
"""

#########################################################################################################################

#BMI CALCULATOR:
#8.write a program that calculates the body mass index(BMI) using the formula: BMI = weight (in kg)/(height(m))^2.
#the program should take weight and height as an input.

weight = int(input("enter the weight(in kg):"))
height = int(input("enter the height(m) :"))
print(f"weight is {weight},height is {height}.BMI is {weight/(height)**2}")
