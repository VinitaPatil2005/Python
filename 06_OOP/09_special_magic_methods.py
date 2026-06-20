"""
=========================================================
        PYTHON SPECIAL (MAGIC / DUNDER) METHODS
=========================================================

What are Special Methods?
-------------------------

Special methods (also called Magic Methods or Dunder Methods)
are predefined methods in Python.

They start and end with double underscores (__).

Examples

__init__()
__str__()
__repr__()
__len__()
__eq__()
__add__()

They allow us to customize the behavior of objects.
"""

# =========================================================
# __init__()
# =========================================================

"""
Automatically called when an object is created.
"""

class Student:

    def __init__(self, name):

        self.name = name

student = Student("Vinita")

print(student.name)


# =========================================================
# __str__()
# =========================================================

"""
Returns a user-friendly string representation
of an object.

Called by print(object).
"""

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):

        return f"Name: {self.name}, Age: {self.age}"

student = Student("Vinita", 21)

print(student)


# =========================================================
# __repr__()
# =========================================================

"""
Returns an official string representation.

Used mainly for debugging.
"""

class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def __repr__(self):

        return f"Employee('{self.name}', {self.salary})"

employee = Employee("Rahul", 50000)

print(repr(employee))


# =========================================================
# __len__()
# =========================================================

"""
Allows len() to work on custom objects.
"""

class Playlist:

    def __init__(self, songs):

        self.songs = songs

    def __len__(self):

        return len(self.songs)

playlist = Playlist(["Song1", "Song2", "Song3"])

print(len(playlist))


# =========================================================
# __eq__()
# =========================================================

"""
Defines equality between objects.
"""

class Student:

    def __init__(self, marks):

        self.marks = marks

    def __eq__(self, other):

        return self.marks == other.marks

student1 = Student(90)
student2 = Student(90)

print(student1 == student2)

# Output
# True


# =========================================================
# __add__()
# =========================================================

"""
Overloads the + operator.
"""

class Box:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return self.value + other.value

box1 = Box(20)
box2 = Box(30)

print(box1 + box2)

# Output
# 50


# =========================================================
# __lt__() and __gt__()
# =========================================================

"""
Customize < and > operators.
"""

class Student:

    def __init__(self, marks):

        self.marks = marks

    def __lt__(self, other):

        return self.marks < other.marks

    def __gt__(self, other):

        return self.marks > other.marks

student1 = Student(75)
student2 = Student(90)

print(student1 < student2)
print(student1 > student2)


# =========================================================
# Real World Example
# =========================================================

class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def __str__(self):

        return f"{self.name} - ₹{self.price}"

product = Product("Laptop", 65000)

print(product)


# =========================================================
# Commonly Used Magic Methods
# =========================================================

"""
Method              Purpose

__init__()          Constructor

__str__()           String representation

__repr__()          Official representation

__len__()           Supports len()

__eq__()            Equality

__add__()           + operator

__lt__()            < operator

__gt__()            > operator
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What are Magic Methods?

Special predefined methods.

-----------------------------------

2. Why are they called Dunder methods?

Because they have Double UNDERscores.

-----------------------------------

3. Which method is called automatically?

__init__()

-----------------------------------

4. Which method is called by print()?

__str__()

-----------------------------------

5. Difference between __str__() and __repr__()?

__str__()

Readable output.

__repr__()

Developer-friendly output.

-----------------------------------

6. Which method supports len()?

__len__()

-----------------------------------

7. Which method overloads + ?

__add__()

-----------------------------------

8. Which method overloads == ?

__eq__()
"""


# =========================================================
# Mini Project
# =========================================================

class Book:

    def __init__(self, title, price):

        self.title = title
        self.price = price

    def __str__(self):

        return f"{self.title} - ₹{self.price}"

    def __eq__(self, other):

        return self.price == other.price

book1 = Book("Python", 799)
book2 = Book("Data Science", 799)

print(book1)

print(book1 == book2)


# =========================================================
# Cheat Sheet
# =========================================================

"""
__init__()   -> Constructor

__str__()    -> print(object)

__repr__()   -> repr(object)

__len__()    -> len(object)

__eq__()     -> ==

__add__()    -> +

__lt__()     -> <

__gt__()     -> >
"""

# =========================================================
# END OF FILE
# =========================================================