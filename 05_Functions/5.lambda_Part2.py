# =========================================================
#          PYTHON LAMBDA FUNCTIONS (PART 2)
# =========================================================

from functools import reduce

# =========================================================
# map() with Multiple Lists
# =========================================================

"""
map() can process multiple iterables simultaneously.
"""

list1 = [10, 20, 30]
list2 = [1, 2, 3]

result = list(
    map(lambda x, y: x + y, list1, list2)
)

print(result)

# Output
# [11, 22, 33]


# =========================================================
# Convert Celsius to Fahrenheit
# =========================================================

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(
    map(lambda c: (c * 9/5) + 32, celsius)
)

print(fahrenheit)


# =========================================================
# String Length
# =========================================================

words = ["Python", "Java", "SQL", "Machine Learning"]

lengths = list(
    map(lambda word: len(word), words)
)

print(lengths)


# =========================================================
# Convert Strings to Uppercase
# =========================================================

languages = ["python", "java", "c++"]

upper = list(
    map(lambda lang: lang.upper(), languages)
)

print(upper)


# =========================================================
# filter() Positive Numbers
# =========================================================

numbers = [-5, 10, -2, 15, 0, 20]

positive = list(
    filter(lambda x: x > 0, numbers)
)

print(positive)


# =========================================================
# filter() Odd Numbers
# =========================================================

numbers = [1,2,3,4,5,6,7,8,9,10]

odd = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print(odd)


# =========================================================
# Filter Long Words
# =========================================================

words = ["AI", "Python", "Machine", "ML", "Programming"]

long_words = list(
    filter(lambda word: len(word) > 5, words)
)

print(long_words)


# =========================================================
# reduce() Find Maximum
# =========================================================

numbers = [5, 9, 3, 12, 8]

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print(largest)


# =========================================================
# reduce() Find Minimum
# =========================================================

smallest = reduce(
    lambda a, b: a if a < b else b,
    numbers
)

print(smallest)


# =========================================================
# Sorting Dictionary
# =========================================================

students = [

    {"name": "Vinita", "marks": 90},

    {"name": "Rahul", "marks": 82},

    {"name": "Amit", "marks": 95},

    {"name": "Sneha", "marks": 88}

]

students.sort(
    key=lambda student: student["marks"]
)

print(students)


# =========================================================
# Sort by Name
# =========================================================

students.sort(
    key=lambda student: student["name"]
)

print(students)


# =========================================================
# Multiple Key Sorting
# =========================================================

employees = [

    ("Rahul", 50000),

    ("Vinita", 70000),

    ("Amit", 70000),

    ("Sneha", 45000)

]

employees.sort(
    key=lambda employee: (employee[1], employee[0])
)

print(employees)


# =========================================================
# Nested Lambda
# =========================================================

multiply = lambda x: lambda y: x * y

double = multiply(2)

triple = multiply(3)

print(double(10))

print(triple(10))


# =========================================================
# any()
# =========================================================

numbers = [0, 0, 5, 0]

print(any(numbers))

# Output
# True


# =========================================================
# all()
# =========================================================

numbers = [1,2,3,4]

print(all(numbers))

# Output
# True


# =========================================================
# Data Science Example
# =========================================================

marks = [95, 82, 67, 91, 58]

grades = list(

    map(

        lambda mark:

        "Pass" if mark >= 35 else "Fail",

        marks

    )

)

print(grades)


# =========================================================
# Chaining map() and filter()
# =========================================================

numbers = [1,2,3,4,5,6,7,8,9,10]

result = list(

    map(

        lambda x: x ** 2,

        filter(

            lambda x: x % 2 == 0,

            numbers

        )

    )

)

print(result)

# Output
# [4,16,36,64,100]


# =========================================================
# Lambda with sorted()
# =========================================================

cities = [

    "Pune",

    "Mumbai",

    "Delhi",

    "Bangalore"

]

sorted_cities = sorted(

    cities,

    key=lambda city: len(city)

)

print(sorted_cities)


# =========================================================
# Summary Table
# =========================================================

"""
Function                    Purpose

map()                       Modify every element

filter()                    Select matching elements

reduce()                    Produce one value

any()                       At least one True

all()                       All True

sorted()                    Custom sorting

Nested Lambda               Lambda returning lambda
"""


# =========================================================
# END OF PART 2
# =========================================================