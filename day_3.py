#List and Tuple
"""
List: A built in dta type that stores set of values.
It can store elements of different types.

"""
marks = [2.3, 4.5, 4.5, 5.6, 5, 9, "A+"]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
# print(marks[10])       X error

marks[0]= 5
print(marks)

# list slicing: list_name[starting_idx:ending_idx]   also negative indixing is possible.
print(marks[2:6])
print(marks[:5])
print(marks[2:])

# List Methods

list = [2, 1, 3]
list.append(4)     #sdds one element at the end
print(list)
list.sort()     #sorts in ascending order
print(list)
list.sort(reverse = True)     #sorts in descending order
print(list)
list.reverse()     #reverse list
print(list)
list.insert(2,5)     #insert element at index
print(list)
list.remove(2)     #removes first occurrence of element 
print(list)
list.pop(2)
print(list)


#Tuples in python 
"""
A buil-in data type that lets us create immutable sequences of velues.
"""
print("Tuples")

tup = (56, 54, 23, 25, 65)

print(tup)
print(type(tup))
print(tup[2])

# tup[0]=5  X error 


"""
1.WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
"""
favMovies= []
favMovies.append(input("Enter your favMovie_1."))
favMovies.append(input("Enter your favMovie_2."))
favMovies.append(input("Enter your favMovie_3."))

print("fav movies are : " ,favMovies)
"""
2. WAP to check if list contains a palindrome of elements.(Hint: use copy() metho)
"""
list1 = [1,2,3,2,1]
list2 = [2,3,4,1,2]

list1copy=list1.copy()
list1copy.reverse()

list2copy=list2.copy()
list2copy.reverse()

if(list1==list1copy):
    print("list1 is palindrome")
else:
    print("list1 is not palindrome")

if(list2==list2copy):
    print("list1 is palindrome")
else:
    print("list2 is not palindrome")

"""
3. WAP to count the number of students with the "A" grade in the following tuple.
"""
tuple = ("C","D","A","A","B","B","A")
print(tuple.count('A'))
_list = ["C","D","A","A","B","B","A"]
_list.sort()
print(_list)