"""
=========================================================
                PYTHON WHILE LOOP
=========================================================

What is a while Loop?
---------------------
A while loop executes a block of code repeatedly
as long as the given condition is True.

Unlike the for loop,
the number of iterations is usually NOT known.

Syntax

while condition:
    statements

The condition is checked before every iteration.

If the condition becomes False,
the loop stops.
"""

# =========================================================
# Simple while Loop
# =========================================================

i = 1

while i <= 5:

    print(i)

    i += 1

# Output
# 1
# 2
# 3
# 4
# 5


# =========================================================
# Print 1 to 10
# =========================================================

number = 1

while number <= 10:

    print(number)

    number += 1


# =========================================================
# Print Even Numbers
# =========================================================

number = 2

while number <= 20:

    print(number)

    number += 2


# =========================================================
# Print Odd Numbers
# =========================================================

number = 1

while number <= 19:

    print(number)

    number += 2


# =========================================================
# Reverse Counting
# =========================================================

number = 10

while number >= 1:

    print(number)

    number -= 1


# =========================================================
# Sum of First 10 Numbers
# =========================================================

number = 1

total = 0

while number <= 10:

    total += number

    number += 1

print("Sum =", total)

# Output
# Sum = 55


# =========================================================
# Multiplication Table
# =========================================================

table = 7

i = 1

while i <= 10:

    print(f"{table} x {i} = {table*i}")

    i += 1


# =========================================================
# Factorial
# =========================================================

number = 5

factorial = 1

i = 1

while i <= number:

    factorial *= i

    i += 1

print("Factorial =", factorial)

# Output
# Factorial = 120


# =========================================================
# Traverse a String
# =========================================================

text = "Python"

index = 0

while index < len(text):

    print(text[index])

    index += 1


# =========================================================
# Traverse a List
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

index = 0

while index < len(fruits):

    print(fruits[index])

    index += 1


# =========================================================
# User Controlled Loop
# =========================================================

"""
Uncomment to test

choice = "yes"

while choice.lower() == "yes":

    print("Program Running")

    choice = input("Continue? (yes/no): ")
"""


# =========================================================
# Infinite Loop
# =========================================================

"""
while True:

    print("Infinite Loop")

Press Ctrl + C to stop.
"""


# =========================================================
# Counting Digits
# =========================================================

number = 987654

count = 0

while number > 0:

    number //= 10

    count += 1

print("Digits =", count)

# Output
# Digits = 6


# =========================================================
# Reverse a Number
# =========================================================

number = 12345

reverse = 0

while number > 0:

    digit = number % 10

    reverse = reverse * 10 + digit

    number //= 10

print("Reverse =", reverse)

# Output
# Reverse = 54321


# =========================================================
# Summary Table
# =========================================================

"""
Loop Type              Example

Simple Loop            while i <= 10

Reverse Loop           while i >= 1

Infinite Loop          while True

List Traversal         while index < len(list)

String Traversal       while index < len(string)
"""


# =========================================================
# END OF PART 1
# =========================================================