# Dictionary in python 
"""
Dictionaries are used to store data values in key:value pairs.
They are unordered, mutable(changeable) & don't allow duplicate keys

dict = {
    "key" : value   
}
Can access the values of dictionary by  dict["key"]
"""
dict1 = {
    "name" : "Saroj",
    "age" : 20,
    "sem" : "4th",
    "marks" : 93.88,
    "is_adult" : True,
    "list" : ["python" , "C" , "C++", "javascript"],
}
print(dict1)
print(type(dict1))
print(dict1["age"])
print(dict1["list"])
print(dict1["marks"])

dict1["marks"] = 98  #mutable
print(dict1["marks"])

#can create the null dictionary
null_dict = {}
print(null_dict)
null_dict["name"] = "ram"
print(null_dict)

# nested dictionary
teacher = {
    "name" : "Ram Babu gyawali",
    "subjects":{
        "DSA" : "5hr",
        "CN"  : "4hr"
    }
}
# accessing nested Dictionary
print(teacher)
print(teacher["subjects"])
print(teacher["subjects"]["DSA"])

print("\n")
#Dictionary Methods

dict2 = dict1
# print(dict2)

print(dict2.keys())     # ['key','key']
print(dict2.values())    # ['value','value']
print(dict2.items())     # [('key',value),('key',value)]
print(dict2.get("list"))
print(dict2.update({"newcity": "kathmandu"}))
print(dict2)  #{'name': 'Saroj', 'age': 20, 'sem': '4th', 'marks': 98, 'is_adult': True, 'list': ['python', 'C', 'C++', 'javascript'], 'newcity': 'kathmandu'}

#length of Dictionary
print(len(dict2))

# typecasting from dictionary to list
print(list(dict2.keys()))




# Set in Python
"""
Set is the collection of the unordered items.
Each element in the set must be unique & immutable.
we cant store the list in set
"""

nums = {1,2,3,4,5,6,7,8,9}
sets = {1,2,3,2,2,3}   #ignore the double value like : 2 and 3
print(sets)            #{1, 2, 3}

print(nums)
print(sets)
print(type(sets))       #set
print(len(nums))
print(len(sets))

null_dict = {}    # it is empty dictionary
null_set = set()


# Set Method

nums.add(10)            #Adds an element
nums.remove(1)            #removes the element 
sets.clear()            #empties the set 
print(nums.pop() )           #removes a random value
print(sets)

# nums.add([1,2,3,4])   #Error : unshshable type: dictionary list [immutable]

sets.add(299)
print(sets.union(nums))
print(sets)

sets.add(5)
print(sets.intersection(nums))


# practice 

"""
1.Store following word meanings in a python dictionary
table:"a piece of furniture", "List of facts and figures"
cat: "a small animal"
"""
py_dict = {
    "table" : ["a piece of furniture", "List of facts and figures"],
    "cat": "a small animal"
}
print(py_dict)

"""
2.You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all studenyts.
"""
subject = {"python", "java","c++", "python","Javascript","java","python","java","c++","C"}
print("Number of classroom needed by all students is :", len(subject))


"""
3.WAp to enter marks of 3 subjects from the user and store them in a dictionary . Start with an empty dictionary and add one by one. Use subject name as key and marks as value.
"""

marks = {}
marks.update({"DSA" : int(input("Enter the marks of 1st subject: "))})
marks.update({"AI":int(input("Enter the marks of 2nd subject: "))})
marks.update({"CN":int(input("Enter the marks of 3rd subject: "))})
print(marks)


"""
4.Figure out a way to store 9 and 9.0 as separate values in the set .(you can take help of built-in data types)
"""

_set= {
    ("float",9.0),("int",9)
}
__set = {
    9,"9.0"
}
print(_set)
print(__set)