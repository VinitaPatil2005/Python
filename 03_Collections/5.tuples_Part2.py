# =========================================================
#              PYTHON TUPLES (PART 2)
# =========================================================

# =========================================================
# Tuple Packing
# =========================================================

"""
Packing means storing multiple values into one tuple.
"""

student = ("Vinita", 21, "AIML", 9.15)

print(student)

# Output:
# ('Vinita', 21, 'AIML', 9.15)


# =========================================================
# Tuple Unpacking
# =========================================================

"""
Unpacking means assigning tuple values
to multiple variables.
"""

name, age, branch, cgpa = student

print(name)
print(age)
print(branch)
print(cgpa)


# =========================================================
# Using * Operator
# =========================================================

numbers = (10,20,30,40,50)

a, *b, c = numbers

print(a)

print(b)

print(c)

# Output:
# 10
# [20,30,40]
# 50


# =========================================================
# Nested Tuples
# =========================================================

students = (
    ("Vinita", 90),
    ("Rahul", 85),
    ("Amit", 95)
)

print(students)

print(students[0])

print(students[0][0])

print(students[2][1])

# Output:
# Vinita
# 95


# =========================================================
# Traversing Nested Tuples
# =========================================================

for student in students:
    print(student)

print()

for name, marks in students:
    print(name, marks)


# =========================================================
# enumerate()
# =========================================================

languages = ("Python", "Java", "C++")

for index, value in enumerate(languages):
    print(index, value)

# Output:
# 0 Python
# 1 Java
# 2 C++


# =========================================================
# zip()
# =========================================================

names = ("Vinita","Rahul","Amit")

marks = (90,85,95)

result = tuple(zip(names, marks))

print(result)

# Output:
# (('Vinita',90), ('Rahul',85), ('Amit',95))


# =========================================================
# Tuple Comparison
# =========================================================

tuple1 = (1,2,3)

tuple2 = (1,2,3)

tuple3 = (1,2)

print(tuple1 == tuple2)

print(tuple1 != tuple3)

# Output:
# True
# True


# =========================================================
# Copying Tuples
# =========================================================

"""
Tuples are immutable.

No copy() method is available.

Assignment creates another reference.

This is safe because tuples cannot change.
"""

tuple1 = (10,20,30)

tuple2 = tuple1

print(tuple1)

print(tuple2)


# =========================================================
# Sorting Tuple
# =========================================================

numbers = (40,20,50,10)

sorted_numbers = tuple(sorted(numbers))

print(sorted_numbers)

# Output:
# (10,20,40,50)


# =========================================================
# Reverse Tuple
# =========================================================

numbers = (10,20,30,40)

reverse_tuple = numbers[::-1]

print(reverse_tuple)

# Output:
# (40,30,20,10)


# =========================================================
# Convert Tuple
# =========================================================

numbers = (10,20,30)

print(list(numbers))

print(set(numbers))

print(tuple(numbers))


# =========================================================
# Time Complexity
# =========================================================

"""
Operation               Complexity

Access                  O(1)

Search                  O(n)

Traversal               O(n)

count()                 O(n)

index()                 O(n)

Concatenation           O(n)

Slicing                 O(k)
"""


# =========================================================
# Difference Between List and Tuple
# =========================================================

"""
List

- Mutable
- Larger memory
- Slower
- Many methods

Tuple

- Immutable
- Less memory
- Faster
- Only count() and index()
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a Tuple?

Answer:
An ordered, immutable collection.

------------------------------------------------

2. Are Tuples mutable?

Answer:
No.

------------------------------------------------

3. Which bracket is used?

Answer:
()

------------------------------------------------

4. How many tuple methods are available?

Answer:
Two

count()

index()

------------------------------------------------

5. Difference between List and Tuple?

List

Mutable

Tuple

Immutable

------------------------------------------------

6. Why are Tuples faster?

Answer:
Because they are immutable.

------------------------------------------------

7. How do you create a single-element tuple?

Answer:

t = (10,)

------------------------------------------------

8. What is Packing?

Answer:
Storing multiple values into one tuple.

------------------------------------------------

9. What is Unpacking?

Answer:
Assigning tuple values to variables.

------------------------------------------------

10. Which function converts List into Tuple?

Answer:

tuple()

------------------------------------------------

11. Can Tuples contain Lists?

Answer:
Yes.

------------------------------------------------

12. Can Tuples contain Tuples?

Answer:
Yes.

------------------------------------------------

13. Which function returns tuple length?

Answer:

len()

------------------------------------------------

14. Which method counts occurrences?

Answer:

count()

------------------------------------------------

15. Which method returns index?

Answer:

index()

------------------------------------------------

16. Can tuple elements be duplicated?

Answer:
Yes.

------------------------------------------------

17. Which operator joins tuples?

Answer:
+

------------------------------------------------

18. Which operator repeats tuples?

Answer:
*

------------------------------------------------

19. Which function sorts a tuple?

Answer:

sorted()

------------------------------------------------

20. Are Tuples hashable?

Answer:
Yes, if all their elements are hashable.
"""

# =========================================================
# MINI PROJECT
# =========================================================

students = (
    ("Vinita", 90),
    ("Rahul", 85),
    ("Amit", 95)
)

print("\n========== STUDENT REPORT ==========")

total = 0

for name, marks in students:

    print(f"Name  : {name}")

    print(f"Marks : {marks}")

    print("-" * 25)

    total += marks

average = total / len(students)

print(f"Class Average : {average:.2f}")

print("=" * 40)


# =========================================================
# CHEAT SHEET
# =========================================================

"""
Tuple Creation      ()

Length              len()

Count               count()

Index               index()

Concatenate         +

Repeat              *

Slice               tuple[1:4]

Reverse             tuple[::-1]

Convert             tuple()

Sort                sorted()

Membership          in

Traversal           for loop
"""


# =========================================================
# END OF FILE
# =========================================================