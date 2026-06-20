"""
=========================================================
            PYTHON CONSTRUCTORS (__init__)
=========================================================

What is a Constructor?
----------------------

A constructor is a special method that is
automatically called when an object is created.

In Python, the constructor is:

__init__()

It is mainly used to initialize object attributes.

Syntax

class ClassName:

    def __init__(self):
        ...
"""

# =========================================================
# Default Constructor
# =========================================================

class Student:

    def __init__(self):

        print("Student Object Created")

student1 = Student()

# Output
# Student Object Created


# =========================================================
# Parameterized Constructor
# =========================================================

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

student1 = Student("Vinita", 21)

print(student1.name)

print(student1.age)


# =========================================================
# Understanding self
# =========================================================

"""
self refers to the current object.

It is used to access instance variables
and methods.

Python automatically passes self.
"""

class Employee:

    def __init__(self, name, salary):

        self.name = name

        self.salary = salary

employee1 = Employee("Rahul", 50000)

print(employee1.name)

print(employee1.salary)


# =========================================================
# Multiple Objects
# =========================================================

student2 = Student("Amit", 20)

print(student2.name)

print(student2.age)


# =========================================================
# Constructor with Default Values
# =========================================================

class Car:

    def __init__(self, brand, color="Black"):

        self.brand = brand

        self.color = color

car1 = Car("Toyota")

car2 = Car("Honda", "White")

print(car1.brand, "-", car1.color)

print(car2.brand, "-", car2.color)


# =========================================================
# Constructor Calling Methods
# =========================================================

class Person:

    def __init__(self, name):

        self.name = name

        self.display()

    def display(self):

        print("Welcome", self.name)

person = Person("Vinita")


# =========================================================
# Real World Example
# =========================================================

class Laptop:

    def __init__(self, brand, ram, price):

        self.brand = brand

        self.ram = ram

        self.price = price

    def show_details(self):

        print("Brand :", self.brand)

        print("RAM   :", self.ram)

        print("Price :", self.price)

laptop = Laptop("Lenovo", "16GB", 65000)

laptop.show_details()


# =========================================================
# Constructor vs Normal Method
# =========================================================

"""
Constructor

Automatically called

__init__()

Used for initialization

-----------------------------

Normal Method

Called manually

Any valid name

Performs specific task
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a constructor?

A special method automatically called
when an object is created.

------------------------------------

2. Constructor name?

__init__()

------------------------------------

3. Is constructor called manually?

No.

------------------------------------

4. What is self?

Reference to current object.

------------------------------------

5. Can a constructor take parameters?

Yes.

------------------------------------

6. Can a class have multiple constructors?

No (Python does not support constructor overloading).

------------------------------------

7. Can we define a class without __init__()?

Yes.

Python provides a default constructor.

------------------------------------

8. What is the purpose of __init__()?

Initialize object attributes.
"""


# =========================================================
# Mini Project
# =========================================================

class Book:

    def __init__(self, title, author, price):

        self.title = title

        self.author = author

        self.price = price

    def display(self):

        print("\n========== BOOK ==========")

        print("Title  :", self.title)

        print("Author :", self.author)

        print("Price  :", self.price)

book = Book(

    "Python Programming",

    "Guido van Rossum",

    799

)

book.display()


# =========================================================
# Cheat Sheet
# =========================================================

"""
Constructor

def __init__(self):

----------------------------

Parameterized Constructor

def __init__(self, name):

----------------------------

Object Creation

obj = ClassName()

----------------------------

Access Attribute

obj.name

----------------------------

self

Current Object
"""

# =========================================================
# END OF FILE
# =========================================================