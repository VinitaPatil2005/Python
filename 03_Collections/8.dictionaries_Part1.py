"""
=========================================================
                PYTHON DICTIONARIES
=========================================================

What is a Dictionary?
---------------------
A Dictionary is a built-in Python data structure used to
store data in the form of Key : Value pairs.

Unlike Lists, Dictionaries store data using keys instead
of indexes.

Syntax:

dictionary = {
    key1 : value1,
    key2 : value2
}

Example:

student = {
    "name": "Vinita",
    "age": 21,
    "cgpa": 9.15
}

=========================================================
FEATURES OF DICTIONARY
=========================================================

- Ordered (Python 3.7+)
- Mutable
- No Duplicate Keys
- Values can be duplicated
- Fast Searching
- Stores Different Data Types
"""

# =========================================================
# Creating Dictionary
# =========================================================

student = {
    "name": "Vinita",
    "age": 21,
    "cgpa": 9.15
}

print(student)

# Output:
# {'name': 'Vinita', 'age': 21, 'cgpa': 9.15}


# =========================================================
# Dictionary with Different Data Types
# =========================================================

employee = {
    "id":101,
    "name":"Rahul",
    "salary":50000,
    "is_manager":False,
    "skills":["Python","SQL"]
}

print(employee)


# =========================================================
# Empty Dictionary
# =========================================================

empty = {}

print(type(empty))

# Output:
# <class 'dict'>


# =========================================================
# Using dict() Constructor
# =========================================================

student = dict(
    name="Vinita",
    age=21,
    city="Pune"
)

print(student)


# =========================================================
# Length
# =========================================================

print(len(student))

# Output:
# 3


# =========================================================
# Accessing Values
# =========================================================

student = {
    "name":"Vinita",
    "age":21,
    "city":"Pune"
}

print(student["name"])

print(student["city"])

# Output:
# Vinita
# Pune


# =========================================================
# get()
# =========================================================

"""
Returns None if key is absent.

Does NOT raise KeyError.
"""

print(student.get("age"))

print(student.get("salary"))

# Output:
# 21
# None


# =========================================================
# Difference Between [] and get()
# =========================================================

"""
student["salary"]

Raises KeyError

student.get("salary")

Returns None
"""


# =========================================================
# Updating Values
# =========================================================

student["age"] = 22

print(student)


# =========================================================
# Adding New Key
# =========================================================

student["branch"] = "AIML"

print(student)


# =========================================================
# update()
# =========================================================

student.update({
    "cgpa":9.15,
    "city":"Mumbai"
})

print(student)


# =========================================================
# Removing Items using pop()
# =========================================================

student.pop("city")

print(student)


# =========================================================
# popitem()
# =========================================================

"""
Removes the LAST inserted item.
"""

student.popitem()

print(student)


# =========================================================
# del Keyword
# =========================================================

student = {
    "name":"Vinita",
    "age":21
}

del student["age"]

print(student)


# =========================================================
# clear()
# =========================================================

student.clear()

print(student)

# Output:
# {}


# =========================================================
# Copy Dictionary
# =========================================================

student = {
    "name":"Vinita",
    "age":21
}

copy_student = student.copy()

print(copy_student)


# =========================================================
# Membership Operators
# =========================================================

student = {
    "name":"Vinita",
    "age":21
}

print("name" in student)

print("salary" not in student)

# Checks KEYS only.


# =========================================================
# Traversing Dictionary
# =========================================================

student = {
    "name":"Vinita",
    "age":21,
    "city":"Pune"
}

for key in student:
    print(key)

print()

for key in student:
    print(key, student[key])


# =========================================================
# Summary Table
# =========================================================

"""
Method              Purpose

get()               Safe access

update()            Update values

pop()               Remove by key

popitem()           Remove last item

clear()             Remove all

copy()              Copy dictionary

len()               Number of items
"""


# =========================================================
# END OF PART 1
# =========================================================