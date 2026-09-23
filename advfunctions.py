#Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing 
# the square of each number in the input list.Use the map() function with a lambda function to implement this.
"""def square_all(numbers):
    return map(lambda i:i**2,numbers)
input = (input("enter numbers separated by spaces:")) 
list_n = [int(i) for i in input.split()]
print("entered inputs in a list:",list_n)
print("squares of the input list:",list(square_all(list_n)))"""

#==============================================================================================================================================
#Write a Python function filter_positive(numbers) that takes a list of numbers as input and returns a new list 
# containing only the positive numbers from the input list. Use the filter() function with a lambda function to implement this.
"""def filter_positive(numbers):
    return filter(lambda i:i>=0,numbers)
input = (input("enter numbers separated by spaces:"))
list_n = list(map(float,input.split()))
print("entered inputs in a list:",list_n)
print("positive numbers from input list:",list(filter_positive(list_n))) """
#==============================================================================================================================================
#Write a Python function calculate_factorial(n) that calculates the factorial of a given number n .
#  Use the reduce() function with an appropriate lambda function to implement this.
"""from functools import reduce

def calculate_factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
    return 1 if n == 0 else reduce(lambda x, y: x * y, range(1,n+1))            #range from 1 to entered no.  logic for factorial
input = int(input("enter a number to find factorial:"))
print(calculate_factorial(input))"""
#==============================================================================================================================================
#Write a Python function count_vowels(string) that takes a string as input and returns the count of vowels (a, e, i, o, u) 
# in the input string. Use the reduce() function with an appropriate lambda function to implement this.

#unable to find in reduce .. iwill solve this another method.
empty_list = []
input = input("enter the string:")
vowels = ["a","e","i","o","u"]
for i in input:
    if i in vowels:
        empty_list.append(i)
print("count of vowels from the string:",len(empty_list))