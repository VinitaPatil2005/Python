"""
=========================================================
                PYTHON TYPE CASTING
=========================================================

What is Type Casting?
---------------------
Type Casting means converting one data type into another.

Example:
String -> Integer
Integer -> Float
Float -> String

Python provides built-in functions for type conversion.

These functions are:
1. int()
2. float()
3. str()
4. bool()
5. list()
6. tuple()
7. set()
8. dict()

=========================================================
WHY TYPE CASTING IS REQUIRED?
=========================================================

Sometimes data received from users, files, or databases is
in the wrong format.

Example:
User enters age as "21" (String)

To perform mathematical operations, convert it into Integer.

"""

# =========================================================
# CHECKING DATA TYPE
# =========================================================

x = "100"

print(x)
print(type(x))

# Output:
# 100
# <class 'str'>


# =========================================================
# IMPLICIT TYPE CASTING
# =========================================================

"""
Implicit Type Casting is performed automatically by Python.

Python converts a smaller data type into a larger data type
to avoid data loss.
"""

a = 10        # int
b = 2.5       # float

result = a + b

print(result)
print(type(result))

# Output:
# 12.5
# <class 'float'>


# =========================================================
# EXPLICIT TYPE CASTING
# =========================================================

"""
Explicit Type Casting is performed manually by the programmer.

Syntax:

datatype(variable)
"""

num = "50"

print(type(num))

num = int(num)

print(type(num))

# Output:
# <class 'int'>


# =========================================================
# int()
# =========================================================

"""
Converts values into Integer.

Syntax:
int(value)
"""

print(int(10.99))

# Output:
# 10

print(int(True))

# Output:
# 1

print(int(False))

# Output:
# 0

print(int("200"))

# Output:
# 200


# =========================================================
# Invalid Conversion
# =========================================================

# print(int("Hello"))

# ValueError
# Because "Hello" is not a valid number.


# =========================================================
# float()
# =========================================================

"""
Converts values into Float.
"""

print(float(25))

# Output:
# 25.0

print(float("15.75"))

# Output:
# 15.75

print(float(True))

# Output:
# 1.0


# =========================================================
# str()
# =========================================================

"""
Converts values into String.
"""

age = 21

print(type(age))

age = str(age)

print(type(age))

print(age)

# Output:
# <class 'str'>


# =========================================================
# bool()
# =========================================================

"""
Converts values into Boolean.

Rules:

0 -> False

None -> False

Empty String -> False

Empty List -> False

Everything else -> True
"""

print(bool(10))

print(bool(0))

print(bool("Python"))

print(bool(""))

print(bool([]))

print(bool([1, 2]))

print(bool(None))

# Output:
# True
# False
# True
# False
# False
# True
# False


# =========================================================
# list()
# =========================================================

"""
Converts iterable objects into List.
"""

text = "Python"

print(list(text))

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']

numbers = (1, 2, 3)

print(list(numbers))

# Output:
# [1, 2, 3]


# =========================================================
# tuple()
# =========================================================

"""
Converts iterable objects into Tuple.
"""

numbers = [10, 20, 30]

print(tuple(numbers))

# Output:
# (10, 20, 30)


# =========================================================
# set()
# =========================================================

"""
Converts iterable objects into Set.

Duplicate values are removed.
"""

numbers = [1, 2, 2, 3, 4, 4]

print(set(numbers))

# Output:
# {1,2,3,4}


# =========================================================
# dict()
# =========================================================

"""
Creates a dictionary from key-value pairs.
"""

pairs = [
    ("Name", "Vinita"),
    ("Age", 21),
    ("City", "Pune")
]

student = dict(pairs)

print(student)

# Output:
# {'Name':'Vinita', 'Age':21, 'City':'Pune'}


# =========================================================
# STRING TO INTEGER
# =========================================================

marks = "95"

marks = int(marks)

print(marks + 5)

# Output:
# 100


# =========================================================
# INTEGER TO STRING
# =========================================================

roll_no = 101

roll_no = str(roll_no)

print("Roll Number :", roll_no)

# Output:
# Roll Number : 101


# =========================================================
# INTEGER TO FLOAT
# =========================================================

salary = 50000

salary = float(salary)

print(salary)

# Output:
# 50000.0


# =========================================================
# FLOAT TO INTEGER
# =========================================================

pi = 3.14159

print(int(pi))

# Output:
# 3

# Decimal part is removed (not rounded).


# =========================================================
# INTERVIEW QUESTIONS
# =========================================================

"""
1. What is Type Casting?

Answer:
Converting one data type into another.

---------------------------------------------------

2. What are the two types of Type Casting?

Answer:

Implicit

Explicit

---------------------------------------------------

3. Difference between Implicit and Explicit?

Implicit
--------
Done automatically by Python.

Explicit
--------
Done manually by programmer.

---------------------------------------------------

4. Which function converts String into Integer?

Answer:

int()

---------------------------------------------------

5. Which function converts Integer into Float?

Answer:

float()

---------------------------------------------------

6. What happens when we execute

int("Hello")

Answer:

ValueError

---------------------------------------------------

7. What is the output?

print(int(10.99))

Answer:
10

---------------------------------------------------

8. What is the output?

bool(0)

Answer:
False

---------------------------------------------------

9. What is the output?

bool("")

Answer:
False

---------------------------------------------------

10. Does int() round numbers?

Answer:
No.

It removes the decimal part.

Example:

int(9.99)

Output:
9
"""

# =========================================================
# END OF FILE
# =========================================================