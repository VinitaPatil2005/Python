"""
=========================================================
                PYTHON METHODS
=========================================================

What are Methods?
-----------------

Methods are functions defined inside a class.

Python has three types of methods:

1. Instance Method
2. Class Method
3. Static Method
"""

# =========================================================
# Instance Method
# =========================================================

"""
Instance methods work with object data.

They use self as the first parameter.
"""

class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def display(self):

        print("Name :", self.name)
        print("Marks:", self.marks)

student = Student("Vinita", 95)

student.display()


# =========================================================
# Another Instance Method
# =========================================================

class Rectangle:

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width

rectangle = Rectangle(10, 5)

print("Area =", rectangle.area())


# =========================================================
# Class Method
# =========================================================

"""
Class methods work with class variables.

Decorator:
@classmethod

First parameter:
cls
"""

class Employee:

    company = "Google"

    @classmethod
    def company_name(cls):

        print("Company:", cls.company)

Employee.company_name()


# =========================================================
# Changing Class Variable
# =========================================================

class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, name):

        cls.company = name

Employee.change_company("Microsoft")

print(Employee.company)

# Output
# Microsoft


# =========================================================
# Static Method
# =========================================================

"""
Static methods do not use

self

or

cls

Decorator:

@staticmethod
"""

class Calculator:

    @staticmethod
    def add(a, b):

        return a + b

print(Calculator.add(10, 20))


# =========================================================
# Another Static Method
# =========================================================

class Math:

    @staticmethod
    def square(number):

        return number ** 2

print(Math.square(8))


# =========================================================
# Calling Methods
# =========================================================

class Car:

    def start(self):

        print("Car Started")

car = Car()

car.start()


# =========================================================
# Accessing Instance Variables
# =========================================================

class Laptop:

    def __init__(self, brand, price):

        self.brand = brand
        self.price = price

    def display(self):

        print(self.brand)
        print(self.price)

laptop = Laptop("Lenovo", 65000)

laptop.display()


# =========================================================
# Accessing Class Variables
# =========================================================

class Mobile:

    category = "Electronics"

    def display(self):

        print(Mobile.category)

phone = Mobile()

phone.display()


# =========================================================
# Difference Between Methods
# =========================================================

"""
Instance Method

Uses self

Works with object variables

------------------------------------

Class Method

Uses cls

Works with class variables

------------------------------------

Static Method

Uses neither self nor cls

Utility method
"""


# =========================================================
# Real World Example
# =========================================================

class Bank:

    bank_name = "State Bank"

    def __init__(self, holder, balance):

        self.holder = holder
        self.balance = balance

    def show_account(self):

        print("Holder :", self.holder)
        print("Balance:", self.balance)

    @classmethod
    def show_bank(cls):

        print("Bank :", cls.bank_name)

    @staticmethod
    def interest():

        print("Interest Rate = 7%")

account = Bank("Vinita", 50000)

account.show_account()

Bank.show_bank()

Bank.interest()


# =========================================================
# Interview Questions
# =========================================================

"""
1. What are methods?

Functions inside a class.

------------------------------------

2. Types of methods?

Instance Method

Class Method

Static Method

------------------------------------

3. Which method uses self?

Instance Method.

------------------------------------

4. Which method uses cls?

Class Method.

------------------------------------

5. Which decorator is used for class method?

@classmethod

------------------------------------

6. Which decorator is used for static method?

@staticmethod

------------------------------------

7. Can a static method access instance variables?

No.

------------------------------------

8. Can an instance method access class variables?

Yes.

------------------------------------

9. Which method is used for utility functions?

Static Method.
"""


# =========================================================
# Mini Project
# =========================================================

class Student:

    school = "ABC School"

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def show(self):

        print("Name :", self.name)
        print("Marks:", self.marks)

    @classmethod
    def school_name(cls):

        print("School:", cls.school)

    @staticmethod
    def pass_marks():

        print("Pass Marks = 35")

student = Student("Vinita", 92)

student.show()

Student.school_name()

Student.pass_marks()


# =========================================================
# END OF FILE
# =========================================================