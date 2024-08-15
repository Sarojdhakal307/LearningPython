# Function and Recursion
"""
Block of statement that perform a specific task.
solve the problem of redundant
def function_name(param1,param2,...):
    statement
    return value
"""
def get_values():
    num1 = 2
    num2 = 2
    return [num1,num2]

def sum(num):
    return  num[0]+num[1]

print('values is : ',get_values())
print('Sum is : ',sum(get_values()))

# defult values in function  

def product(num1=0,num2=0):  # is defult value of the params num1 and num2 
    return num1*num2

print("Product is : ",product(5,4))
print("Product is : ",product())      # defult value is used during this condition



# Lets practice 
"""
1. WAF to print the length of a list.(list is the parameter).
2. WAF to print the elements of a list in a single line.(list is the parameter).
3. WAF to find the factorial of n. (n is the parameter).
4. WAF to convert mins to hrs
"""

# 1.
_list = [1,2,3,4,5,6,7,8]
def lenList(_list_):
    return len(_list_)

print("Length of the list is :" , lenList(_list))

# 2.
_list = [1,2,3,4,5,6,7,8]
def _printList(_list_):
    print("list is :",_list_,"\nlist is : " ,end='')
    for item in _list_:
        print(item,"",sep=",",end='')

_printList(_list)

# 3.
def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)   #Recursion : nest topic

print(fact(5))

# 4.

def _timeConverter(_min_):
    _minRem= _min_%60
    _hrs = int(_min_/60)
    return {
        "mins": _minRem,            
        "hrs": _hrs
    }
time = _timeConverter(150)
print("The time is  ",time["hrs"],":",time["mins"], sep="")



# Recursion
"""When a function calls itself repeatedly"""

def show(n):
    if(n==0):
        return
    show(n-1)
    print(n,end='')
show(5)

# Factorial function
def fact(n):
    if(n==1 or 0):
        return 1
    return n*fact(n-1)   

print("\nFactorial is :",fact(5))

# Lets practice
"""
1. Write a recursive function to calculate the sum of first n natural numbers.
2. Write a recursive function to print all elements in a list.
"""
# 1.
def _sumNumber(_num):
    if(_num==0):
        return 0
    return _num+_sumNumber(_num-1)

print("sum of natural number :",_sumNumber(10))

# 2.
_list = [1,2,3,4,5,6,7,8]
def _printList(_list_,indx =0):
    if(indx == len(_list_)):
        return
    print(_list_[indx] ,end=',')
    _printList(_list_,indx+1)

_printList(_list)