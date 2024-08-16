# File i/o
"""
Python can be used to perform operations on a file .(read anf write data)
Types of all files:
1. Text Files: .txt,.docx,.log etc.
2. Binary Files: .mp4, .mov, .png, .jpeg etc.


Open Read and Close Files:
    We have to open a file before reading or writing

    f = open("File_name","mode")
    mode: read , write...etc
Mode:
r : Opean for reading
w : Open for writing,truncating the file first   
a : Open for writing , appenfing to the end of the file if it exits 
x : create a new file and open it for writing
b : binary mode 
t : text mode
+ : open a disk file for updating (reading and writing)

"""

# Read file
"""
f = open("files\demo.txt","r")
data = f.read(numOfChar)
data = f.readline()     # read one line at a time

"""
f = open("files\demo_r.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()
f = open("files\demo_r.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

# Writing to a file
"""
f = open("files\demo_w.txt","w")
data = f.write(" lines ")
"""
f = open("files\demo_w.txt","w")
f.write("Hey nepal is a beautiful country.") 
f.close()

# Append to a file
"""
f = open("files\demo_a.txt","a")
data = f.write(" lines ")
"""
f = open("files\demo_a.txt","a")
f.write("Hey,I am append file. \n") 
f.close()

#r+ mode  "not truncating Pointer is at start"
f = open("files\demo_r+.txt","r+")
# f.write("Hey,I am  file. \n") 
print(f.read())
f.close()

#w+ mode    "truncating Pointer is at start""
f = open("files\demo_r+.txt","w+")
f.write("Hey,I am  file. \n") 
# print(f.read())
f.close()

#a+ mode    "not truncating Pointer is at end""
f = open("files\demo_r+.txt","a+")
f.write("Hey,I am  file. \n") 
# print(f.read())
f.close()


"""
with syntax
with open("file_name","a") as f:
    data = f.read() 
"""
with open("files\demo_r.txt","r") as f:
    print(f.read())
    f.close()


"""
Deleting a file

using the os module
Module(like a code library) is a file written by another programmer that generally has a functions we can use.

    import os
    os.remove(filePath)

"""
import os
# os.remove("files\sample.txt")

#Lets practice:
"""
1. Create a new file "Practice.txt" using python. Add the following data in it :
Hi everyone
We are learning File I/O
using Java:
I like programming in Java.
2.Replace all java in the file by the python.
3. Search it the word "learning exits in the file or not.
4. WAF to find in which line of the file does the word "Learning" occur first. Print -1 if word not found. 
5. From a file containing numbers separated by comma, print the  count of even numbers.
 """
# 1
with open("files\_task1.txt",'w') as f:
    f.write("Hi everyone \nWe are learning File I/O \nusing java :\nI like programming in java .")
    f.close()
# 2
with open("files\_task1.txt","r") as f:
    data = f.read()
with open("files\_task1.txt","w") as f:
    f.write(data.replace("java","python"))
# 3
if(data.find("learning") != -1):
    print("learning is available")
else:
    print("learning is not available")

# 4.
def check_line():
    word = "learning"
    data = True
    _linenum = 0
    with open("files\_task1.txt","r") as f:
        while data:
            data = f.readline()
            _linenum += 1
            if(word in data):
                print(word ," found") 
                return _linenum           
    return -1        

print(check_line())

# # 5

with open("files\_task5.txt","r") as f:
    data = f.read()
    print(data)
    num = ""
    for i in range(len(data)):
        if(data[i]==','):
            print(int(num),end=":")
            if((int(num)%2) == 0):
                print("Odd ")
            else:
                print("even ")
            num=""
        else:
            num+= data[i]


# Or
with open("files\_task5.txt","r") as f:
    data = f.read()
    print(data)
    num = ""
    data = data.replace(",","")
    data_list = data.split()
    print(data_list)

    for val in data_list:
        if((int(val))%2==0):
            print(int(val),"even",sep=":")
        else:
            print(int(val),"Odd",sep=":")
