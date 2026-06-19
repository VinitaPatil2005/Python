"""
=========================================================
            PYTHON MATCH...CASE STATEMENT
=========================================================

What is match...case?
---------------------

match...case is Python's version of a switch statement.

Introduced in Python 3.10.

It compares one value against multiple patterns.

Only one matching case executes.

Syntax

match variable:

    case value1:
        statements

    case value2:
        statements

    case _:
        default statements
"""

# =========================================================
# Basic Example
# =========================================================

day = 2

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid Day")

# Output
# Tuesday


# =========================================================
# Default Case
# =========================================================

month = 15

match month:

    case 1:
        print("January")

    case 2:
        print("February")

    case _:
        print("Invalid Month")


# =========================================================
# Multiple Values in One Case
# =========================================================

letter = "A"

match letter:

    case "A" | "E" | "I" | "O" | "U":
        print("Vowel")

    case _:
        print("Consonant")


# =========================================================
# Calculator
# =========================================================

a = 20
b = 10

operator = "+"

match operator:

    case "+":
        print(a + b)

    case "-":
        print(a - b)

    case "*":
        print(a * b)

    case "/":
        print(a / b)

    case "//":
        print(a // b)

    case "%":
        print(a % b)

    case "**":
        print(a ** b)

    case _:
        print("Invalid Operator")


# =========================================================
# Grade Example
# =========================================================

grade = "A"

match grade:

    case "A":
        print("Excellent")

    case "B":
        print("Very Good")

    case "C":
        print("Good")

    case "D":
        print("Average")

    case _:
        print("Fail")


# =========================================================
# Number Check
# =========================================================

number = 3

match number:

    case 1:
        print("One")

    case 2:
        print("Two")

    case 3:
        print("Three")

    case _:
        print("Unknown")


# =========================================================
# Match with Guard
# =========================================================

age = 25

match age:

    case value if value >= 18:
        print("Adult")

    case _:
        print("Minor")


# =========================================================
# Even or Odd
# =========================================================

number = 12

match number % 2:

    case 0:
        print("Even")

    case _:
        print("Odd")


# =========================================================
# Matching Tuples
# =========================================================

point = (3, 0)

match point:

    case (0, 0):
        print("Origin")

    case (x, 0):
        print("X-Axis")

    case (0, y):
        print("Y-Axis")

    case (x, y):
        print("Point =", x, y)


# =========================================================
# Matching Lists
# =========================================================

numbers = [1, 2]

match numbers:

    case [x]:
        print("One Element")

    case [x, y]:
        print("Two Elements")

    case [x, y, z]:
        print("Three Elements")

    case _:
        print("Other")


# =========================================================
# Matching Dictionary
# =========================================================

student = {

    "name": "Vinita",

    "age": 21

}

match student:

    case {"name": name, "age": age}:

        print(name)

        print(age)

    case _:

        print("No Match")


# =========================================================
# Menu Program
# =========================================================

choice = 2

match choice:

    case 1:
        print("Add Student")

    case 2:
        print("Delete Student")

    case 3:
        print("Update Student")

    case 4:
        print("Search Student")

    case _:
        print("Invalid Choice")


# =========================================================
# Nested Match
# =========================================================

department = "IT"

role = "Developer"

match department:

    case "IT":

        match role:

            case "Developer":
                print("Write Code")

            case "Tester":
                print("Test Software")

            case _:
                print("Unknown Role")

    case _:
        print("Unknown Department")


# =========================================================
# Common Mistakes
# =========================================================

"""
Wrong

switch(value):

Reason

Python uses match.

-----------------------------------

Wrong

default:

Correct

case _:

-----------------------------------

match is available only
from Python 3.10 onwards.
"""


# =========================================================
# Time Complexity
# =========================================================

"""
Simple match

O(1)

Worst Case

O(n)

Depends on number of cases.
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is match...case?

Answer:
A decision-making statement similar to switch.

------------------------------------------------

2. Which Python version introduced match?

Answer:
Python 3.10

------------------------------------------------

3. Which keyword replaces switch?

Answer:

match

------------------------------------------------

4. Which keyword replaces case?

Answer:

case

------------------------------------------------

5. Which symbol represents default?

Answer:

_

------------------------------------------------

6. Can multiple values be matched?

Answer:
Yes.

case 1 | 2 | 3

------------------------------------------------

7. Can match use conditions?

Answer:
Yes.

Using guards.

------------------------------------------------

8. Can match work with tuples?

Answer:
Yes.

------------------------------------------------

9. Can match work with dictionaries?

Answer:
Yes.

------------------------------------------------

10. Can match work with lists?

Answer:
Yes.

------------------------------------------------

11. Does Python support switch?

Answer:
No.

Instead, Python uses match...case.

------------------------------------------------

12. Which statement is better for many choices?

Answer:

match...case
"""


# =========================================================
# MINI PROJECT
# =========================================================

print("\n========== MENU ==========")

choice = 3

match choice:

    case 1:
        print("Add Student")

    case 2:
        print("View Students")

    case 3:
        print("Update Student")

    case 4:
        print("Delete Student")

    case 5:
        print("Exit")

    case _:
        print("Invalid Choice")

print("=" * 35)


# =========================================================
# CHEAT SHEET
# =========================================================

"""
Basic

match variable:

    case value:
        ...

----------------------------

Default

case _:

----------------------------

Multiple Values

case 1 | 2 | 3:

----------------------------

Guard

case value if condition:

----------------------------

Tuple

case (x, y):

----------------------------

Dictionary

case {"name": name}

----------------------------

List

case [x, y]
"""


# =========================================================
# END OF FILE
# =========================================================