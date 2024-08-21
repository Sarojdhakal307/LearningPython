# # OOPs part 2

# # del keyword : Used to delete object properties or object itsef
# class student:
#     name = 'Shiva'
#     __balance = 0
#     def print_balance(self):
#         print("balance is ",self.__balance)
#     def __add_balance(self,balance):
#         self.__balance += balance
#         self.print_balance()
#     def update_balance(self):
#         self.__add_balance(int(input("Enter the balance to add in account: ")))

# _s = student()
# _s1 = student()
# print(_s.name)
# del _s
# # print(_s.name)     #NameError: name '_s' is not defined


# # Private(like) attributes and methods that
# """
# Conceptual implementations in python
# Private attributes and methods are meant to be used only within the class and are not accessble from outside the class.
# By giving the 2 underscore(__) infront of name(attributes): __balance
# """
# # print(_s1.__balance)  #give error because __balance is private attributes cant acces outside of the class

# _s1.print_balance()
# _s1.update_balance()



# Inheritance : When one class(child/derived) derives the properties and methods of another class(parent/base)

class father:       #parents class
    have_car= True
class son(father):      # Child class
    pass


# Types of inherutance
"""
1.  Singel inheritance  : Car toyota
2.  Multi-level inheritance      :Car fortuner
3.  Multiple inheritance           :wowcar car and cycle
"""

class cycle:
    cycle = True
class bike:
    bike = True
class Car:                          #Base class
    car = True
    color = "black"
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car is started !")
    @staticmethod
    def stop():
        print("car is stoped !")
    
class Toyota(Car):                          #Derived_1 class
    toyota = True
    def __init__(self,name):
        self.name = name
        
class fortuner(Toyota):                          #Derived_2 class
    fortuner = True
    def __init__(self,brand):
        self.brand = brand

class wowCar(cycle,bike):
    wowcar = True


car1 = Toyota("bishnu")
car2 = fortuner("nischal")
car3 = wowCar()


car1.start()
car2.start()
# car3.start()

print(car1.color)
print(car2.color)
print(car3.bike,car3.cycle)



#Super method : super() method is used to access methods of the parent class.
class A:
    def __init__(self,cast):
        self.cast = cast
    a = True
class B(A):
    def __init__(self,name,cast):
        self.name = name
        super().__init__(cast)
    a = True

obj1 = B("bijay","B.K")
print(obj1.name,obj1.cast)


# class method :
"""
A class method is bound to the class andrecerves the class as an implicit first argument.
Note- static method can't acess or modify class state and generally for utility.

"""
class person:
    name = "anonymous"
    address= "kathmandu"
    age =15
    def changeName(self,name):
        self.name = name
    def changeaddress(self,address):        # instance method
        # person.address = address          Or
        self.__class__.address = address 
    @classmethod                            #  @classmethod decoretor
    def change_age(cls,age):
        cls.age  =age
p1 = person()
print(p1.name)
print(p1.address)
print(p1.age)
p1.changeName("suraj")
p1.changeaddress("pokhara")
p1.change_age(70)
print(p1.name)
print(p1.address)
print(p1.age)
print(person.name)
print(person.address)
print(person.age)



#@property :
class student:
    def __init__(self,phy,chem,math):
        self.phy =phy
        self.chem =chem
        self.math =math
        # self.percentage = str((phy+chem+math)/3) +"%"

    # def calculatepercentage(self):
    #     self.percentage = str((self.phy+self.chem+self.math)/3) +"%"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) +"%"

s1= student(25,30,45)
print(s1.percentage)

s1.phy = 95
print(s1.phy)
print(s1.percentage)

#@getter @setter

#Polymorphism : operator overloading
"""
when the same operator is allowed to have different meaning according to the context.

Operators and Dunder functions
a+b a.__add__(b)
a-b a.__sub__(b)
a*b a.__mul__(b)
a/b a.__truediv__(b)
a%b a.__mod__(b)
"""
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"+ ",self.img,"i")
    def add(self,num2):
        newReal = self.real +num2.real
        newImg = self.img + num2.img
        return complex(newReal,newImg)
    def __add__(self,num2):                     #dunder function
        newReal = self.real +num2.real
        newImg = self.img + num2.img
        return complex(newReal,newImg)
    def __sub__(self,num2):
        newReal = self.real -num2.real
        newImg = self.img - num2.img
        return complex(newReal,newImg)
num = complex(5,6)
num1 = complex(7,14)
numm3 = num.add(num1)

print(num.showNumber())
print(num1.showNumber())

# num2 = num.add(num1)
num2 = num+num1
num3 = num-num1
num2.showNumber()
num3.showNumber()

#lets practice
"""
Qs. Define a circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a perimeter method of the class which allows you to calculate the perimeter of the circle.
"""
class circle:
    def __init__(self,radius):
        self.radius = radius
    def Area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 3.14*self.radius

c = circle(5)
print("area : " ,c.Area())
print("perimeter : ", c.perimeter())

"""
Qs2. Define a Employee class with attributes role, department and salary.This class also has a showDetails() method.
Create an Engineer class that inherits properties from Employee and has additional attributes: name and age.
"""
class Employee():
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showDetails(self):
        print("\nrole :",self.role)
        print("department :",self.department)
        print("salary :",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,role,department,salary):
        super().__init__(role,department,salary)
        self.name = name
        self.age = age

# e1 = Employee("admin","finance", 98888)
# e1.showDetails()

e1 = Engineer("ramesh" ,18,"admin","finance", 98888)
e1.showDetails()


"""
Qs3. Create a class called Order which stores item and its price.
    Use Dunder dunction __gt__() to convey that:
        order1 > order2 if price of order1 > price of order

"""
class Order():
    def __init__(self,item, price):
        self.item= item
        self.price= price
    def __gt__(self,order):
        return self.price > order2.price
    
order1 = Order("pen",10)
order2 = Order("copy",20)

print(order1>order2)
