#You are given a string sentence . Print the characters at even indices.
sentence = "Python is amazing"
print(sentence[::2])

################################################################################################################################
#You are given a string s . Replace all spaces in the string with underscores ( _ ) and print the modified string.
#Example:
s = "Python is fun and powerful"
print(s.replace(" ","_"))

################################################################################################################################
#You are given a string s . Check if the string contains only digits.
#Example:
s = "12345"
print(s.isdigit())

################################################################################################################################
#You are given a string s . Print the string in reverse order.
#Example:
s = "Python is amazing"
print(s[::-1])

################################################################################################################################
#You are given a string s . Capitalize the first letter of each word in the string and print the modified string.
#Example:
s = "python programming is fun"
modified_string =s.title()
print("Modified string =",modified_string)