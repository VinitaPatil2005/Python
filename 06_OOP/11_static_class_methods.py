"""
=========================================================
      PYTHON STATIC METHOD & CLASS METHOD
=========================================================

Python provides three types of methods:

1. Instance Method
2. Class Method
3. Static Method

This file focuses on Class Methods and
Static Methods.
"""

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

class Student:

    college = "PES Modern College"

    @classmethod
    def show_college(cls):

        print("College:", cls.college)

Student.show_college()


# =========================================================
# Modify Class Variable
# =========================================================

class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, name):

        cls.company = name

Employee.change_company("Microsoft")

print(Employee.company)


# =========================================================
# Alternative Constructor
# =========================================================

"""
Class methods are often used as
alternative constructors.
"""

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):

        name, age = data.split(",")

        return cls(name, int(age))

student = Student.from_string("Vinita,21")

print(student.name)

print(student.age)


# =========================================================
# Static Method
# =========================================================

"""
Static methods do not depend on

self

or

cls

Used for utility functions.
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
# Static Method Example
# =========================================================

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):

        return (c * 9/5) + 32

print(Temperature.celsius_to_fahrenheit(25))


# =========================================================
# Factory Method Example
# =========================================================

class Car:

    def __init__(self, brand, year):

        self.brand = brand
        self.year = year

    @classmethod
    def create_default(cls):

        return cls("Toyota", 2025)

car = Car.create_default()

print(car.brand)

print(car.year)


# =========================================================
# Difference
# =========================================================

"""
Instance Method

Uses self

Works with object variables

----------------------------

Class Method

Uses cls

Works with class variables

Can create objects

----------------------------

Static Method

Uses neither self nor cls

Utility function
"""


# =========================================================
# Real World Example
# =========================================================

class Bank:

    bank_name = "State Bank"

    def __init__(self, holder):

        self.holder = holder

    @classmethod
    def bank(cls):

        print("Bank:", cls.bank_name)

    @staticmethod
    def interest():

        print("Current Interest Rate = 7%")

account = Bank("Vinita")

Bank.bank()

Bank.interest()


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a class method?

Works with class variables.

-----------------------------------

2. Which decorator is used?

@classmethod

-----------------------------------

3. First parameter?

cls

-----------------------------------

4. What is a static method?

Independent utility method.

-----------------------------------

5. Which decorator is used?

@staticmethod

-----------------------------------

6. Does a static method use self?

No.

-----------------------------------

7. Does a static method use cls?

No.

-----------------------------------

8. Can a class method create objects?

Yes.

Using cls().
"""


# =========================================================
# Mini Project
# =========================================================

class Student:

    school = "ABC School"

    def __init__(self, name):

        self.name = name

    @classmethod
    def school_name(cls):

        print("School:", cls.school)

    @staticmethod
    def welcome():

        print("Welcome to the School")

student = Student("Vinita")

Student.school_name()

Student.welcome()

# =========================================================
# END OF FILE
# =========================================================