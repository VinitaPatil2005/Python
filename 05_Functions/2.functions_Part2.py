# =========================================================
#              PYTHON FUNCTIONS (PART 2)
# =========================================================

# =========================================================
# Local Variables
# =========================================================

"""
A local variable is created inside a function.

It can only be accessed within that function.
"""

def student():

    name = "Vinita"

    print(name)

student()

# print(name)

# NameError


# =========================================================
# Global Variables
# =========================================================

"""
A global variable is declared outside a function.

It can be accessed anywhere in the program.
"""

college = "PES Modern College"

def display():

    print(college)

display()

print(college)


# =========================================================
# Global Keyword
# =========================================================

"""
The global keyword allows a function
to modify a global variable.
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
# Local vs Global Variable
# =========================================================

value = 100

def demo():

    value = 50

    print("Local Value :", value)

demo()

print("Global Value:", value)


# =========================================================
# Nested Functions
# =========================================================

"""
A function defined inside another function
is called a Nested Function.
"""

def outer():

    print("Outer Function")

    def inner():

        print("Inner Function")

    inner()

outer()


# =========================================================
# Returning a Function
# =========================================================

def outer():

    def inner():

        print("Hello from Inner Function")

    return inner

message = outer()

message()


# =========================================================
# Function as an Object
# =========================================================

def greet():

    print("Welcome!")

welcome = greet

welcome()

greet()


# =========================================================
# Passing Function as Argument
# =========================================================

def square(number):

    return number ** 2

def cube(number):

    return number ** 3

def calculate(function, value):

    print(function(value))

calculate(square, 5)

calculate(cube, 5)


# =========================================================
# Higher Order Functions
# =========================================================

"""
A Higher Order Function is a function that

- Accepts another function

or

- Returns another function.
"""

def operation(function, value):

    return function(value)

print(operation(square, 10))


# =========================================================
# First-Class Functions
# =========================================================

"""
Python treats functions as objects.

They can be

- Assigned
- Passed
- Returned
"""

def hello():

    print("Hello Python")

func = hello

func()


# =========================================================
# Recursive Thinking (Preview)
# =========================================================

"""
A function calling itself is called Recursion.

Detailed explanation is covered
in recursion.py
"""

def countdown(number):

    if number == 0:

        print("Finished")

        return

    print(number)

    countdown(number - 1)

countdown(5)


# =========================================================
# Anonymous Function Preview
# =========================================================

"""
Lambda Functions are covered in

lambda_functions.py
"""

square = lambda x: x ** 2

print(square(8))


# =========================================================
# Function with List
# =========================================================

def average(numbers):

    return sum(numbers) / len(numbers)

marks = [90, 85, 95, 88]

print(average(marks))


# =========================================================
# Function with Dictionary
# =========================================================

def print_student(student):

    for key, value in student.items():

        print(f"{key} : {value}")

student = {

    "Name": "Vinita",

    "Age": 21,

    "CGPA": 9.15

}

print_student(student)


# =========================================================
# Function with String
# =========================================================

def reverse_string(text):

    return text[::-1]

print(reverse_string("Python"))


# =========================================================
# Function Returning Boolean
# =========================================================

def is_even(number):

    return number % 2 == 0

print(is_even(10))

print(is_even(15))


# =========================================================
# Practical Example
# =========================================================

def calculate_area(length, width):

    return length * width

area = calculate_area(10, 20)

print("Area =", area)


# =========================================================
# Summary Table
# =========================================================

"""
Concept                 Description

Local Variable          Exists inside function

Global Variable         Exists throughout program

global                  Modify global variable

Nested Function         Function inside function

Higher Order Function   Accepts/Returns function

First-Class Function    Function as object

Lambda                  Anonymous function

Recursion               Function calling itself
"""


# =========================================================
# END OF PART 2
# =========================================================