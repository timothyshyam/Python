#Problem 1: Using break in a for Loop
#Write a Python program that takes a list of numbers as input numbers = [25, 30,20, 40, 15, 25] and 
# prints the sum of the numbers. However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100".
"""
sum=0
input_num = [25, 30,20, 40, 15, 25]
for i in input_num:
    sum+=i
    if sum>100:
        print("sum exceeded 100")
        break
print(f"sum of numbers,{sum}")
"""
#Problem 2: Using continue in a For Loop
#Write a Python script that uses a for loop to iterate through numbers from 1 to 600.
#  Print only the odd numbers, skipping the even ones using the continue statement.
"""
for i in range(1,600):
    if i%2 == 0:
        continue
    print(i)
"""
#Problem 3: Using pass in Conditional Statements
#Write a Python script that checks if a number is even or odd. If the number is even, print "Even"; 
#if odd, do nothing (use the pass statement).
"""
input_num = int(input("enter number:"))
if input_num%2==0:
    print("even")
else:
    pass
"""
#Problem 4: Combining Transfer Statements
#Write a Python script that iterates through a list of words. If the word is "break,"
#exit the loop using the break statement. If the word is "skip," skip the rest of the
#code for the current iteration using the continue statement. For any other word,print the word.

words=["place","name","break","skip","animal"]
for i in words:
    if i=="break":
        break
    elif i=="skip":
        continue
    else:
        print(i)