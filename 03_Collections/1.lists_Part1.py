"""
=========================================================
                    PYTHON LISTS
=========================================================

What is a List?
---------------
A List is a built-in Python data structure used to store
multiple items in a single variable.

A list can store:
- Integers
- Float
- Strings
- Boolean
- Lists
- Dictionaries
- Mixed Data Types

Syntax:
list_name = [item1, item2, item3]

Example:
fruits = ["Apple", "Banana", "Mango"]

=========================================================
FEATURES OF LIST
=========================================================

- Ordered
- Mutable (Can be Modified)
- Allows Duplicate Values
- Supports Indexing
- Supports Slicing
- Can Store Multiple Data Types
"""

# =========================================================
# Creating Lists
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']


# =========================================================
# List with Different Data Types
# =========================================================

student = [
    "Vinita",
    21,
    9.15,
    True
]

print(student)

# Output:
# ['Vinita', 21, 9.15, True]


# =========================================================
# Empty List
# =========================================================

numbers = []

print(numbers)

# Output:
# []


# =========================================================
# Creating List using list()
# =========================================================

letters = list("Python")

print(letters)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']


# =========================================================
# Length of List
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))

# Output:
# 3


# =========================================================
# Type of List
# =========================================================

print(type(fruits))

# Output:
# <class 'list'>


# =========================================================
# Indexing
# =========================================================

"""
Positive Index

Apple Banana Mango Orange

0      1      2      3
"""

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])

print(fruits[2])

# Output:
# Apple
# Mango


# =========================================================
# Negative Indexing
# =========================================================

"""
Negative Index

Apple Banana Mango Orange

-4     -3     -2    -1
"""

print(fruits[-1])

print(fruits[-2])

# Output:
# Orange
# Mango


# =========================================================
# List Slicing
# =========================================================

"""
Syntax:

list[start : stop : step]
"""

numbers = [10,20,30,40,50,60]

print(numbers[1:4])

# Output:
# [20,30,40]

print(numbers[:3])

# Output:
# [10,20,30]

print(numbers[2:])

# Output:
# [30,40,50,60]

print(numbers[:])

# Output:
# Entire List


# =========================================================
# Step Value
# =========================================================

print(numbers[::2])

# Output:
# [10,30,50]

print(numbers[::-1])

# Output:
# [60,50,40,30,20,10]


# =========================================================
# Updating List Elements
# =========================================================

fruits = ["Apple","Banana","Mango"]

print("Before Update")

print(fruits)

fruits[1] = "Orange"

print("After Update")

print(fruits)

# Output:
# ['Apple','Orange','Mango']


# =========================================================
# Updating Multiple Elements
# =========================================================

numbers = [10,20,30,40,50]

numbers[1:4] = [100,200,300]

print(numbers)

# Output:
# [10,100,200,300,50]


# =========================================================
# Adding Elements using append()
# =========================================================

"""
append()

Adds one element at the END of the list.
"""

fruits = ["Apple","Banana"]

fruits.append("Mango")

print(fruits)

# Output:
# ['Apple','Banana','Mango']


# =========================================================
# append() with Different Data Types
# =========================================================

data = [10,20]

data.append(True)

data.append("Python")

print(data)

# Output:
# [10,20,True,'Python']


# =========================================================
# insert()
# =========================================================

"""
insert(index, value)

Adds an element at a specified position.
"""

fruits = ["Apple","Banana","Mango"]

fruits.insert(1,"Orange")

print(fruits)

# Output:
# ['Apple','Orange','Banana','Mango']


# =========================================================
# extend()
# =========================================================

"""
extend()

Adds multiple elements.

Syntax:

list.extend(iterable)
"""

fruits = ["Apple","Banana"]

new_fruits = ["Mango","Orange"]

fruits.extend(new_fruits)

print(fruits)

# Output:
# ['Apple','Banana','Mango','Orange']


# =========================================================
# Difference Between append() and extend()
# =========================================================

list1 = [1,2]

list1.append([3,4])

print(list1)

# Output:
# [1,2,[3,4]]

list2 = [1,2]

list2.extend([3,4])

print(list2)

# Output:
# [1,2,3,4]


# =========================================================
# remove()
# =========================================================

"""
Removes the FIRST occurrence of a value.
"""

fruits = ["Apple","Banana","Apple","Mango"]

fruits.remove("Apple")

print(fruits)

# Output:
# ['Banana','Apple','Mango']


# =========================================================
# pop()
# =========================================================

"""
Removes element by INDEX.

Returns removed value.
"""

numbers = [10,20,30,40]

print(numbers.pop())

# Output:
# 40

print(numbers)

# Output:
# [10,20,30]

print(numbers.pop(1))

# Output:
# 20


# =========================================================
# del Keyword
# =========================================================

numbers = [10,20,30,40]

del numbers[2]

print(numbers)

# Output:
# [10,20,40]


# =========================================================
# clear()
# =========================================================

numbers = [1,2,3,4]

numbers.clear()

print(numbers)

# Output:
# []


# =========================================================
# Summary Table
# =========================================================

"""
Method          Purpose

append()        Add one item

extend()        Add multiple items

insert()        Add at index

remove()        Remove by value

pop()           Remove by index

del             Delete element

clear()         Remove all elements

len()           Length

type()          Data type
"""


# =========================================================
# END OF PART 1
# =========================================================