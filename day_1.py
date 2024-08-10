# print something in python 
print("Hello Word!")     
print("I am saroj Dhakal", "I am from nepal!")
print(34+43)

# variable in python
name = "saroj dhakal"
age = 20
height = 5.009
fine = False
wife = None

if(fine):
    print("My name is :", name,".My age and height is :",age,height)
else:
    print("there is no name")

# Data type in python 
# int,str,float,bool,NoneType
print(type(name))
print(type(age))
print(type(height))
print(type(fine))
print(type(wife))

# print sum
a= 2
b=4 
c = a+b
print("sum :" , c)

# arithmetic operator

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)  #a^b  power operator

# relational operator

print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
# ....

# assugnment operator

num = 10
print("num :", num)
num = num + 20
print("num :", num)
num +-20
print("num :", num)

num %=2
# .......

# logical operator  
# not and or 
print(not False)
print(not 4==4)
print(4==4)

print(True and False)
print(True or False)


# type conversion 

result = age + height
print(type(result) ,  result)

newresult = int(result)
print(type(newresult) ,  newresult)

# take input from user in python 

# input("Printing string (question )")

name = input('What is your name ?')
age = int (input('What is your age ?'))
gender = input('What is your gender ?')

if(gender == "male"):
    print("i know you have short hair")
else:
    print("i know you have long hair")


