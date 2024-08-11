# String and conditional statements

# string
str = "This is my day 2 of learning python!."
str1 = 'i am happy'
str2 = """This is my dance"""
print(str)
str3 = "i am Saroj Dhakal.\n I am from Nepal "
print(str3)

# string concatenation
str4 = str + str1
print(str4)

# String length 
lengthofString = len(str4)

# string indexing
print(str[0])
print(str[1])
print(str[2])
print(str[3])
# str[0]= 2    not allowed

# slicing in string : Accessing parts of a string 
# str[starting index :ending index]
str5 = str[1:5]
print(str5)  #his
print(str[6:]) #  missing place take the length of string
print(str[:5]) # missing place take the 0 by defut

print(str[-3:-1])  # output : n!  " in python the negative indexing is indexed by backward"

# string functions

str6 = "i am student of amrit campus."

print(str6.endswith("campus."))   #returns true if string ends with substring
print(str6.capitalize())   #caputalizes 1st char
print(str6.replace("student","teacher"))   #replace all occurrences of 1st substring with 2nd substring
print(str6.find("am"))   #retun 1st index of 1st occurrence
print(str6.count('a'))   #count the occurrence of substring in string


#let's practice
"""
1. WAP to input user's first name and print its length .
"""
userName = input("Enter your name :")
print("Your name is ",userName," and your name length is ",len(userName))
"""
2. WAP to find the occurrence of "$" in a string.
"""
aString = "Wow! i am happy,he had $100 and he gives me $20"
print("Occurrence of '$' in string :" , aString.count('$'))


# conditional statements

# indentation : in python tab     other language { }

"""
if(condition):
    statement1
elif(condition):
    statement2
else
    statementN
"""
# for driving
age=10
if(age>16):
    print("you can apply for driving")
else:
    print("you cant apply for driving")

# for traffic light
light = "green" 
if(light == "green" ):
    print("you can Go")
elif(light == "Yellow" ):
    print("look and go ")
elif(light == "red" ):
    print("Stop!")
else:
    print("Error in light")


"""
mark >= 90.grade = "A"
90>marks>=80, grade = "B"
80 > marks >= 70, grade = "C"
70 > marks, grade = "D"
"""
marks = int(input("Enter your marks: "))
if(marks >=90):
    print("your grade is 'A'")
elif(90 > marks >=80):
    print("your grade is 'B'")
elif(80>marks>=70):
    print("your grade is 'C'")
else:
    print("your grade is 'D'")


# nesting
"""
if(condition):
    if(condition):
        if(condition):

        else:
    else:
else:

"""
if(age>=18):
    if(age>=80):
        print("You cannot drive")
    else:
        print("you can drive")
else:
    print("Cannot drive")

# lets practice

"""
1. WAP to check if a number entered by the user is odd or even.
"""
number = int(input("Enter a number :"))
if(number%2 ==0):
    print("Your number is Even!")
else:
    print("Your number is odd!")

"""
2.WAP to find greatest of 3 numbers entered by the user.
"""
number1 = int(input("Enter a number1 :"))
number2= int(input("Enter a number2 :"))
number3 = int(input("Enter a number3 :"))

if(number1 >number2):
    if(number1>number3):
        print("the greatest number is " , number1)
    else:
        print("the greatest number is ", number3)
else:
    if(number2>number3):
        print("the greatest number is " , number2)
    else:
        print("the greatest number is ", number3)


"""
3. WAP to check if a number is a multiple of 7 or not.
""" 
num = int(input("Enter a number: "))
if(num%7==0):
    print("tHE NUMBER is a multiple of 7")
else:
    print("the number is not multiple of 7")
