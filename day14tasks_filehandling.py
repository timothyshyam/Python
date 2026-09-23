# MODE = 'r'
#reads the data from an exisiting file..and print the content from the existing file.
#print operation can only be performed in 'r' and 'r+' modes only...

file = open("C:\\Users\\sravy\\OneDrive\\Desktop\\New Text Document.txt",mode = 'r')
print(file.read())
file.close()

#method = readline()
#reads only the 1st line from the existing file.and prints it
file = open("C:\\Users\\sravy\\OneDrive\\Desktop\\New Text Document.txt",mode = 'r')
print(file.readline())
file.close()

#prints the each line of the existing file into list of substrings..
file = open("C:\\Users\\sravy\\OneDrive\\Desktop\\New Text Document.txt",mode = 'r')
print(file.readlines())
file.close()

#MODE = 'r+'
#same as 'r' mode ...but here we can perform write() as well.
file = open("C:\\Users\\sravy\\OneDrive\\Desktop\\New Text Document.txt",mode = 'r+')
file.write("shyam \npython life \n1234")
file.seek(0)
print(file.read())
file.close()

###################################################################################################################################################################################
#MODE = 'a'
#appends the data to the existing at the last..without any actual data loss(truncate)
#in this method we can also create new files.
#to perfrom append method we use write()
#this method cant be printed.

file = open("demo.txt",mode = 'a')
file.write("shyam123")
file.close()

#MODE = 'a+'
#same as 'a' mode ...but in this mode we can read data and print it.

file = open("demo.txt",mode = 'a+')
file.write("\nshyam123")
print(file.tell())                     #---------- here tell() prints the last index value of the file.
file.seek(0)                           #-----------here seek(arg = index value)   takes pointer to the index value given.from there it reads and prints out the data....as we already perfromed an write operation,the pointer stays at last.so we use this function to overcome .
print(file.read())
file.close()

########################################################################################################################################################################################
#MODE = 'w'
#writes the data given in the method write(data) and truncates all the previously existed data and returns only the given new data.
#in this mode we can also create new files while open().
 
file = open("demo.txt",mode = 'w')
file.write("shyam123")
file.close()

#method = writelines()
#this method takes list of strings as arguments and print it to an new or existing file.(no numbers can be taken if needed mention them in the strings) 
list_of_strings = ["shyam\n","python life\n","12"]
file = open("demo.txt",mode = 'w')
file.writelines(list_of_strings)
file.close()

#MODE = 'w+'
#same as 'w' mode but here we can also read data and print it. (ensure to use seek() to set the pointer after write operation)
 
file = open("demo.txt",mode = 'w+')
file.write("shyam123")
file.seek(0)
print(file.read())
file.close()