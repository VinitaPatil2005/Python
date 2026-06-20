"""
=========================================================
    INSTANCE VARIABLES vs CLASS VARIABLES
=========================================================

What are Variables in a Class?
------------------------------

Python supports two types of variables:

1. Instance Variables
2. Class Variables

Understanding the difference is very important
for interviews and real-world projects.
"""

# =========================================================
# Instance Variables
# =========================================================

"""
Instance variables belong to an object.

Each object has its own copy.

Defined using self.variable.
"""

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

student1 = Student("Vinita", 21)
student2 = Student("Rahul", 22)

print(student1.name)
print(student2.name)

# Output
# Vinita
# Rahul


# =========================================================
# Class Variables
# =========================================================

"""
Class variables are shared by all objects.

Declared directly inside the class.
"""

class Student:

    college = "PES Modern College"

student1 = Student()
student2 = Student()

print(student1.college)
print(student2.college)

# Output
# PES Modern College
# PES Modern College


# =========================================================
# Mixing Instance and Class Variables
# =========================================================

class Student:

    college = "PES Modern College"

    def __init__(self, name):

        self.name = name

student1 = Student("Vinita")
student2 = Student("Amit")

print(student1.name)
print(student1.college)

print(student2.name)
print(student2.college)


# =========================================================
# Changing Class Variable
# =========================================================

class Employee:

    company = "Google"

employee1 = Employee()
employee2 = Employee()

Employee.company = "Microsoft"

print(employee1.company)
print(employee2.company)

# Output
# Microsoft
# Microsoft


# =========================================================
# Changing Instance Variable
# =========================================================

class Car:

    def __init__(self, brand):

        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")

car1.brand = "BMW"

print(car1.brand)
print(car2.brand)

# Output
# BMW
# Honda


# =========================================================
# Accessing Class Variables
# =========================================================

class Laptop:

    warranty = "2 Years"

print(Laptop.warranty)

laptop = Laptop()

print(laptop.warranty)


# =========================================================
# Accessing Instance Variables
# =========================================================

class Mobile:

    def __init__(self, brand):

        self.brand = brand

phone = Mobile("Samsung")

print(phone.brand)


# =========================================================
# Difference
# =========================================================

"""
Instance Variable

✔ Belongs to object

✔ Different values

✔ Created using self

----------------------------

Class Variable

✔ Belongs to class

✔ Shared by all objects

✔ Created directly inside class
"""


# =========================================================
# Real World Example
# =========================================================

class Employee:

    company = "Infosys"

    def __init__(self, name, salary):

        self.name = name

        self.salary = salary

employee1 = Employee("Vinita", 60000)
employee2 = Employee("Rahul", 55000)

print(employee1.name)
print(employee1.salary)
print(employee1.company)

print(employee2.name)
print(employee2.salary)
print(employee2.company)


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is an Instance Variable?

Variable belonging to an object.

------------------------------------

2. What is a Class Variable?

Variable shared by all objects.

------------------------------------

3. Where is an instance variable declared?

Inside __init__()
using self.

------------------------------------

4. Where is a class variable declared?

Directly inside the class.

------------------------------------

5. Which variable is shared?

Class Variable.

------------------------------------

6. Can objects have different instance variables?

Yes.

------------------------------------

7. Can class variables be modified?

Yes.

Using ClassName.variable
"""


# =========================================================
# Mini Project
# =========================================================

class BankAccount:

    bank_name = "State Bank"

    def __init__(self, holder, balance):

        self.holder = holder

        self.balance = balance

account1 = BankAccount("Vinita", 50000)
account2 = BankAccount("Rahul", 35000)

print("\n========== BANK DETAILS ==========")

print(account1.holder)
print(account1.balance)
print(account1.bank_name)

print()

print(account2.holder)
print(account2.balance)
print(account2.bank_name)


# =========================================================
# Cheat Sheet
# =========================================================

"""
Instance Variable

self.name

------------------------

Class Variable

class Student:

    college = "ABC"

------------------------

Access

object.variable

ClassName.variable

------------------------

Shared

Class Variable

------------------------

Unique

Instance Variable
"""

# =========================================================
# END OF FILE
# =========================================================