#==========================================RUN-TIME ERRORS==============================================
#Exception, is an common base class for finding the error for all the types of errors.
try:
    x= 1
    print(x.append(2))
except Exception as e:
    print("Exception:",e)

#ZeroDivisionError
#(raised when a no.is divided by zero 0)
try:
    a=1
    b=0
    print(a/b)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)


#ValueError
#raised when a function receives an correct type of argument but an inappropriate value
try:
    input_1 =int(input("enter num_1:"))
    input_2 =int(input("enter num_2:"))
    print(input_1+input_2)
except ValueError as e:
    print("ValueError:",e)

#TypeError
#raised when an operation applied to an inappropriate type
try:
    print(int("5"+10))
except TypeError as e:
    print("TypeError:",e)

#IndexError
#raised when index no. entered is out of range from the given type.
try:
    list = [1,2,3,4,5]
    print(list[5])
except IndexError as e:
    print("IndexError:",e)

#KeyError
#raised when an dictionary key is not found
try:
    dict = {"name": "shyam"}
    print(dict["age"])
except KeyError as e:
    print("KeyError:",e)

#AttributeError
#raised when an inappropriate attribute reference is made.
try:
    x= 10
    x.append(5)
except AttributeError as e:
    print("AttributeError:",e)

#ImportError
#raised when we try to import an non existing module in our cwd(current working directory)
try:
    import gtts
except ImportError as e:
    print("ImportError:",e)

#FileNotFoundError
#raised when we try to open an file which doesn't exists
try:
    open("missing_file.txt",mode = 'r')
except FileNotFoundError as e:
    print("FileNotFoundError:",e)

