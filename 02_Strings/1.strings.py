"""
=========================================================
                    PYTHON STRINGS
=========================================================

What is a String?
-----------------
A String is a sequence of characters enclosed in:

• Single Quotes (' ')
• Double Quotes (" ")
• Triple Quotes (''' ''' or \"\"\" \"\"\")

Examples:

"Python"

'Hello'

'''This is a
multi-line string'''

Strings are one of the most commonly used data types in Python.

=========================================================
FEATURES OF STRINGS
=========================================================

✔ Ordered
✔ Immutable
✔ Supports Indexing
✔ Supports Slicing
✔ Allows Duplicate Characters
✔ Can store letters, numbers, and symbols


"""

# =========================================================
# Creating Strings
# =========================================================

name = "Vinita"

language = 'Python'

message = """Welcome to
Python Programming"""

print(name)

print(language)

print(message)


# =========================================================
# Type of String
# =========================================================

print(type(name))

# Output:
# <class 'str'>


# =========================================================
# Accessing Characters (Indexing)
# =========================================================

"""
Positive Index

P  y  t  h  o  n

0  1  2  3  4  5
"""

text = "Python"

print(text[0])

print(text[1])

print(text[5])

# Output:
# P
# y
# n


# =========================================================
# Negative Indexing
# =========================================================

"""
Negative Index

 P  y  t  h  o  n

-6 -5 -4 -3 -2 -1
"""

print(text[-1])

print(text[-2])

print(text[-6])

# Output:
# n
# o
# P


# =========================================================
# String Slicing
# =========================================================

"""
Syntax

string[start : stop : step]
"""

print(text[0:4])

# Output:
# Pyth

print(text[2:])

# Output:
# thon

print(text[:3])

# Output:
# Pyt

print(text[:])

# Output:
# Python


# =========================================================
# Step Value
# =========================================================

print(text[::2])

# Output:
# Pto

print(text[::-1])

# Output:
# nohtyP

# Reverse string


# =========================================================
# String Length
# =========================================================

print(len(text))

# Output:
# 6


# =========================================================
# Membership Operators
# =========================================================

print("Py" in text)

print("Java" in text)

print("Java" not in text)


# =========================================================
# Loop Through String
# =========================================================

for ch in text:

    print(ch)


# =========================================================
# Concatenation
# =========================================================

first = "Hello"

second = "World"

result = first + " " + second

print(result)

# Output:
# Hello World


# =========================================================
# Repetition
# =========================================================

print("=" * 40)

print("Python " * 3)

# Output:
# ========================================
# Python Python Python


# =========================================================
# Escape Characters
# =========================================================

print("Hello\nWorld")

print("Python\tProgramming")

print("He said \"Python is Easy\"")

print("C:\\Users\\Vinita")


# =========================================================
# Immutability
# =========================================================

"""
Strings cannot be modified.

Wrong

text[0] = "J"

Error

TypeError

Correct

Create a new string.
"""

text = "Python"

text = "J" + text[1:]

print(text)

# Output:
# Jython


# =========================================================
# String Comparison
# =========================================================

print("Apple" == "Apple")

print("Apple" == "apple")

print("Python" > "Java")

# Comparison is based on Unicode values.


# =========================================================
# ASCII / Unicode
# =========================================================

print(ord("A"))

print(ord("a"))

print(chr(65))

print(chr(97))

# Output:
# 65
# 97
# A
# a


# =========================================================
# Raw String
# =========================================================

path = r"C:\Users\Vinita\Python"

print(path)


# =========================================================
# Multi-line String
# =========================================================

paragraph = """
Python is
easy to learn.

It is used in

AI

Machine Learning

Web Development
"""

print(paragraph)


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a String?

Answer:
A sequence of characters enclosed in quotes.

------------------------------------------------

2. Are Strings mutable?

Answer:
No.

------------------------------------------------

3. Which function returns string length?

Answer:

len()

------------------------------------------------

4. What is indexing?

Answer:
Accessing characters using position.

------------------------------------------------

5. Difference between Positive and Negative Index?

Positive starts from 0.

Negative starts from -1.

------------------------------------------------

6. How do you reverse a string?

Answer:

text[::-1]

------------------------------------------------

7. What does len() return?

Answer:
Number of characters.

------------------------------------------------

8. Which operator concatenates strings?

Answer:
+

------------------------------------------------

9. Which operator repeats strings?

Answer:
*

------------------------------------------------

10. What is the output?

text = "Python"

print(text[-1])

Answer:
n
"""

# =========================================================
# END OF FILE
# =========================================================