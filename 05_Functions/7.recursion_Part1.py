"""
=========================================================
                PYTHON RECURSION
=========================================================

What is Recursion?
------------------

Recursion is a programming technique where a function
calls itself to solve a problem.

Every recursive function must have:

1. Base Case
   Stops recursion.

2. Recursive Case
   Calls itself with a smaller problem.

Without a base case,
the recursion will continue forever
and eventually cause a RecursionError.

=========================================================
Syntax
=========================================================

def function():

    if base_condition:
        return

    function()
"""

# =========================================================
# Simple Recursion
# =========================================================

def hello(count):

    if count == 0:
        return

    print("Hello Python")

    hello(count - 1)

hello(5)


# =========================================================
# Countdown
# =========================================================

def countdown(number):

    if number == 0:

        print("Blast Off!")

        return

    print(number)

    countdown(number - 1)

countdown(5)


# =========================================================
# Count Up
# =========================================================

def count_up(number):

    if number == 0:
        return

    count_up(number - 1)

    print(number)

count_up(5)


# =========================================================
# Factorial
# =========================================================

"""
5!

5 * 4 * 3 * 2 * 1

=120
"""

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))

# Output
# 120


# =========================================================
# Sum of First N Numbers
# =========================================================

def total(number):

    if number == 1:
        return 1

    return number + total(number - 1)

print(total(5))

# Output
# 15


# =========================================================
# Power Function
# =========================================================

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2, 5))

# Output
# 32


# =========================================================
# Fibonacci Series
# =========================================================

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(10):

    print(fibonacci(i), end=" ")

print()

# Output
# 0 1 1 2 3 5 8 13 21 34


# =========================================================
# Reverse String
# =========================================================

def reverse(text):

    if len(text) == 0:
        return ""

    return reverse(text[1:]) + text[0]

print(reverse("Python"))

# Output
# nohtyP


# =========================================================
# Sum of Digits
# =========================================================

def sum_digits(number):

    if number == 0:
        return 0

    return number % 10 + sum_digits(number // 10)

print(sum_digits(9876))

# Output
# 30


# =========================================================
# Count Digits
# =========================================================

def count_digits(number):

    if number == 0:
        return 0

    return 1 + count_digits(number // 10)

print(count_digits(123456))

# Output
# 6


# =========================================================
# END OF PART 1
# =========================================================