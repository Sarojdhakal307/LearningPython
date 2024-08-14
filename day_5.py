#Loops in python 
"""
Loops are used to repeat instructions.

"""
i=1

#While loop
"""Print numbers from 1 to 100."""
while(i<=100):                 
    print( i)
    i+=1
print("i is :",i)

"""Print numbers from 1000 to 1."""
i=100
while(i>=1):
    print(i)
    i-=1

"""Print the multiplication table of a number n."""

# n = int(input("Enter a number: "))
# i = 1
# while(i<=10):
#     print(n*i)
#     i +=1

"""Print the elements of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]"""
count = 0
terms = 1
lists=[]
while(count<10):
    lists.append(terms)
    print(terms)
    terms = terms+(3+count*2)
    count+=1
print(lists)

"""search for a number X in this tuple using loop"""
num1 = int(input("Enter number : "))
get = False
count=-1
while(not get and count <len(lists)-1):
    count+=1
    if(lists[count] ==num1):
        get =True
    

if(get==True):
    print(num1," is at index : ",count)
else:
    print(num1," is not in lists.")

#break and Continue
"""
Break : Used to teminate the loop when encountered
Continue: Terminates execution in the ocurrent interation and continues execution of the loop with the next  interation.
"""
i=0
while(i<=10):
    if(i==7):
        print("iu am here")
        break
    print("nice")
    i+=1


#continue
i=0
while(i<=10):
    i+=1
    if(i==7):
        print("i am here")
        continue
    print("nice")
    
# for loops
"""
for loops are used for sequwntial traversal . For traversing list, string, tuples etc.
"""

list2= [12,13,14,15,16,17,18]
tup1= (132,143,134,125,116,147,158)
str = "Saroj Dhakal"
for val in list2:
    print(val)

for val in tup1:
    print(val)

for val in str:
    print(val)

#for loon with else  : else runs after the endings of loop 

for val in str:
    print(val)
else:
    print("String Operating complete")



"""
Print the elemeents of the following list usinga loop:
"""
list1 = [1,4,9,16,25,36,49,64,81,100]
for val in list1:
    print(val)

"""Search for a number X in this tuple using loop """
x=25
flag = False
for val in list1:
    if(x==val):
        print(val,"found")
        break
else:
        print("not found")



#range()
"""
Range functions returns sequence of numbers, starting  from 0 by default, and increments by 1 by default , and stops before a specified number.
"""
#range(start?,stop,step?)

print(range(5))

seq = range(5) #range(stop)
for val in seq:
    print(val)


seq = range(2,5) #range(start,stop)
for val in seq:
    print(val)

seq = range(2,25,10) #range(start,stop,step_size)
for val in seq:
    print(val)


for i in range(0,10,2):
    print(i) # printing the even number in between o and 10 


"""
using for and range()

print numbers from 1 to 100
print numbers from 100 to 1
print the multiplication table of a number n 
"""
for val in range(1,101):
    print(val)

for val in range(100,0,-1):
    print(val)

n=5
for val in range(1,11):
    print(val*n)


# Pass Statement 
"""
Pass is null statement that does nothing. It is used as a placeholder for future code.used in exception an try Catch
"""
for j in range(5):
    pass


"""
WAP to find the sum of first n numbers. using While
WAP to find the factorial of first n numbers. using for
"""
n = 10
i=1
sum=0
fac=1
while(i<=n):
    sum = sum+i
    i+=1
print("sum is : ",sum)

for i in range(1,n):
    fac=fac*i

print("fac is :" ,fac)