#Reverse List:
#Write Python code to reverse the order of elements in the given list my_list .Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]
print(my_list[::-1])     #step value -1 is used to reverse the elemnents.

#################################################################################################################################################

#Common Elements:
#Given two lists list1 and list2 , find and print the common elements between them.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [x for x in list1 if x in list2]
print(common_elements)

###################################################################################################################################################

#Unique Elements:
#Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
set_list = set(original_list)
unique_list = list(set_list)
print(f"original_list = {original_list}")
print(f"unique_list = {unique_list}")

###################################################################################################################################################

#Remove Duplicates:
#remove duplicate elements from the given list duplicated_list and print the list without duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
empty_list = []
[empty_list.append(i) for i in duplicated_list if i not in empty_list]
print(empty_list)

##########################################################################################################################################################

#List Concatenation
#Write a Python script that concatenates two lists and prints the result.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Concatenated list:", combined_list)

################################################################################################################################################

#List Repetition
#Write a Python script that repeats a list three times and prints the result.
list_1 = [1,2,3]
print(f"3 times repeated list = {list_1*3}")

#################################################################################################################################################

#List Removal
#Write a Python script that removes the elements at even indices from a list.

original_list = [10, 20, 30, 40, 50, 60, 70]
result_list = [original_list[i] for i in range(len(original_list)) if i % 2 != 0]       # len() function returns all the indices...i%2!=0 removes the even indices and stores the indices values in i.. prints the odd indices by original_list[i]

print("List after removing elements at even indices:", result_list)

#####################################################################################################################################################

#List Insertion
#Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list.

list_new = [1,2,3]
list_new.insert(0,10)
list_new.insert(1,11)
list_new.insert(2,12)
print(list_new)

#######################################################################################################################################################

#List comprehensions
#1. Square Numbers: Create a list of squares of numbers from 1 to 10.
#2. Even Numbers: Generate a list of even numbers from 1 to 20.
#3. Words Lengths: Given a list of words, create a list containing the lengths of each word.
words = ["apple", "banana", "cherry", "date"]


print("1.list of squares of numbers from 1 to 10:",[i*i for i in range(11)])

print("2.list of even numbers from 1 to 20:",[i for i in range(21) if i%2==0])

print("3.Lengths of each word:",[len(i) for i in words])