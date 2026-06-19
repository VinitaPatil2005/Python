"""
=========================================================
                PYTHON FOR LOOP
=========================================================

What is a Loop?
---------------
A loop is used to execute a block of code repeatedly.

Python provides two loops:

1. for Loop
2. while Loop

The for loop is mainly used when the number of
iterations is known.

=========================================================
Syntax
=========================================================

for variable in iterable:
    statements

Examples of Iterables

• List
• Tuple
• String
• Set
• Dictionary
• range()
"""

# =========================================================
# Simple for Loop
# =========================================================

for i in range(5):

    print(i)

# Output
# 0
# 1
# 2
# 3
# 4


# =========================================================
# range(stop)
# =========================================================

"""
range(stop)

Starts from 0.
"""

for i in range(10):

    print(i)


# =========================================================
# range(start, stop)
# =========================================================

for i in range(5, 11):

    print(i)

# Output
# 5 6 7 8 9 10


# =========================================================
# range(start, stop, step)
# =========================================================

for i in range(0, 21, 2):

    print(i)

# Even Numbers


# =========================================================
# Reverse Loop
# =========================================================

for i in range(10, 0, -1):

    print(i)

# Output
# 10 9 8 ... 1


# =========================================================
# Loop Through String
# =========================================================

language = "Python"

for letter in language:

    print(letter)


# =========================================================
# Loop Through List
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:

    print(fruit)


# =========================================================
# Loop Through Tuple
# =========================================================

numbers = (10, 20, 30)

for number in numbers:

    print(number)


# =========================================================
# Loop Through Set
# =========================================================

colors = {"Red", "Green", "Blue"}

for color in colors:

    print(color)


# =========================================================
# Loop Through Dictionary
# =========================================================

student = {

    "name": "Vinita",

    "age": 21,

    "city": "Pune"

}

for key in student:

    print(key)

print()

for key in student:

    print(key, ":", student[key])


# =========================================================
# Using items()
# =========================================================

for key, value in student.items():

    print(key, "=", value)


# =========================================================
# Using enumerate()
# =========================================================

languages = ["Python", "Java", "SQL"]

for index, language in enumerate(languages):

    print(index, language)

# Output
# 0 Python
# 1 Java
# 2 SQL


# =========================================================
# Using zip()
# =========================================================

names = ["Vinita", "Rahul", "Amit"]

marks = [90, 85, 95]

for name, mark in zip(names, marks):

    print(name, mark)


# =========================================================
# Nested for Loop
# =========================================================

for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)


# =========================================================
# Multiplication Table
# =========================================================

number = 5

for i in range(1, 11):

    print(f"{number} x {i} = {number * i}")


# =========================================================
# Sum of First 10 Numbers
# =========================================================

total = 0

for i in range(1, 11):

    total += i

print("Sum =", total)


# =========================================================
# Factorial
# =========================================================

number = 5

factorial = 1

for i in range(1, number + 1):

    factorial *= i

print("Factorial =", factorial)


# =========================================================
# Summary Table
# =========================================================

"""
Loop Type             Example

range(stop)           range(5)

range(start, stop)    range(2,10)

range(step)           range(0,20,2)

String                for ch in text

List                  for item in list

Dictionary            for key,value in dict.items()

enumerate()           Index + Value

zip()                 Combine Iterables
"""


# =========================================================
# END OF PART 1
# =========================================================