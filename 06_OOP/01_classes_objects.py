"""
=========================================================
        PYTHON OBJECT ORIENTED PROGRAMMING (OOP)
=========================================================

What is OOP?
------------

Object-Oriented Programming (OOP) is a programming
paradigm based on Objects and Classes.

OOP helps organize code into reusable, modular,
and maintainable components.

Advantages of OOP

- Code Reusability
- Better Security
- Easy Maintenance
- Scalability
- Real World Modelling

Python is an Object-Oriented Language.
"""

# =========================================================
# Class
# =========================================================

"""
A Class is a blueprint for creating objects.

Example

Class : Student

Attributes
-----------
name
age
marks

Methods
-------
study()
sleep()
"""

# =========================================================
# Object
# =========================================================

"""
An Object is an instance of a class.

Example

Student

↓

Vinita

Rahul

Amit

Each student is an object.
"""

# =========================================================
# Creating a Class
# =========================================================

class Student:

    pass


print(Student)

# Output:
# <class '__main__.Student'>


# =========================================================
# Creating Objects
# =========================================================

student1 = Student()

student2 = Student()

print(student1)

print(student2)

"""
Each object has a different memory address.
"""


# =========================================================
# Adding Attributes
# =========================================================

student1.name = "Vinita"
student1.age = 21
student1.branch = "AIML"

print(student1.name)
print(student1.age)
print(student1.branch)


# =========================================================
# Multiple Objects
# =========================================================

student2.name = "Rahul"
student2.age = 22
student2.branch = "Computer"

print(student2.name)
print(student2.age)
print(student2.branch)


# =========================================================
# Object Identity
# =========================================================

print(id(student1))

print(id(student2))

"""
id()

Returns object's memory address.
"""


# =========================================================
# isinstance()
# =========================================================

print(isinstance(student1, Student))

print(isinstance(student2, Student))

# Output
# True


# =========================================================
# type()
# =========================================================

print(type(student1))

print(type(student2))


# =========================================================
# Real World Example
# =========================================================

class Car:

    pass

car1 = Car()

car1.brand = "Toyota"

car1.model = "Fortuner"

car1.price = 4500000

print(car1.brand)

print(car1.model)

print(car1.price)


# =========================================================
# Difference Between Class and Object
# =========================================================

"""
Class

Blueprint

No Memory for Data

Creates Objects

----------------------------

Object

Instance of Class

Occupies Memory

Stores Actual Data
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is OOP?

Programming based on objects.

------------------------------------

2. What is a Class?

Blueprint of objects.

------------------------------------

3. What is an Object?

Instance of a class.

------------------------------------

4. Difference between Class and Object?

Class

Blueprint

Object

Real instance

------------------------------------

5. Which keyword creates a class?

class

------------------------------------

6. How to create an object?

obj = ClassName()

------------------------------------

7. Which function returns memory address?

id()

------------------------------------

8. Which function checks object type?

isinstance()

------------------------------------

9. Which function returns data type?

type()
"""


# =========================================================
# Mini Project
# =========================================================

class Mobile:

    pass

phone = Mobile()

phone.brand = "Samsung"

phone.model = "S24"

phone.price = 80000

print("\n========== MOBILE ==========")

print("Brand :", phone.brand)

print("Model :", phone.model)

print("Price :", phone.price)


# =========================================================
# END OF FILE
# =========================================================