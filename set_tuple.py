#================================= SET ===============================
# Set Intersection
#Write Python code to find and print the intersection of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1)
print(set2)
print("intersection of the following two sets:",set1.intersection(set2))

#################################################################################################################################
#Set Union
#Write Python code to find and print the union of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1)
print(set2)
print("union of the following two sets:",set1.union(set2))

################################################################################################################################
#Set Difference
#Write Python code to find and print the elements present in set1 but not in set2 :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1)
print(set2)
print("difference :",set1.difference(set2))

################################################################################################################################
#Set Symmetric Difference
#Write Python code to find and print the symmetric difference of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1)
print(set2)
print("symmetric difference of the following two sets:",set1.symmetric_difference(set2))

################################################################################################################################
#Set Membership Test
#Write Python code to check if the element 3 is present in the set my_set :
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)



#=================================== TUPLE ===================================
#Create a Tuple:
# Write a program that creates a tuple containing three elements:
# your name, your age, and your favorite color. Then print the tuple.
"""name = input("Enter your name: ")
age = int(input("Enter your age: "))
color = input("Enter your favorite color: ")
sample = (name, age, color)
print("Your information as a tuple:",sample)"""

################################################################################################################################
#Access Tuple Elements:
#  Write a program that creates a tuple containing the days of the week. Then, print the third element of the tuple.
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("The third day of the week is:", days[2])

################################################################################################################################
#Tuple Concatenation:
# Write a program that creates two tuples, one containing odd numbers from 1 to 5 and another 
#containing even numbers from 2 to 6. Concatenate these two tuples and print the result.
odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
print("concatenation :",odd_numbers+even_numbers)

################################################################################################################################
#Tuple Unpacking: 
# Write a program that defines a tuple containing the dimensions of a rectangle (length and width).
# Then, unpack this tuple into two variables and calculate the area of the rectangle.
rectangle = (10, 5)
length, width = rectangle                  # Unpack the tuple
area = length * width
print("Length:", length)
print("Width:", width)
print("Area of the rectangle:", area)

################################################################################################################################
#Check if an Element Exists:
#  Write a program that checks if a given element exists in a tuple.
sample_tuple = (10, 20, 30, 40, 50)
element = int(input("Enter an element to check: "))          #given = user input
if element in sample_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple")

################################################################################################################################
#Write a Python program to generate a bill for a supermarket purchase. The program should store the items
#and their prices in a list of tuples. It should then iterate over this list to print out each item along with its price.
# Finally,calculate and print the total cost of all the items.
items_price= [("Apple", 99.00), ("Banana", 99.00), ("Milk", 49.00)]
total=0
print("items        price")
print("-"*20)
for i,j in items_price:
    print(f"{i}        {j}")
    total+=j
print("-"*20)
print(f"Total    {total}")