#Dictionary Update
#Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25}
my_dict['city']= 'west godavari'
print(my_dict)

###################################################################################################################################
#Dictionary Access
#Write Python code to access and print the value associated with the key 'price' in the following dictionary:
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info.get)

###############################################################################################################################
#Dictionary Removal
#Write Python code to remove the key-value pair with the key 'city' from the following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop('city')
print(my_dict)

###############################################################################################################################
#Dictionary Keys
#Write Python code to print all the keys present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())

###############################################################################################################################
#Dictionary Values
#Write Python code to print all the values present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())

###############################################################################################################################
#Dictionary Update
#Write a Python script that updates a dictionary with a new key-value pair.
my_dict = {'name': 'python', 'age': 25}
my_dict.update({'gender':'male'})
print(my_dict)

###############################################################################################################################
#Dictionary Access
#Write a Python script that accesses and prints the value associated with a specific key in a dictionary.
my_dict = {'name': 'python', 'age': 25}
print(my_dict.get('age'))

###############################################################################################################################
#Dictionary Removal
#Write a Python script that removes a key-value pair from a dictionary.
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict)
my_dict.pop('age')
print(f"after removing a key-value pair :{my_dict}")
