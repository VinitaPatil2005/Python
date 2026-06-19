"""
=========================================================
                PYTHON FUNCTIONS
=========================================================

What is a Function?
-------------------

A function is a reusable block of code that performs
a specific task.

Instead of writing the same code again and again,
we write it once inside a function and call it whenever
needed.

Advantages of Functions

- Code Reusability
- Better Readability
- Easy Debugging
- Modular Programming
- Reduces Code Duplication

=========================================================
Syntax
=========================================================

def function_name(parameters):
    statements
    return value

Function Definition

def

Keyword used to define a function.

Function Call

function_name(arguments)
"""

# =========================================================
# Simple Function
# =========================================================

def greet():

    print("Welcome to Python!")

greet()

# Output
# Welcome to Python!

# =========================================================
# Function with One Parameter
# =========================================================

def greet(name):

    print("Hello", name)

greet("Vinita")

greet("Rahul")


# =========================================================
# Function with Multiple Parameters
# =========================================================

def student(name, age, branch):

    print("Name   :", name)

    print("Age    :", age)

    print("Branch :", branch)

student("Vinita", 21, "AIML")


# =========================================================
# Function Returning Value
# =========================================================

def add(a, b):

    return a + b

result = add(10, 20)

print(result)

# Output
# 30


# =========================================================
# Returning Multiple Values
# =========================================================

def calculate(a, b):

    addition = a + b

    subtraction = a - b

    multiplication = a * b

    return addition, subtraction, multiplication

add_result, sub_result, mul_result = calculate(20, 10)

print(add_result)

print(sub_result)

print(mul_result)


# =========================================================
# Function Without return
# =========================================================

def message():

    print("Python")

value = message()

print(value)

# Output
# Python
# None


# =========================================================
# Default Parameters
# =========================================================

def greet(name="Guest"):

    print("Hello", name)

greet()

greet("Vinita")


# =========================================================
# Keyword Arguments
# =========================================================

def employee(name, salary, city):

    print(name)

    print(salary)

    print(city)

employee(

    city="Pune",

    salary=50000,

    name="Rahul"

)


# =========================================================
# Positional Arguments
# =========================================================

employee("Amit", 45000, "Mumbai")


# =========================================================
# Positional + Keyword
# =========================================================

employee(

    "Sneha",

    city="Nashik",

    salary=65000

)


# =========================================================
# Variable-Length Arguments (*args)
# =========================================================

"""
*args allows multiple positional arguments.
"""

def total_marks(*marks):

    print(marks)

    print(sum(marks))

total_marks(80, 85, 90)

total_marks(70, 75)


# =========================================================
# Variable-Length Keyword Arguments (**kwargs)
# =========================================================

"""
**kwargs stores keyword arguments
inside a dictionary.
"""

def student_details(**details):

    print(details)

student_details(

    name="Vinita",

    age=21,

    branch="AIML"

)


# =========================================================
# Combining Parameters
# =========================================================

def sample(a, b=0, *args, **kwargs):

    print(a)

    print(b)

    print(args)

    print(kwargs)

sample(

    10,

    20,

    30,

    40,

    city="Pune",

    cgpa=9.15

)


# =========================================================
# Function Documentation
# =========================================================

def square(number):

    """
    Returns the square of a number.
    """

    return number ** 2

print(square(5))

print(square.__doc__)


# =========================================================
# Built-in Functions
# =========================================================

numbers = [10,20,30]

print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sum(numbers))

# =========================================================
# END OF PART 1
# =========================================================