"""
=========================================================
                    PYTHON TUPLES
=========================================================

What is a Tuple?
----------------
A Tuple is a built-in Python data structure used to store
multiple items in a single variable.

Unlike Lists, Tuples are IMMUTABLE.

This means once a tuple is created,
its elements cannot be modified.

Syntax:

tuple_name = (item1, item2, item3)

Example:

fruits = ("Apple", "Banana", "Mango")

=========================================================
FEATURES OF TUPLES
=========================================================

- Ordered
- Immutable
- Allows Duplicate Values
- Supports Indexing
- Supports Slicing
- Faster than Lists
- Can Store Different Data Types
"""

# =========================================================
# Creating Tuples
# =========================================================

fruits = ("Apple", "Banana", "Mango")

print(fruits)

# Output:
# ('Apple', 'Banana', 'Mango')


# =========================================================
# Tuple with Different Data Types
# =========================================================

student = (
    "Vinita",
    21,
    9.15,
    True
)

print(student)


# =========================================================
# Empty Tuple
# =========================================================

empty = ()

print(empty)


# =========================================================
# Single Element Tuple
# =========================================================

"""
Remember:

Comma is compulsory.
"""

t1 = (10)

print(type(t1))

# int

t2 = (10,)

print(type(t2))

# tuple


# =========================================================
# Using tuple() Constructor
# =========================================================

letters = tuple("Python")

print(letters)

# Output:
# ('P','y','t','h','o','n')


# =========================================================
# Length
# =========================================================

print(len(fruits))

# Output:
# 3


# =========================================================
# Indexing
# =========================================================

numbers = (10,20,30,40,50)

print(numbers[0])

print(numbers[2])

print(numbers[-1])

print(numbers[-2])


# =========================================================
# Slicing
# =========================================================

print(numbers[1:4])

print(numbers[:3])

print(numbers[2:])

print(numbers[::2])

print(numbers[::-1])


# =========================================================
# Traversing Tuple
# =========================================================

for item in fruits:

    print(item)


# =========================================================
# Traversing using Index
# =========================================================

for i in range(len(fruits)):

    print(i, fruits[i])


# =========================================================
# Membership Operators
# =========================================================

print("Apple" in fruits)

print("Orange" not in fruits)


# =========================================================
# Concatenation
# =========================================================

tuple1 = (1,2,3)

tuple2 = (4,5)

print(tuple1 + tuple2)

# Output:
# (1,2,3,4,5)


# =========================================================
# Repetition
# =========================================================

print(("Python",) * 3)

# Output:
# ('Python','Python','Python')


# =========================================================
# Immutability
# =========================================================

"""
Wrong

fruits[0] = "Orange"

Error

TypeError

Tuples cannot be modified.
"""


# =========================================================
# Updating Tuple
# =========================================================

"""
Since tuples are immutable,

Convert

Tuple → List

Modify

List → Tuple
"""

fruits = ("Apple","Banana","Mango")

temp = list(fruits)

temp[1] = "Orange"

fruits = tuple(temp)

print(fruits)


# =========================================================
# Deleting Tuple
# =========================================================

numbers = (1,2,3)

del numbers

# print(numbers)

# NameError


# =========================================================
# Built-in Functions
# =========================================================

numbers = (10,20,30,40)

print(len(numbers))

print(min(numbers))

print(max(numbers))

print(sum(numbers))


# =========================================================
# count()
# =========================================================

numbers = (10,20,10,30,10)

print(numbers.count(10))

# Output:
# 3


# =========================================================
# index()
# =========================================================

numbers = (10,20,30,40)

print(numbers.index(30))

# Output:
# 2


# =========================================================
# Summary Table
# =========================================================

"""
Function / Method        Purpose

len()                    Length

count()                  Count value

index()                  Position

min()                    Smallest value

max()                    Largest value

sum()                    Total
"""


# =========================================================
# END OF PART 1
# =========================================================