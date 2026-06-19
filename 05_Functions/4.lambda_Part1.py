"""
=========================================================
            PYTHON LAMBDA FUNCTIONS
=========================================================

What is a Lambda Function?
--------------------------

A Lambda Function is a small anonymous function.

Anonymous means the function has no name.

Unlike normal functions, lambda functions
can contain only ONE expression.

Syntax

lambda arguments : expression

Example

square = lambda x: x ** 2

print(square(5))

Output
25

=========================================================
Advantages
=========================================================

- Short syntax
- One-line functions
- Useful with map()
- Useful with filter()
- Useful with sorted()
- Useful with reduce()
"""

# =========================================================
# Normal Function vs Lambda
# =========================================================

def square(number):

    return number ** 2

print(square(5))

square_lambda = lambda number: number ** 2

print(square_lambda(5))


# =========================================================
# Lambda with One Argument
# =========================================================

square = lambda x: x * x

print(square(6))


# =========================================================
# Lambda with Two Arguments
# =========================================================

add = lambda a, b: a + b

print(add(20, 30))


# =========================================================
# Lambda with Three Arguments
# =========================================================

average = lambda a, b, c: (a + b + c) / 3

print(average(10, 20, 30))


# =========================================================
# Lambda Returning Boolean
# =========================================================

is_even = lambda number: number % 2 == 0

print(is_even(20))

print(is_even(15))


# =========================================================
# Conditional Expression
# =========================================================

largest = lambda a, b: a if a > b else b

print(largest(25, 18))


# =========================================================
# Sorting using Lambda
# =========================================================

students = [

    ("Vinita", 90),

    ("Rahul", 82),

    ("Amit", 95),

    ("Sneha", 88)

]

students.sort(key=lambda student: student[1])

print(students)


# =========================================================
# sorted() with Lambda
# =========================================================

numbers = [5, 2, 9, 1, 7]

ascending = sorted(numbers)

descending = sorted(numbers, key=lambda x: -x)

print(ascending)

print(descending)


# =========================================================
# max() with Lambda
# =========================================================

employees = [

    {"name": "Rahul", "salary": 50000},

    {"name": "Vinita", "salary": 70000},

    {"name": "Amit", "salary": 60000}

]

highest = max(

    employees,

    key=lambda employee: employee["salary"]

)

print(highest)


# =========================================================
# min() with Lambda
# =========================================================

lowest = min(

    employees,

    key=lambda employee: employee["salary"]

)

print(lowest)


# =========================================================
# map()
# =========================================================

"""
map(function, iterable)

Applies a function to every element.
"""

numbers = [1, 2, 3, 4, 5]

square = list(

    map(lambda x: x ** 2, numbers)

)

print(square)

# Output
# [1,4,9,16,25]


# =========================================================
# map() Example
# =========================================================

names = ["vinita", "rahul", "amit"]

capital = list(

    map(lambda name: name.capitalize(), names)

)

print(capital)


# =========================================================
# filter()
# =========================================================

"""
filter(function, iterable)

Returns only matching elements.
"""

numbers = [10, 15, 20, 25, 30]

even = list(

    filter(lambda x: x % 2 == 0, numbers)

)

print(even)

# Output
# [10,20,30]


# =========================================================
# filter() Example
# =========================================================

students = [

    ("Vinita", 90),

    ("Rahul", 35),

    ("Amit", 28),

    ("Sneha", 80)

]

passed = list(

    filter(

        lambda student: student[1] >= 35,

        students

    )

)

print(passed)


# =========================================================
# reduce()
# =========================================================

"""
reduce()

Located inside functools module.
"""

from functools import reduce

numbers = [1,2,3,4,5]

total = reduce(

    lambda a, b: a + b,

    numbers

)

print(total)

# Output
# 15


# =========================================================
# Product using reduce()
# =========================================================

product = reduce(

    lambda a, b: a * b,

    numbers

)

print(product)


# =========================================================
# Summary Table
# =========================================================

"""
Function                Purpose

lambda                  Anonymous Function

map()                   Transform data

filter()                Filter data

reduce()                Reduce to one value

sorted()                Custom sorting

max()                   Largest element

min()                   Smallest element
"""


# =========================================================
# END OF PART 1
# =========================================================