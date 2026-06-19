"""
=========================================================
                PYTHON VARIABLES
=========================================================

What is a Variable?
-------------------
A variable is a named memory location used to store data.

Think of a variable as a container that stores information.

Example:
name = "Vinita"

Here,
'name' is the variable name.
'Vinita' is the value stored in the variable.

Python automatically decides the data type of the variable.
Therefore, Python is called a Dynamically Typed Language.
"""

# =========================================================
# Creating Variables
# =========================================================

name = "Vinita"
age = 21
cgpa = 9.15
is_student = True

print(name)
print(age)
print(cgpa)
print(is_student)

# Output:
# Vinita
# 21
# 9.15
# True

# =========================================================
# Checking Variable Type
# =========================================================

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

# Output:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>

# =========================================================
# Dynamic Typing
# =========================================================

"""
Python allows changing the data type of a variable
during program execution.
"""

x = 10
print(x)

x = "Python"

print(x)

# No error occurs because Python is dynamically typed.

# =========================================================
# Variable Naming Rules
# =========================================================

"""
Rules:

- Must start with a letter or underscore (_)
- Cannot start with a number
- Can contain:
    Letters
    Numbers
    Underscore (_)
- Cannot contain spaces
- Cannot use Python keywords
- Variable names are Case Sensitive
"""

student_name = "Amit"
_student = "Rahul"

# Valid

age1 = 20

# =========================================================
# Case Sensitivity
# =========================================================

name = "Vinita"

Name = "Python"

NAME = "Programming"

print(name)
print(Name)
print(NAME)

# All three variables are different.

# =========================================================
# Variable Naming Convention
# =========================================================

"""
1. snake_case (Recommended in Python)

student_name

total_marks

average_salary

-------------------------------------

2. camelCase

studentName

totalMarks

-------------------------------------

3. PascalCase

StudentName

EmployeeSalary
"""

student_name = "Vinita"

print(student_name)

# =========================================================
# Assign Multiple Values
# =========================================================

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# =========================================================
# Assign Same Value
# =========================================================

a = b = c = 100

print(a)
print(b)
print(c)

# =========================================================
# Unpacking a Collection
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

x, y, z = fruits

print(x)
print(y)
print(z)

# =========================================================
# Variable Reassignment
# =========================================================

city = "Pune"

print(city)

city = "Mumbai"

print(city)

# =========================================================
# Swapping Variables (Method 1)
# =========================================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# =========================================================
# Swapping Variables (Method 2)
# =========================================================

x = 5
y = 15

temp = x
x = y
y = temp

print(x)
print(y)

# =========================================================
# Swapping Variables (Method 3)
# =========================================================

m = 50
n = 100

m = m + n
n = m - n
m = m - n

print(m)
print(n)

# =========================================================
# Global Variable
# =========================================================

college = "PES Modern College"

def display():

    print(college)

display()

print(college)

# =========================================================
# Local Variable
# =========================================================

def student():

    name = "Vinita"

    print(name)

student()

# print(name)

# Error because local variable cannot be accessed outside
# the function.

# =========================================================
# Global Keyword
# =========================================================

count = 0

def increment():

    global count

    count += 1

increment()

print(count)

# =========================================================
# Constants
# =========================================================

"""
Python has no built-in constant.

Programmers write constants in UPPER_CASE by convention.
"""

PI = 3.14159

GRAVITY = 9.8

MAX_SIZE = 100

print(PI)

# =========================================================
# Memory Address
# =========================================================

"""
id() returns the memory address (identity)
of an object.
"""

x = 100

print(id(x))

y = 100

print(id(y))

# Small integers may share the same memory location.

# =========================================================
# Deleting Variables
# =========================================================

language = "Python"

print(language)

del language

# print(language)

# NameError because the variable is deleted.


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a variable?

Answer:
A variable is a named memory location used to store data.

-----------------------------------------------------

2. Why is Python called a dynamically typed language?

Answer:
Because we do not need to declare the data type explicitly.

-----------------------------------------------------

3. How do you check the type of a variable?

Answer:

type(variable)

-----------------------------------------------------

4. What is the difference between Global and Local variables?

Global Variable
- Declared outside functions
- Accessible everywhere

Local Variable
- Declared inside functions
- Accessible only inside that function

-----------------------------------------------------

5. What is a constant?

Answer:
A variable whose value should not change.
Python uses naming conventions (UPPER_CASE).

-----------------------------------------------------

6. Which naming style is recommended in Python?

Answer:
snake_case

-----------------------------------------------------

7. Which function returns the memory address?

Answer:
id()

-----------------------------------------------------

8. Can a variable change its data type?

Answer:
Yes.
Python supports dynamic typing.

-----------------------------------------------------

9. How do you delete a variable?

Answer:

del variable_name

-----------------------------------------------------

10. Are variable names case-sensitive?

Answer:
Yes.

age

Age

AGE

All are different variables.
"""
# =========================================================
# End of File
# =========================================================