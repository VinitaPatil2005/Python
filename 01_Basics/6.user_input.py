"""
=========================================================
                PYTHON USER INPUT
=========================================================

What is User Input?
-------------------
User input allows the user to enter data while the program
is running.

Python uses the built-in input() function to accept input.

Syntax:
input("Message")

Example:
name = input("Enter your name: ")

NOTE:
The input() function ALWAYS returns data as a STRING.

If you need a number, convert it using int() or float().
"""

# =========================================================
# SIMPLE USER INPUT
# =========================================================

name = input("Enter your Name: ")

print("Hello,", name)

# Example Input:
# Vinita

# Output:
# Hello, Vinita


# =========================================================
# TAKING INTEGER INPUT
# =========================================================

"""
Since input() returns a string,
we convert it into an integer using int().
"""

age = int(input("Enter your Age: "))

print("Your age is:", age)

# Example Input:
# 21

# Output:
# Your age is: 21


# =========================================================
# TAKING FLOAT INPUT
# =========================================================

salary = float(input("Enter your Salary: "))

print("Salary =", salary)

# Example:
# 50000.50


# =========================================================
# TAKING STRING INPUT
# =========================================================

city = input("Enter your City: ")

print("City:", city)


# =========================================================
# MULTIPLE INPUTS
# =========================================================

"""
split() divides the entered text into multiple values.

Example Input:
Vinita 21 Pune
"""

name, age, city = input(
    "Enter Name Age City: "
).split()

print(name)
print(age)
print(city)


# =========================================================
# MULTIPLE INTEGER INPUTS
# =========================================================

"""
map(function, iterable)

Used to convert multiple values.

Example Input:
10 20
"""

num1, num2 = map(int, input(
    "Enter two numbers: "
).split())

print("Addition =", num1 + num2)


# =========================================================
# MULTIPLE FLOAT INPUTS
# =========================================================

a, b = map(float, input(
    "Enter two decimal numbers: "
).split())

print("Sum =", a + b)


# =========================================================
# USER INPUT EXAMPLE 1
# =========================================================

"""
Find Area of Rectangle
"""

length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

area = length * breadth

print("Area =", area)


# =========================================================
# USER INPUT EXAMPLE 2
# =========================================================

"""
Find Simple Interest

Formula:

SI = (P × R × T)/100
"""

principal = float(input("Principal Amount: "))

rate = float(input("Rate: "))

time = float(input("Time: "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)


# =========================================================
# USER INPUT EXAMPLE 3
# =========================================================

"""
Swap Two Numbers
"""

x = int(input("First Number: "))

y = int(input("Second Number: "))

print("Before Swapping")

print(x, y)

x, y = y, x

print("After Swapping")

print(x, y)


# =========================================================
# USER INPUT EXAMPLE 4
# =========================================================

"""
Check Adult or Minor
"""

age = int(input("Enter Age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# =========================================================
# USER INPUT EXAMPLE 5
# =========================================================

"""
Calculator
"""

num1 = float(input("Enter First Number: "))

num2 = float(input("Enter Second Number: "))

print("Addition =", num1 + num2)

print("Subtraction =", num1 - num2)

print("Multiplication =", num1 * num2)

print("Division =", num1 / num2)


# =========================================================
# STRING CONCATENATION
# =========================================================

first_name = input("First Name: ")

last_name = input("Last Name: ")

full_name = first_name + " " + last_name

print("Full Name:", full_name)


# =========================================================
# COMMON MISTAKES
# =========================================================

"""
Wrong

age = input("Age: ")

print(age + 5)

Reason:
input() returns String.

Correct

age = int(input("Age: "))

print(age + 5)
"""

# =========================================================
# TYPE CHECKING
# =========================================================

number = input("Enter Number: ")

print(type(number))

number = int(number)

print(type(number))

# Output:
# <class 'str'>
# <class 'int'>


# =========================================================
# SUMMARY TABLE
# =========================================================

"""
Statement                        Purpose

input()                          Accept input

int(input())                     Integer input

float(input())                   Float input

input().split()                  Multiple inputs

map(int, input().split())        Multiple integers

map(float, input().split())      Multiple floats
"""


# =========================================================
# INTERVIEW QUESTIONS
# =========================================================

"""
1. Which function is used to take user input?

Answer:
input()

------------------------------------------------

2. What data type does input() return?

Answer:
String

------------------------------------------------

3. How do you convert input into Integer?

Answer:

int(input())

------------------------------------------------

4. How do you convert input into Float?

Answer:

float(input())

------------------------------------------------

5. How do you take multiple inputs?

Answer:

input().split()

------------------------------------------------

6. How do you take multiple integers?

Answer:

map(int, input().split())

------------------------------------------------

7. What happens if you write?

age = input()

print(age + 5)

Answer:
TypeError

------------------------------------------------

8. What is map()?

Answer:
map() applies a function to every item in an iterable.

------------------------------------------------

9. Why is type conversion needed with input()?

Answer:
Because input() always returns a string.

------------------------------------------------

10. Which function separates multiple values entered by the user?

Answer:
split()
"""


# =========================================================
# MINI PROJECT
# =========================================================

print("\n========== STUDENT DETAILS ==========")

name = input("Name : ")

roll = input("Roll Number : ")

branch = input("Branch : ")

cgpa = float(input("CGPA : "))

print("\n===== STUDENT INFORMATION =====")

print("Name   :", name)

print("Roll No:", roll)

print("Branch :", branch)

print("CGPA   :", cgpa)

print("=====================================")


# =========================================================
# END OF FILE
# =========================================================