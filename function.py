#Add Function
#Write a Python function named add that takes two arguments a and b and returns their sum.
def add(a,b):
    return a+b
obj = add(1,2)
print(obj)
#===================================================================================================================================================
#Square Function
#Write a Python function named square that takes a number x as input and returns its square
"""num=int(input("enter a number to find it's square:"))
def square(x):
    global num
    return num**2
obj = square(num)
print(obj)"""
#===============================================================================================================================================
#Factorial Function
#Write a Python function named factorial that takes a positive integer n as input and returns its factorial
"""n = int(input("enter a number to find it's factorial:"))
import math
def factorial(n):
    if n<0:
        print("enter an positive integer.")
    else:
        return math.factorial(n)
obj = factorial(n)
print(obj)"""
#===============================================================================================================================================
#Maximum Function
#Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list.
"""def maximum(n):
    return max(list_n)
n = (input("enter the numbers separated by spaces:"))
list_n = [int(i) for i in n.split()]
print(f"list of input numbers:{list_n}")
max = maximum(list_n)
print(max)
"""
#===============================================================================================================================================
#Reverse Function
#Write a Python function named reverse that takes a string s as input and returns its reverse.
"""s=input("enter the string:")
def reverse(s):
    return s[::-1]         #using indexing to reverse the string.
revesed_string = reverse(s)
print("reversed string:",revesed_string)"""
#===============================================================================================================================================
#Check Prime Function
#Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False
"""n =int(input("enter a number to find it's prime:"))
def is_prime(n):
    if n<=1:                                      #0 and 1 are not a prime number.
        return False
    for i in range(2,int(n**0.5)+1):             #to check square root of n ...n**0.5   logic= no.divided by square root(**0.5) of no.
        if n%i==0:
            return False
    return True
prime_bool = is_prime(n)
print(prime_bool)"""
#===============================================================================================================================================
#Fibonacci Function
#Write a Python function named fibonacci that takes a positive integer n as input and returns the n th Fibonacci number
"""from sympy import fibonacci as sympy_fibonacci  #installed an module sympy by pip install sympy in terminal...to return fibonacci no.easier
n =int(input("enter a positive integer:"))
def fibonacci(n):
    return sympy_fibonacci(n)                        
nth_fibonacci =fibonacci(n)
print("nth fibonacci number:",nth_fibonacci)"""
#===============================================================================================================================================
#Palindrome Function
#Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False
"""s= input("enter the string:")
def is_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
check_palindrome= is_palindrome(s)
print(check_palindrome)"""
#===============================================================================================================================================
#Sum of Squares Function
#Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those number
"""n=input("enter numbers separted by spaces:")
list_n = [int(i) for i in n.split()]                  # to get all the inputs in the list.
def sum_of_squares(list_n):
    sum =0
    for i in list_n:
        sum+=i
    return sum**2
print("entered inputs as list:",list_n)
sum_squares = sum_of_squares(list_n)
print("sum of squares of these numbers:",sum_squares)"""
#===============================================================================================================================================
#Average Function
#Write a Python function named average that takes a list of numbers as input and returns the average value.
n=input("enter numbers separted by spaces:")
list_n = [int(i) for i in n.split()]
def average(n):
    return sum(list_n)/len(list_n)
avg=average(list_n)
print("entered inputs in a list:",list_n)
print("average value :",avg)