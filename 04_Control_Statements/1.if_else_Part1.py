"""
=========================================================
                PYTHON IF...ELSE STATEMENTS
=========================================================

What is Decision Making?
------------------------
Decision making allows a program to execute different
blocks of code based on a condition.

Python uses:

1. if
2. if...else
3. if...elif...else
4. Nested if
5. Ternary Operator

Conditions return either:

True
False

If the condition is True,
the if block executes.

Otherwise,
the else block executes.
"""

# =========================================================
# Comparison Operators
# =========================================================

"""
Comparison operators are mostly used with if statements.

==      Equal to

!=      Not Equal to

>       Greater Than

<       Less Than

>=      Greater Than or Equal

<=      Less Than or Equal
"""

a = 20
b = 15

print(a > b)
print(a == b)
print(a != b)

# Output:
# True
# False
# True


# =========================================================
# Simple if Statement
# =========================================================

"""
Syntax

if condition:
    statement
"""

age = 20

if age >= 18:
    print("Eligible for Voting")

print("Program Finished")

# Output:
# Eligible for Voting
# Program Finished


# =========================================================
# Another Example
# =========================================================

marks = 90

if marks >= 35:
    print("Pass")

# Output:
# Pass


# =========================================================
# if...else Statement
# =========================================================

"""
Syntax

if condition:
    statements

else:
    statements
"""

age = 16

if age >= 18:

    print("Adult")

else:

    print("Minor")

# Output:
# Minor


# =========================================================
# Example 2
# =========================================================

number = 7

if number % 2 == 0:

    print("Even")

else:

    print("Odd")

# Output:
# Odd


# =========================================================
# Example 3
# =========================================================

salary = 60000

if salary >= 50000:

    print("High Salary")

else:

    print("Low Salary")


# =========================================================
# if...elif...else
# =========================================================

"""
Used when multiple conditions need to be checked.

Syntax

if condition1:

elif condition2:

elif condition3:

else:
"""

marks = 82

if marks >= 90:

    print("Grade A")

elif marks >= 75:

    print("Grade B")

elif marks >= 60:

    print("Grade C")

elif marks >= 35:

    print("Grade D")

else:

    print("Fail")

# Output:
# Grade B


# =========================================================
# Example
# =========================================================

temperature = 32

if temperature >= 40:

    print("Very Hot")

elif temperature >= 30:

    print("Hot")

elif temperature >= 20:

    print("Pleasant")

else:

    print("Cold")


# =========================================================
# Nested if
# =========================================================

"""
An if statement inside another if statement
is called Nested if.
"""

age = 22

has_license = True

if age >= 18:

    if has_license:

        print("You can drive.")

    else:

        print("Get a Driving License.")

else:

    print("You are underage.")

# Output:
# You can drive.


# =========================================================
# Example
# =========================================================

username = "admin"

password = "1234"

if username == "admin":

    if password == "1234":

        print("Login Successful")

    else:

        print("Wrong Password")

else:

    print("Invalid Username")


# =========================================================
# Short-hand if
# =========================================================

"""
Used when only one statement is present.
"""

age = 21

if age >= 18: print("Eligible")

# Output:
# Eligible


# =========================================================
# Short-hand if...else (Ternary Operator)
# =========================================================

"""
Syntax

value_if_true if condition else value_if_false
"""

age = 17

status = "Adult" if age >= 18 else "Minor"

print(status)

# Output:
# Minor


# =========================================================
# Another Example
# =========================================================

a = 50
b = 70

largest = a if a > b else b

print("Largest =", largest)

# Output:
# Largest = 70


# =========================================================
# Nested Ternary Operator
# =========================================================

marks = 94

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "Fail"
)

print(grade)

# Output:
# A


# =========================================================
# Pass Statement
# =========================================================

"""
pass is used when you don't want
to write code immediately.
"""

age = 25

if age >= 18:
    pass

print("Program continues...")


# =========================================================
# Summary Table
# =========================================================

"""
Statement              Purpose

if                     Execute when condition is True

if...else              Choose between two blocks

if...elif...else       Multiple conditions

Nested if              if inside another if

Ternary                One-line if...else

pass                   Empty block
"""


# =========================================================
# END OF PART 1
# =========================================================