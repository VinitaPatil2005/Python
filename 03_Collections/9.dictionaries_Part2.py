# =========================================================
#          PYTHON DICTIONARIES (PART 2)
# =========================================================

# =========================================================
# keys()
# =========================================================

"""
Returns all keys of the dictionary.

Return Type:
dict_keys
"""

student = {
    "name": "Vinita",
    "age": 21,
    "city": "Pune"
}

print(student.keys())

# Output:
# dict_keys(['name', 'age', 'city'])


# =========================================================
# values()
# =========================================================

"""
Returns all values.
"""

print(student.values())

# Output:
# dict_values(['Vinita', 21, 'Pune'])


# =========================================================
# items()
# =========================================================

"""
Returns key-value pairs as tuples.
"""

print(student.items())

# Output:
# dict_items([('name','Vinita'),
#             ('age',21),
#             ('city','Pune')])


# =========================================================
# Loop Through Keys
# =========================================================

for key in student.keys():

    print(key)


# =========================================================
# Loop Through Values
# =========================================================

for value in student.values():

    print(value)


# =========================================================
# Loop Through Key-Value Pairs
# =========================================================

for key, value in student.items():

    print(key, ":", value)


# =========================================================
# Nested Dictionary
# =========================================================

students = {

    "student1": {
        "name": "Vinita",
        "marks": 90
    },

    "student2": {
        "name": "Rahul",
        "marks": 85
    },

    "student3": {
        "name": "Amit",
        "marks": 95
    }

}

print(students)

print(students["student1"])

print(students["student2"]["name"])

print(students["student3"]["marks"])

# Output:
# Rahul
# 95


# =========================================================
# Traversing Nested Dictionary
# =========================================================

for student, details in students.items():

    print(student)

    for key, value in details.items():

        print(key, ":", value)

    print()


# =========================================================
# Dictionary of Lists
# =========================================================

student = {

    "name": "Vinita",

    "subjects": [
        "Python",
        "Java",
        "SQL"
    ]

}

print(student)

print(student["subjects"])

print(student["subjects"][1])

# Output:
# Java


# =========================================================
# List of Dictionaries
# =========================================================

employees = [

    {
        "id": 101,
        "name": "Rahul"
    },

    {
        "id": 102,
        "name": "Amit"
    },

    {
        "id": 103,
        "name": "Vinita"
    }

]

print(employees)

print(employees[0]["name"])

print(employees[2]["id"])


# =========================================================
# Traversing List of Dictionaries
# =========================================================

for emp in employees:

    print(emp["id"], emp["name"])


# =========================================================
# setdefault()
# =========================================================

"""
Returns the value of a key.

If the key does not exist,
it inserts the key with the default value.
"""

student = {

    "name": "Vinita"

}

print(student.setdefault("city", "Pune"))

print(student)

# Output:
# Pune
# {'name':'Vinita','city':'Pune'}


# =========================================================
# fromkeys()
# =========================================================

"""
Creates a new dictionary with specified keys.
"""

keys = ("Python", "Java", "SQL")

marks = 0

subjects = dict.fromkeys(keys, marks)

print(subjects)

# Output:
# {'Python':0,'Java':0,'SQL':0}


# =========================================================
# Dictionary Comprehension
# =========================================================

"""
Syntax

{key:value for item in iterable}
"""

numbers = [1,2,3,4,5]

square = {

    num: num**2

    for num in numbers

}

print(square)

# Output:
# {1:1,2:4,3:9,4:16,5:25}


# =========================================================
# Dictionary Comprehension with Condition
# =========================================================

numbers = range(1,11)

even_square = {

    num: num**2

    for num in numbers

    if num % 2 == 0

}

print(even_square)


# =========================================================
# Merge Dictionaries
# =========================================================

student = {

    "name":"Vinita"

}

details = {

    "city":"Pune",

    "cgpa":9.15

}

student.update(details)

print(student)


# =========================================================
# Using | Operator (Python 3.9+)
# =========================================================

dict1 = {

    "A":1,

    "B":2

}

dict2 = {

    "C":3,

    "D":4

}

result = dict1 | dict2

print(result)


# =========================================================
# Sorting Dictionary Keys
# =========================================================

student = {

    "city":"Pune",

    "name":"Vinita",

    "age":21

}

for key in sorted(student):

    print(key, student[key])


# =========================================================
# Summary Table
# =========================================================

"""
Method                  Purpose

keys()                  All keys

values()                All values

items()                 Key-value pairs

setdefault()            Insert default value

fromkeys()              Create dictionary

update()                Merge dictionaries

sorted()                Sort keys

Dictionary Comprehension
                        Create dictionary quickly
"""


# =========================================================
# END OF PART 2
# =========================================================