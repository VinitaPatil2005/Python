"""
=========================================================
            PYTHON STRING METHODS (PART 1)
=========================================================

What are String Methods?
------------------------
String methods are built-in functions that perform various
operations on strings.

Syntax:
string.method()

Example:
name = "python"

print(name.upper())

Output:
PYTHON

NOTE:
Strings are immutable.
Every string method returns a NEW string.
The original string remains unchanged unless reassigned.
"""

# =========================================================
# upper()
# =========================================================

"""
Converts all characters into UPPERCASE.
"""

text = "python programming"

print(text.upper())

# Output:
# PYTHON PROGRAMMING


# =========================================================
# lower()
# =========================================================

"""
Converts all characters into lowercase.
"""

text = "PYTHON"

print(text.lower())

# Output:
# python


# =========================================================
# capitalize()
# =========================================================

"""
Converts only the first letter to uppercase.
"""

text = "python programming"

print(text.capitalize())

# Output:
# Python programming


# =========================================================
# title()
# =========================================================

"""
Converts the first letter of every word into uppercase.
"""

text = "python programming language"

print(text.title())

# Output:
# Python Programming Language


# =========================================================
# swapcase()
# =========================================================

"""
Converts uppercase to lowercase and vice versa.
"""

text = "PyThOn"

print(text.swapcase())

# Output:
# pYtHoN


# =========================================================
# casefold()
# =========================================================

"""
Similar to lower() but more aggressive.

Used for case-insensitive comparisons.
"""

text = "PYTHON"

print(text.casefold())

# Output:
# python


# =========================================================
# strip()
# =========================================================

"""
Removes spaces from both sides.
"""

text = "   Python   "

print(text.strip())

# Output:
# Python


# =========================================================
# lstrip()
# =========================================================

"""
Removes spaces from the left side.
"""

text = "     Python"

print(text.lstrip())

# Output:
# Python


# =========================================================
# rstrip()
# =========================================================

"""
Removes spaces from the right side.
"""

text = "Python     "

print(text.rstrip())

# Output:
# Python


# =========================================================
# replace()
# =========================================================

"""
Replaces one string with another.

Syntax:

replace(old, new)
"""

text = "I like Java"

print(text.replace("Java", "Python"))

# Output:
# I like Python


# =========================================================
# replace() with Count
# =========================================================

text = "apple apple apple"

print(text.replace("apple", "mango", 2))

# Output:
# mango mango apple


# =========================================================
# find()
# =========================================================

"""
Returns the first occurrence.

Returns -1 if not found.
"""

text = "Python Programming"

print(text.find("Program"))

print(text.find("Java"))

# Output:
# 7
# -1


# =========================================================
# index()
# =========================================================

"""
Similar to find().

Difference:

find() -> returns -1

index() -> raises ValueError
"""

text = "Python"

print(text.index("t"))

# print(text.index("z"))

# ValueError


# =========================================================
# rfind()
# =========================================================

"""
Returns last occurrence.
"""

text = "apple mango apple"

print(text.rfind("apple"))

# Output:
# 12


# =========================================================
# rindex()
# =========================================================

"""
Returns last occurrence.

Raises ValueError if not found.
"""

text = "apple mango apple"

print(text.rindex("apple"))


# =========================================================
# count()
# =========================================================

"""
Counts number of occurrences.
"""

text = "banana"

print(text.count("a"))

# Output:
# 3


# =========================================================
# startswith()
# =========================================================

"""
Checks beginning of string.

Returns True or False.
"""

text = "Python Programming"

print(text.startswith("Python"))

print(text.startswith("Java"))

# Output:
# True
# False


# =========================================================
# endswith()
# =========================================================

"""
Checks end of string.
"""

text = "report.pdf"

print(text.endswith(".pdf"))

print(text.endswith(".txt"))

# Output:
# True
# False


# =========================================================
# split()
# =========================================================

"""
Converts string into list.

Default separator is space.
"""

text = "Python Java C++"

print(text.split())

# Output:
# ['Python', 'Java', 'C++']


# =========================================================
# split() with Separator
# =========================================================

text = "Apple,Mango,Grapes"

print(text.split(","))

# Output:
# ['Apple', 'Mango', 'Grapes']


# =========================================================
# split() with maxsplit
# =========================================================

text = "Python Java C C++"

print(text.split(" ", 2))

# Output:
# ['Python', 'Java', 'C C++']


# =========================================================
# join()
# =========================================================

"""
Joins iterable elements into one string.
"""

languages = ["Python", "Java", "C++"]

print(" | ".join(languages))

# Output:
# Python | Java | C++


# =========================================================
# partition()
# =========================================================

"""
Splits string into three parts.

(before, separator, after)
"""

text = "python@gmail.com"

print(text.partition("@"))

# Output:
# ('python', '@', 'gmail.com')


# =========================================================
# rpartition()
# =========================================================

"""
Splits from right side.
"""

text = "folder/subfolder/file.txt"

print(text.rpartition("/"))


# =========================================================
# splitlines()
# =========================================================

"""
Splits string at newline characters.
"""

text = "Python\nJava\nC++"

print(text.splitlines())

# Output:
# ['Python', 'Java', 'C++']


# =========================================================
# Summary Table
# =========================================================

"""
Method          Purpose

upper()         Uppercase

lower()         Lowercase

capitalize()    First letter uppercase

title()         Every word uppercase

swapcase()      Reverse cases

strip()         Remove spaces

replace()       Replace text

find()          Find substring

index()         Find substring

count()         Count occurrences

split()         Convert to list

join()          Join list

startswith()    Check beginning

endswith()      Check ending

partition()     Split into 3 parts

splitlines()    Split lines
"""


# =========================================================
# END OF PART 1
# =========================================================