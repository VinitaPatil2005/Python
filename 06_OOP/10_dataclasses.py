"""
=========================================================
                PYTHON DATACLASSES
=========================================================

What is a Dataclass?
--------------------

A dataclass automatically generates special methods
like:

__init__()
__repr__()
__eq__()

This reduces boilerplate code.

Available from Python 3.7+

Import

from dataclasses import dataclass
"""

from dataclasses import dataclass, field

# =========================================================
# Basic Dataclass
# =========================================================

@dataclass
class Student:

    name: str
    age: int
    marks: int

student = Student("Vinita", 21, 95)

print(student)

# Output
# Student(name='Vinita', age=21, marks=95)


# =========================================================
# Access Attributes
# =========================================================

print(student.name)
print(student.age)
print(student.marks)


# =========================================================
# Equality Comparison
# =========================================================

student1 = Student("Vinita", 21, 95)
student2 = Student("Vinita", 21, 95)

print(student1 == student2)

# Output
# True


# =========================================================
# Default Values
# =========================================================

@dataclass
class Employee:

    name: str
    salary: int = 30000

employee = Employee("Rahul")

print(employee)


# =========================================================
# field()
# =========================================================

"""
field() provides additional customization.
"""

@dataclass
class Product:

    name: str
    price: float
    quantity: int = field(default=1)

product = Product("Laptop", 65000)

print(product)


# =========================================================
# default_factory
# =========================================================

"""
Useful for mutable objects like lists.
"""

@dataclass
class Classroom:

    students: list = field(default_factory=list)

room = Classroom()

room.students.append("Vinita")

room.students.append("Rahul")

print(room.students)


# =========================================================
# __post_init__()
# =========================================================

"""
Runs automatically after __init__().
"""

@dataclass
class Rectangle:

    length: float
    width: float

    def __post_init__(self):

        self.area = self.length * self.width

rectangle = Rectangle(10, 5)

print(rectangle.area)


# =========================================================
# Ordering Objects
# =========================================================

@dataclass(order=True)
class Marks:

    score: int

m1 = Marks(80)
m2 = Marks(90)

print(m1 < m2)
print(m1 > m2)


# =========================================================
# Frozen Dataclass
# =========================================================

"""
frozen=True creates immutable objects.
"""

@dataclass(frozen=True)
class User:

    username: str

user = User("Vinita")

print(user.username)

# user.username = "Rahul"   - Error


# =========================================================
# Advantages
# =========================================================

"""
- Less code
- Automatic __init__()
- Automatic __repr__()
- Automatic __eq__()
- Easy to read

"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a dataclass?

A class that automatically generates
special methods.

------------------------------------

2. Which module is used?

dataclasses

------------------------------------

3. Which decorator is used?

@dataclass

------------------------------------

4. Which Python version introduced dataclasses?

Python 3.7

------------------------------------

5. What is __post_init__()?

Runs immediately after __init__().

------------------------------------

6. What is frozen=True?

Makes objects immutable.

------------------------------------

7. Why use default_factory?

To safely initialize mutable objects.
"""


# =========================================================
# Mini Project
# =========================================================

@dataclass
class Book:

    title: str
    author: str
    price: float

book = Book(

    "Python Programming",

    "Guido",

    799

)

print("\n========== BOOK ==========")

print(book)


# =========================================================
# END OF FILE
# =========================================================