
# variables are called attributes and functions are called methods.
class student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
student1 = student()
student1.name = "Saloni"
student1.marks = 87
value = student1.check_pass_fail()
print(value)

student2 = student()
student2.name = "Saroha"
student2.marks = 30
value = student2.check_pass_fail()
print(value)
# Solving a problem by creating objects is one of the most popular approaches in programming. This is called Oops.
 
# Class:- A class is blueprint for creating objects. For example:- university form.
# object :- An object is an instantiation of class. When class is defined. Memory is alloted only after object instantation.
class Number:
    def sum(self):
        return self.a + self.b
    
num = Number() # object instantiation.
num.a = 12
num.b = 34
s = num.sum()
print(s)

class StudentRecord:
    record = "StudentRecord"
    def Data(self):
        print(f"Your Name is{self.name}")
        print(f"Your interest is {self.interest}")
        
Record_data = StudentRecord()
Record_data.name = "Saloni"
Record_data.interest = "programming"
record = Record_data.Data()
print(record)

# Modelling a problem in Oops
''' We identify the following in our problem
Noun = class = Employe
Adjective = Attributes = name, age, salary
verbs = methods = getsalary(), '''
# There are two types of attributes 1. class attributes 2. instance attributes

class Employee:
    company = "Google"
    salary = 400
harry = Employee()
rajni = Employee()
harry.salary = 500 # instance attribute
print(harry.salary)
print(rajni.salary) # class attribute
# Instance attribute takes prefernce over class attribute during assignment.

# Static method :- sometimes we need a function that doesnot use the self parameter. we can define a static method like this;def greet()
#@staticmethod
#def greet():
#     print("hello user")

class Employee1:
    company = "Google"

    def getsalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n {signature}")

        @staticmethod
        def greet():
            print("Good Morning, Sir")
        @staticmethod
        def time():
            print("The time is 9AM in the morning")
harry = Employee1()
harry.salary = 1000
harry.getsalary("Thanks!")

class mynew_class:
    def newfun(self):
        print(f"The name of person is {self.name} and the salary of person is {self.salary}")
    def __init__(self, age, companyname, signature): # This is constructor method.
        print("my favourite company is Google")
        self.age = age
        self.companyname = companyname
        self.signature = signature
    def biodata(self):
        print(f"Age of person is {self.age}")
        print(f"Name of company is {self.companyname}")
        print(f"name of person is {self.signature}")

name_of_class = mynew_class(19, "Google", "Saloni")
name_of_class.biodata()
name_of_class.name = "shradha khapra"
name_of_class.salary = 1000000
name_of_class.newfun()

class Biodata:
    def bio_data_of_person(self):
        print(f"my new company is {self.company} and my expected salary is {self.expectedsalary}")
newbio = Biodata()
newbio.company = "TCS"
newbio.expectedsalary = 2300000
newbio.bio_data_of_person()

# Problem sets
class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getinfo(self):
        print(f"The name of programmer is {self.name} and product is {self.product}")

info = Programmer("Harry", "skype")
info2 = Programmer("saloni", "github")
info.getinfo()
info2.getinfo()

# Problem set 2

class Calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        print(f"The square of given  number is {self.num**2}")
         
        
    def squareroot(self):
        print(f"The square root of no. is {self.num ** 0.5}")
    def cube(self):
        print(f"The cube of given number is {self.num**3}")
a = Calculator(3)
a.square()
a.squareroot()
a.cube()

# Problem set 3

class Sample:
    a = "Saloni"
obj = Sample()
obj.a = "Vicky"
print(Sample.a)
print(obj.a)

# Problem set 4

class Calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        print(f"The square of given  number is {self.num**2}")
         
        
    def squareroot(self):
        print(f"The square root of no. is {self.num ** 0.5}")
    def cube(self):
        print(f"The cube of given number is {self.num**3}")

    @staticmethod # If you do not want to use self then use @staticmethod.
    def greet():
        print("Welcome to the best calculator of the world")
a = Calculator(3)
a.greet()
a.square()
a.squareroot()
a.cube()

# problem set 5

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in train is {self.seats}")
        print(f"The price of Train is {self.fare}")
    def bookseats(self):
        if(self.seats>0):
            print(f"Your ticket has been booked and seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry for incovenience")
intercity = Train("Intercity Express: 14078", 89, 2)
intercity.getStatus()
intercity.bookseats()
intercity.bookseats()
intercity.bookseats()
intercity.bookseats()

# Problem set 6

class Sample:
    a = "Harry"
    def __init__(self, name):
        self.name = name

obj = Sample("saloni")
print(obj.name)

# *********************************** Inheritance *********************************************************
'''' Inheritance is a way of creating a new class from an existing class.
syntax: 
class employee:
    #code
    
There are three types of inheritance 
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance '''

class Enterdata:
    company = "Informatica"

    def showDetails(self):
        print("This is employee")
class Coder(Enterdata):
    language = "Pyhton"
    def getlanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("This is coder")
e = Enterdata()
e.showDetails()
p = Coder()
p.showDetails()
p.getlanguage()

class Single:
    company1 = "Visa"
class Freelancer:
    company = "Fiverr"
    def Writer(self):
        print(f" The name of company is {self.company} ")
class Programmer_by(Single, Freelancer):
    name = "Rohit"
a = Programmer_by()
a.Writer()

# Multi level inheritance
class Person:
    country = "India"
    def takeBreak(self):
        print("I am breathing..")
class Employees:
    company = "Honda"
    def getstarted(self):
        print(f"Salary is {self.salary}")

    def takebreak(self):
        print("I am employee so i am luckily breathing.")
    def Programmer(Employees):
        company = "Fiverr"
    def getstarted(self):
        print(f"no salary to programmers.")

P = Person()
P.takeBreak()
e = Employees()
e.takebreak()













  
        







