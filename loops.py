#SUM OF SQUARES.
#1.write a python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop.

sum = 0
for i in range(1,6):
    result= i*i
    sum+=result
    print(f"square of {i} is {result}")
print(f"sum of the squares of numbers from 1 to 5 is {sum}")

########################################################################################################################
#COUNTDOWN.
#2.write a python program that uses a while loop to print a countdown from 5 to 1.
"""
count =5
while count>=1:
    print(count)
    count-=1
    """
############################################################################################################################
#MULTIPLICATION TABLE WITH NESTED FOR LOOP.
#3.write a python program to the multiplication table for a user specified number using a nested for loop.
"""
num = int(input("enter the number to display its multiplicatin table:"))
for i in range(1,11):                        #from 1 to 10  of multiplication with a given user input
     for j in range(1,2):                    #one iteration per line
        print(f"{num} X {i} = {num*i}")
        """
##########################################################################################################################
#4.WRITE A PYTHON PROGRAM THAT USES "for loop" TO FIND THE SUM OF ALL EVEN NUMBERS BETWEEN 0 AND 10(INCLUSIVE).
"""
sum = 0
for i in range(0,11):
    if i%2==0:                  #if conditon is used to identify even numbers.
         sum+=i
print(f"sum of all even numbers between 0 and 10 is {sum}")
"""
############################################################################################################################
#5. CALCULATE THE SUM OF ALL NUMBERS FROM 1 TO A GIVEN NUMBER.
"""
num = int(input("enter the number:"))
for i in range(1,num):
    num+=i
print(f"sum of all numbers {num}")
"""
###########################################################################################################################
#6.DISPLAY NUMBERS FROM A LIST USING LOOP.
"""
num =[1,2,3,4]
for i in num:
    print(i)
"""
##########################################################################################################################
#7.DISPLAY NUMBERS FROM -10 TO -1 USING "for loop".
"""
for i in range(-10,0):
    print(i)
"""
#########################################################################################################################
#8.write a python program to print the cube of all numbers 1 to a given number
"""
num = int(input("enter the number:"))
for i in range(1,num+1):
    result=i**3
    print(f"number {i},cube is {result}")
"""