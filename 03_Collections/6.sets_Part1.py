"""
=========================================================
                    PYTHON SETS
=========================================================

What is a Set?
--------------
A Set is a built-in Python data structure used to store
multiple unique values in a single variable.

Unlike Lists and Tuples, Sets do not maintain order.

Syntax:

set_name = {value1, value2, value3}

Example:

fruits = {"Apple", "Banana", "Mango"}

=========================================================
FEATURES OF SET
=========================================================

- Unordered
- Mutable
- No Duplicate Values
- Unindexed
- Faster Searching
- Stores Different Data Types
"""

# =========================================================
# Creating Sets
# =========================================================

fruits = {"Apple", "Banana", "Mango"}

print(fruits)

# Output:
# {'Apple', 'Banana', 'Mango'}


# =========================================================
# Set with Different Data Types
# =========================================================

student = {
    "Vinita",
    21,
    9.15,
    True
}

print(student)


# =========================================================
# Empty Set
# =========================================================

"""
Do NOT use {}

{} creates an empty dictionary.

Use set()
"""

empty = set()

print(type(empty))

# Output:
# <class 'set'>


# =========================================================
# Duplicate Values
# =========================================================

numbers = {10,20,30,20,10,40}

print(numbers)

# Output:
# {10,20,30,40}


# =========================================================
# Length
# =========================================================

print(len(numbers))


# =========================================================
# Type
# =========================================================

print(type(numbers))


# =========================================================
# Loop Through Set
# =========================================================

for value in numbers:
    print(value)


# =========================================================
# Membership Operators
# =========================================================

print(20 in numbers)

print(100 not in numbers)


# =========================================================
# add()
# =========================================================

"""
Adds one element.
"""

numbers = {10,20,30}

numbers.add(40)

print(numbers)


# =========================================================
# update()
# =========================================================

"""
Adds multiple elements.
"""

numbers.update([50,60])

print(numbers)


# =========================================================
# remove()
# =========================================================

"""
Removes an element.

Raises KeyError if value is absent.
"""

numbers.remove(20)

print(numbers)

# numbers.remove(100)


# =========================================================
# discard()
# =========================================================

"""
Removes an element.

Does NOT raise an error if value is absent.
"""

numbers.discard(100)

print(numbers)


# =========================================================
# pop()
# =========================================================

"""
Removes a random element.

Since sets are unordered,
the removed value is unpredictable.
"""

value = numbers.pop()

print(value)

print(numbers)


# =========================================================
# clear()
# =========================================================

numbers.clear()

print(numbers)

# Output:
# set()


# =========================================================
# copy()
# =========================================================

set1 = {1,2,3}

set2 = set1.copy()

print(set2)


# =========================================================
# Convert List to Set
# =========================================================

numbers = [10,20,20,30,30]

unique = set(numbers)

print(unique)

# Output:
# {10,20,30}


# =========================================================
# Convert Set to List
# =========================================================

numbers = {10,20,30}

print(list(numbers))


# =========================================================
# Summary Table
# =========================================================

"""
Method          Purpose

add()           Add one item

update()        Add multiple items

remove()        Remove value

discard()       Remove safely

pop()           Remove random item

clear()         Remove all items

copy()          Create copy
"""


# =========================================================
# END OF PART 1
# =========================================================