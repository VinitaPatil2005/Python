# =========================================================
#                PYTHON SETS (PART 2)
# =========================================================

# =========================================================
# union()
# =========================================================

"""
Returns a new set containing all unique elements
from both sets.
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print(result)

# Output:
# {1, 2, 3, 4, 5}


# =========================================================
# | Operator
# =========================================================

result = set1 | set2

print(result)


# =========================================================
# intersection()
# =========================================================

"""
Returns common elements.
"""

set1 = {10,20,30,40}
set2 = {30,40,50,60}

print(set1.intersection(set2))

# Output:
# {30,40}


# =========================================================
# & Operator
# =========================================================

print(set1 & set2)


# =========================================================
# difference()
# =========================================================

"""
Returns elements present in first set
but not in second set.
"""

print(set1.difference(set2))

# Output:
# {10,20}


# =========================================================
# - Operator
# =========================================================

print(set1 - set2)


# =========================================================
# symmetric_difference()
# =========================================================

"""
Returns uncommon elements.
"""

print(set1.symmetric_difference(set2))

# Output:
# {10,20,50,60}


# =========================================================
# ^ Operator
# =========================================================

print(set1 ^ set2)


# =========================================================
# intersection_update()
# =========================================================

"""
Updates original set with common elements.
"""

a = {1,2,3,4}
b = {3,4,5,6}

a.intersection_update(b)

print(a)

# Output:
# {3,4}


# =========================================================
# difference_update()
# =========================================================

a = {1,2,3,4}
b = {3,4,5}

a.difference_update(b)

print(a)

# Output:
# {1,2}


# =========================================================
# symmetric_difference_update()
# =========================================================

a = {1,2,3}
b = {3,4,5}

a.symmetric_difference_update(b)

print(a)

# Output:
# {1,2,4,5}


# =========================================================
# issubset()
# =========================================================

small = {1,2}

large = {1,2,3,4}

print(small.issubset(large))

# Output:
# True


# =========================================================
# issuperset()
# =========================================================

print(large.issuperset(small))

# Output:
# True


# =========================================================
# isdisjoint()
# =========================================================

a = {1,2,3}
b = {4,5,6}

print(a.isdisjoint(b))

# Output:
# True


# =========================================================
# Frozen Set
# =========================================================

"""
A Frozen Set is an immutable set.
"""

numbers = frozenset([10,20,30])

print(numbers)

# numbers.add(40)

# Error


# =========================================================
# Time Complexity
# =========================================================

"""
Operation               Complexity

Add                     O(1)

Remove                  O(1)

Membership              O(1)

Union                   O(len(A)+len(B))

Intersection            O(min(len(A),len(B)))

Difference              O(len(A))

Copy                    O(n)
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a Set?

Answer:
An unordered collection of unique elements.

------------------------------------------------

2. Are Sets ordered?

Answer:
No.

------------------------------------------------

3. Can Sets contain duplicate values?

Answer:
No.

------------------------------------------------

4. Which function creates an empty Set?

Answer:

set()

------------------------------------------------

5. Difference between remove() and discard()?

remove()

Raises KeyError if value is absent.

discard()

Does not raise an error.

------------------------------------------------

6. Which method combines two Sets?

Answer:

union()

------------------------------------------------

7. Which method returns common elements?

Answer:

intersection()

------------------------------------------------

8. Which method returns uncommon elements?

Answer:

symmetric_difference()

------------------------------------------------

9. Which method checks subset?

Answer:

issubset()

------------------------------------------------

10. Which method checks superset?

Answer:

issuperset()

------------------------------------------------

11. Which method checks no common elements?

Answer:

isdisjoint()

------------------------------------------------

12. Which Set is immutable?

Answer:

frozenset

------------------------------------------------

13. Can Sets be indexed?

Answer:
No.

------------------------------------------------

14. Which operator performs Union?

Answer:

|

------------------------------------------------

15. Which operator performs Intersection?

Answer:

&

------------------------------------------------

16. Which operator performs Difference?

Answer:

-

------------------------------------------------

17. Which operator performs Symmetric Difference?

Answer:

^

------------------------------------------------

18. Which method removes a random element?

Answer:

pop()

------------------------------------------------

19. Which method removes duplicates from a List?

Answer:

set()

------------------------------------------------

20. Why are Sets fast?

Answer:
Because they are implemented using hash tables.
"""

# =========================================================
# MINI PROJECT
# =========================================================

python_students = {
    "Vinita",
    "Rahul",
    "Amit",
    "Sneha"
}

java_students = {
    "Rahul",
    "Sneha",
    "Pooja"
}

print("\n========== COURSE REPORT ==========")

print("Python Students:")

print(python_students)

print()

print("Java Students:")

print(java_students)

print()

print("Common Students:")

print(python_students & java_students)

print()

print("All Students:")

print(python_students | java_students)

print("=" * 40)


# =========================================================
# CHEAT SHEET
# =========================================================

"""
add()                      Add one element

update()                   Add multiple elements

remove()                   Remove value

discard()                  Remove safely

pop()                      Remove random element

clear()                    Remove all elements

union()                    Combine Sets

intersection()             Common elements

difference()               First - Second

symmetric_difference()     Uncommon elements

issubset()                 Check subset

issuperset()               Check superset

isdisjoint()               Check common elements

copy()                     Copy Set

frozenset()                Immutable Set
"""


# =========================================================
# END OF FILE
# =========================================================