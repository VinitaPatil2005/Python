# =========================================================
#            PYTHON STRING METHODS (PART 2)
# =========================================================

# =========================================================
# isalpha()
# =========================================================

"""
Returns True if all characters are alphabets.

Spaces, numbers and symbols are not allowed.
"""

text = "Python"

print(text.isalpha())

# Output:
# True

text = "Python3"

print(text.isalpha())

# Output:
# False


# =========================================================
# isdigit()
# =========================================================

"""
Returns True if all characters are digits (0-9).
"""

number = "12345"

print(number.isdigit())

# Output:
# True

number = "12a45"

print(number.isdigit())

# Output:
# False


# =========================================================
# isdecimal()
# =========================================================

"""
Returns True if all characters are decimal numbers.

Similar to isdigit() but slightly stricter.
"""

text = "12345"

print(text.isdecimal())

# Output:
# True


# =========================================================
# isnumeric()
# =========================================================

"""
Returns True if all characters are numeric.

Accepts more numeric characters than isdigit().
"""

text = "12345"

print(text.isnumeric())

# Output:
# True


# =========================================================
# isalnum()
# =========================================================

"""
Returns True if the string contains only
letters and numbers.

No spaces or special symbols allowed.
"""

text = "Python123"

print(text.isalnum())

# Output:
# True

text = "Python 123"

print(text.isalnum())

# Output:
# False


# =========================================================
# islower()
# =========================================================

"""
Checks whether all letters are lowercase.
"""

text = "python"

print(text.islower())

# Output:
# True

text = "Python"

print(text.islower())

# Output:
# False


# =========================================================
# isupper()
# =========================================================

"""
Checks whether all letters are uppercase.
"""

text = "PYTHON"

print(text.isupper())

# Output:
# True

text = "Python"

print(text.isupper())

# Output:
# False


# =========================================================
# istitle()
# =========================================================

"""
Checks whether every word starts with
a capital letter.
"""

text = "Python Programming"

print(text.istitle())

# Output:
# True

text = "python Programming"

print(text.istitle())

# Output:
# False


# =========================================================
# isspace()
# =========================================================

"""
Returns True if the string contains only spaces.
"""

text = "     "

print(text.isspace())

# Output:
# True

text = "Python"

print(text.isspace())

# Output:
# False


# =========================================================
# isidentifier()
# =========================================================

"""
Checks whether a string is a valid Python identifier.
"""

text = "student_name"

print(text.isidentifier())

# Output:
# True

text = "123student"

print(text.isidentifier())

# Output:
# False


# =========================================================
# isascii()
# =========================================================

"""
Returns True if every character belongs
to the ASCII character set.
"""

text = "Python"

print(text.isascii())

# Output:
# True


# =========================================================
# isprintable()
# =========================================================

"""
Returns True if all characters are printable.
"""

text = "Hello"

print(text.isprintable())

# Output:
# True


# =========================================================
# center()
# =========================================================

"""
Centers a string within the specified width.
"""

text = "Python"

print(text.center(20))

print(text.center(20, "*"))

# Output:
#        Python
# *******Python*******


# =========================================================
# ljust()
# =========================================================

"""
Left aligns the string.
"""

text = "Python"

print(text.ljust(15, "-"))

# Output:
# Python---------


# =========================================================
# rjust()
# =========================================================

"""
Right aligns the string.
"""

print(text.rjust(15, "-"))

# Output:
# ---------Python


# =========================================================
# zfill()
# =========================================================

"""
Adds zeros to the left until
the specified length is reached.
"""

number = "45"

print(number.zfill(5))

# Output:
# 00045


# =========================================================
# expandtabs()
# =========================================================

"""
Replaces tab characters with spaces.
"""

text = "Python\tProgramming"

print(text.expandtabs(10))


# =========================================================
# encode()
# =========================================================

"""
Converts a string into bytes.
"""

text = "Python"

print(text.encode())

# Output:
# b'Python'


# =========================================================
# format()
# =========================================================

"""
Formats strings using placeholders.
"""

name = "Vinita"
age = 21

print("My name is {} and I am {} years old.".format(name, age))

# Output:
# My name is Vinita and I am 21 years old.


# =========================================================
# format() with Index
# =========================================================

print("{1} is learning {0}".format("Python", "Vinita"))

# Output:
# Vinita is learning Python


# =========================================================
# format_map()
# =========================================================

"""
Uses a dictionary for formatting.
"""

student = {
    "name": "Vinita",
    "city": "Pune"
}

print("Name: {name}, City: {city}".format_map(student))

# Output:
# Name: Vinita, City: Pune


# =========================================================
# maketrans() and translate()
# =========================================================

"""
translate() replaces characters
using a translation table.
"""

table = str.maketrans("aeiou", "12345")

text = "education"

print(text.translate(table))

# Output:
# 2d5c1t34n


# =========================================================
# INTERVIEW QUESTIONS
# =========================================================

"""
1. Difference between lower() and casefold()?

Answer:
casefold() is stronger and mainly used
for case-insensitive comparisons.

------------------------------------------------

2. Difference between find() and index()?

find()

Returns -1 if not found.

index()

Raises ValueError if not found.

------------------------------------------------

3. Which method joins a list into a string?

Answer:

join()

------------------------------------------------

4. Which method removes spaces?

Answer:

strip()

------------------------------------------------

5. Which method checks whether a string
contains only alphabets?

Answer:

isalpha()

------------------------------------------------

6. Which method checks only digits?

Answer:

isdigit()

------------------------------------------------

7. Which method checks valid Python identifiers?

Answer:

isidentifier()

------------------------------------------------

8. Which method converts text into uppercase?

Answer:

upper()

------------------------------------------------

9. Which method replaces text?

Answer:

replace()

------------------------------------------------

10. Which method converts a string into bytes?

Answer:

encode()
"""

# =========================================================
# END OF string_methods.py
# =========================================================