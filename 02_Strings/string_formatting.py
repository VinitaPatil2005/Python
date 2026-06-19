"""
=========================================================
                PYTHON STRING FORMATTING
=========================================================

What is String Formatting?
--------------------------
String formatting is the process of inserting values
inside a string.

Python provides three ways:

1. % Formatting (Old Style)
2. str.format() Method
3. f-Strings (Recommended)

"""

# =========================================================
# 1. OLD STYLE (%) FORMATTING
# =========================================================

name = "Vinita"
age = 21

print("My name is %s." % name)
print("I am %d years old." % age)

# Output:
# My name is Vinita.
# I am 21 years old.


# =========================================================
# Multiple Values
# =========================================================

name = "Vinita"
cgpa = 9.15

print("Name: %s | CGPA: %.2f" % (name, cgpa))

# Output:
# Name: Vinita | CGPA: 9.15


# =========================================================
# 2. format() METHOD
# =========================================================

name = "Vinita"
city = "Pune"

print("My name is {}.".format(name))
print("{} lives in {}.".format(name, city))

# Output:
# My name is Vinita.
# Vinita lives in Pune.


# =========================================================
# Positional Index
# =========================================================

print("{1} is learning {0}".format("Python", "Vinita"))

# Output:
# Vinita is learning Python


# =========================================================
# Named Arguments
# =========================================================

print(
    "Name: {name}, Age: {age}".format(
        name="Vinita",
        age=21
    )
)

# Output:
# Name: Vinita, Age: 21


# =========================================================
# Formatting Decimal Numbers
# =========================================================

pi = 3.1415926535

print("{:.2f}".format(pi))
print("{:.3f}".format(pi))

# Output:
# 3.14
# 3.142


# =========================================================
# Width
# =========================================================

num = 25

print("{:10}".format(num))

print("{:<10}".format(num))

print("{:>10}".format(num))

print("{:^10}".format(num))


# =========================================================
# Alignment
# =========================================================

text = "Python"

print("|{:>15}|".format(text))

print("|{:<15}|".format(text))

print("|{:^15}|".format(text))


# =========================================================
# Fill Character
# =========================================================

print("{:*^20}".format("Python"))

print("{:-<20}".format("Python"))

print("{:*>20}".format("Python"))


# =========================================================
# Thousand Separator
# =========================================================

salary = 2500000

print("{:,}".format(salary))

# Output:
# 2,500,000


# =========================================================
# Percentage
# =========================================================

marks = 95

print("Percentage: {}%".format(marks))

# Output:
# Percentage: 95%


# =========================================================
# Binary
# =========================================================

num = 20

print("Binary :", format(num, "b"))

# Output:
# 10100


# =========================================================
# Octal
# =========================================================

print("Octal :", format(num, "o"))

# Output:
# 24


# =========================================================
# Hexadecimal
# =========================================================

print("Hex :", format(num, "x"))

print("HEX :", format(num, "X"))

# Output:
# 14
# 14


# =========================================================
# Scientific Notation
# =========================================================

num = 123456

print("{:e}".format(num))

print("{:.2e}".format(num))


# =========================================================
# 3. f-Strings (Python 3.6+)
# =========================================================

"""
Recommended method.

Fast

Easy to read

Most commonly used.
"""

name = "Vinita"

age = 21

print(f"My name is {name}.")

print(f"My age is {age}.")

# Output:
# My name is Vinita.
# My age is 21.


# =========================================================
# Expressions inside f-Strings
# =========================================================

a = 10
b = 20

print(f"Addition = {a+b}")

print(f"Multiplication = {a*b}")

print(f"Average = {(a+b)/2}")


# =========================================================
# Function Call inside f-String
# =========================================================

name = "python"

print(f"{name.upper()}")

print(f"{name.capitalize()}")


# =========================================================
# Decimal Formatting
# =========================================================

pi = 3.1415926535

print(f"{pi:.2f}")

print(f"{pi:.4f}")

# Output:
# 3.14
# 3.1416


# =========================================================
# Width and Alignment
# =========================================================

word = "Python"

print(f"|{word:<15}|")

print(f"|{word:>15}|")

print(f"|{word:^15}|")


# =========================================================
# Thousands Separator
# =========================================================

salary = 2500000

print(f"{salary:,}")

# Output:
# 2,500,000


# =========================================================
# Percentage
# =========================================================

score = 0.95

print(f"{score:.2%}")

# Output:
# 95.00%


# =========================================================
# Binary, Octal and Hex
# =========================================================

number = 100

print(f"Binary : {number:b}")

print(f"Octal : {number:o}")

print(f"Hex : {number:x}")

print(f"HEX : {number:X}")


# =========================================================
# Summary Table
# =========================================================

"""
Formatting Method        Example

Old Style               %s %d %.2f

format()                {}

f-String                f"{name}"

Decimal                 :.2f

Left Align              :<10

Right Align             :>10

Center                  :^10

Thousands               :,

Binary                  :b

Octal                   :o

Hexadecimal             :x

Percentage              :.2%
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is string formatting?

Answer:
It is the process of inserting values into a string.

------------------------------------------------

2. Name three formatting methods.

Answer:

1. %

2. format()

3. f-Strings

------------------------------------------------

3. Which formatting method is recommended?

Answer:

f-Strings

------------------------------------------------

4. Which Python version introduced f-Strings?

Answer:

Python 3.6

------------------------------------------------

5. How do you display two decimal places?

Answer:

{:.2f}

------------------------------------------------

6. Which specifier displays binary?

Answer:

:b

------------------------------------------------

7. Which specifier displays hexadecimal?

Answer:

:x

------------------------------------------------

8. Which specifier adds commas?

Answer:

:,

------------------------------------------------

9. How do you center text?

Answer:

:^20

------------------------------------------------

10. Which formatting method is the fastest?

Answer:

f-Strings
"""


# =========================================================
# MINI PROJECT
# =========================================================

print("\n========== STUDENT REPORT ==========")

name = "Vinita"
roll = 25
branch = "AIML"
cgpa = 9.15

print(f"Name    : {name}")
print(f"Roll No : {roll}")
print(f"Branch  : {branch}")
print(f"CGPA    : {cgpa:.2f}")

print("=" * 40)


# =========================================================
# END OF FILE
# =========================================================