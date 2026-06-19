"""
=========================================================
                PYTHON DATA TYPES 
=========================================================

What is a Data Type?
--------------------
A data type specifies the type of value a variable can store.
Python automatically identifies the data type based on the assigned value,
so Python is called a Dynamically Typed Language.

Example:
"""

x = 10          # int
y = 10.5        # float
name = "Vinita" # str

print(type(x))
print(type(y))
print(type(name))

# =========================================================
# 1. NUMERIC DATA TYPES
# =========================================================

"""
Python provides three numeric data types:

1. int
2. float
3. complex
"""

# ---------------------------------------------------------
# int (Integer)
# ---------------------------------------------------------

"""
Stores whole numbers (positive, negative or zero).

Syntax:
variable = integer

Examples:
"""

a = 100
b = -50
c = 0

print(a)
print(type(a))

# Features:
# • No decimal point
# • Unlimited size in Python
# • Immutable (cannot be modified)


# ---------------------------------------------------------
# float (Floating Point)
# ---------------------------------------------------------

"""
Stores decimal numbers.

Syntax:
variable = decimal_number

Examples:
"""

price = 99.99
temperature = -15.5

print(price)
print(type(price))

# Features:
# • Contains decimal point
# • Can also store scientific notation

num = 5e3      # 5 × 10³ = 5000
print(num)


# ---------------------------------------------------------
# complex
# ---------------------------------------------------------

"""
Stores complex numbers.

Syntax:
a + bj

where j represents the imaginary part.

Example:
"""

z = 4 + 5j

print(z)
print(type(z))

# =========================================================
# 2. STRING (str)
# =========================================================

"""
A string is a collection of characters enclosed in
single quotes (' ')
double quotes (" ")
or triple quotes (''' ''' or """ """)

Strings are Immutable.
"""

name = "Python"

print(name)
print(type(name))

# Accessing characters

print(name[0])
print(name[2])

# Negative indexing

print(name[-1])

# String slicing

print(name[0:4])
print(name[:3])
print(name[2:])

# String methods

print(name.upper())
print(name.lower())
print(name.replace("Py", "My"))
print(len(name))

# =========================================================
# 3. BOOLEAN (bool)
# =========================================================

"""
Boolean data type has only two values:

True
False

Mostly used in conditions.
"""

is_student = True
is_admin = False

print(type(is_student))

print(10 > 5)
print(10 == 5)

# =========================================================
# 4. LIST
# =========================================================

"""
A List is an ordered collection.

Properties:
-----------
- Ordered
- Mutable
- Allows duplicates
- Indexed
- Can store multiple data types
"""

fruits = ["Apple", "Banana", "Mango"]

print(type(fruits))


# =========================================================
# 5. TUPLE
# =========================================================

"""
Tuple is similar to List but Immutable.

Properties:
-----------
 - Ordered
 - Immutable
 - Allows duplicates
 - Faster than List
"""

colors = ("Red", "Green", "Blue")

print(type(colors))

print(colors[0])

# Cannot modify

# colors[0] = "Black"     # Error

# =========================================================
# 6. SET
# =========================================================

"""
A Set stores unique values.

Properties:
-----------
 - Unordered
 - Mutable
 - No duplicate values
 - No indexing
"""

numbers = {1, 2, 3, 4, 4, 5}

print(numbers)

# Duplicate values are automatically removed.


# =========================================================
# 7. DICTIONARY
# =========================================================

"""
Dictionary stores data in Key : Value pairs.

Properties:
-----------
 - Ordered (Python 3.7+)
 - Mutable
 - Keys must be unique
 - Values can repeat
"""

student = {
    "name": "Vinita",
    "age": 21,
    "CGPA": 9.15
}

print(type(student))


# =========================================================
# 8. NONE TYPE
# =========================================================

"""
None represents the absence of a value.

Useful when a variable has no value yet.
"""

x = None

print(type(x))

# =========================================================
# TYPE CONVERSION (TYPE CASTING)
# =========================================================

"""
Converting one data type into another.
"""

a = "100"

print(type(a))

b = int(a)

print(type(b))

c = float(b)

print(type(c))

d = str(c)

print(type(d))

# =========================================================
# MUTABLE vs IMMUTABLE
# =========================================================

"""
Mutable
-------
Can be modified after creation.

Examples:
List
Dictionary
Set

Immutable
---------
Cannot be modified.

Examples:
Integer
Float
Boolean
String
Tuple
Complex
"""

# =========================================================
# SUMMARY TABLE
# =========================================================

"""
Data Type    Ordered    Mutable    Duplicate    Example
---------------------------------------------------------------
int          No         No         No           100
float        No         No         No           25.5
complex      No         No         No           3+4j
str          Yes        No         Yes          "Python"
list         Yes        Yes        Yes          [1,2,3]
tuple        Yes        No         Yes          (1,2,3)
set          No         Yes        No           {1,2,3}
dict         Yes        Yes        Keys No      {"a":1}
bool         No         No         No           True
NoneType     No         No         No           None
"""

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================

"""
1. What is a data type?

2. Difference between List and Tuple?

3. Difference between Set and Dictionary?

4. What is Mutable and Immutable?

5. Difference between == and is?

6. How do you check a variable's data type?

Answer:
type(variable)

7. How do you convert String into Integer?

int("100")

8. Which data type stores key-value pairs?

Dictionary

9. Which data type removes duplicates automatically?

Set

10. Which data type is used to represent no value?

NoneType
"""

# =========================================================
# END OF FILE
# =========================================================