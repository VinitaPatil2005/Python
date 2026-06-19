"""
=========================================================
                PYTHON SCOPE
=========================================================

What is Scope?
--------------

Scope determines where a variable can be accessed
inside a program.

Python follows the LEGB Rule:

L - Local
E - Enclosing
G - Global
B - Built-in
"""

# =========================================================
# Local Scope
# =========================================================

"""
A variable declared inside a function
can only be accessed inside that function.
"""

def student():

    name = "Vinita"

    print(name)

student()

# print(name)   # NameError


# =========================================================
# Global Scope
# =========================================================

"""
A variable declared outside all functions
can be accessed anywhere.
"""

college = "PES Modern College"

def display():

    print(college)

display()

print(college)


# =========================================================
# global Keyword
# =========================================================

"""
Used to modify a global variable.
"""

count = 0

def increment():

    global count

    count += 1

increment()
increment()

print(count)

# Output:
# 2


# =========================================================
# Enclosing Scope
# =========================================================

"""
A variable inside an outer function
is accessible inside the inner function.
"""

def outer():

    message = "Hello"

    def inner():

        print(message)

    inner()

outer()


# =========================================================
# nonlocal Keyword
# =========================================================

"""
Used to modify variables
from the enclosing scope.
"""

def outer():

    number = 10

    def inner():

        nonlocal number

        number += 5

        print(number)

    inner()

    print(number)

outer()

# Output
# 15
# 15


# =========================================================
# Built-in Scope
# =========================================================

"""
Built-in names are available everywhere.

Examples:
len()
max()
min()
sum()
print()
"""

numbers = [10,20,30]

print(len(numbers))

print(max(numbers))


# =========================================================
# LEGB Rule
# =========================================================

"""
Python searches variables in this order:

1. Local

2. Enclosing

3. Global

4. Built-in
"""


# =========================================================
# Variable Shadowing
# =========================================================

"""
A local variable can hide
a global variable.
"""

value = 100

def demo():

    value = 50

    print(value)

demo()

print(value)

# Output
# 50
# 100


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is scope?

Scope determines where a variable
can be accessed.

-------------------------------------

2. What is Local Scope?

Variables inside a function.

-------------------------------------

3. What is Global Scope?

Variables outside functions.

-------------------------------------

4. What is the global keyword?

Used to modify global variables.

-------------------------------------

5. What is the nonlocal keyword?

Used to modify enclosing variables.

-------------------------------------

6. What is LEGB?

Local

Enclosing

Global

Built-in
"""


# =========================================================
# CHEAT SHEET
# =========================================================

"""
Local        -> Inside Function

Global       -> Outside Function

global       -> Modify Global Variable

nonlocal     -> Modify Enclosing Variable

LEGB         -> Local -> Enclosing
                -> Global -> Built-in
"""

# =========================================================
# END OF FILE
# =========================================================