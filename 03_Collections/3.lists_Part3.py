# =========================================================
#            PYTHON LISTS (PART 3)
# =========================================================

# =========================================================
# List Comprehension
# =========================================================

"""
List Comprehension is a short and elegant way
to create lists.

Syntax:

[expression for item in iterable]
"""

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# =========================================================
# List Comprehension with Condition
# =========================================================

numbers = [1,2,3,4,5,6,7,8,9,10]

even = [num for num in numbers if num % 2 == 0]

print(even)

# Output:
# [2,4,6,8,10]


# =========================================================
# Odd Numbers
# =========================================================

odd = [num for num in numbers if num % 2 != 0]

print(odd)

# Output:
# [1,3,5,7,9]


# =========================================================
# Convert to Uppercase
# =========================================================

languages = ["python","java","c++"]

upper = [lang.upper() for lang in languages]

print(upper)

# Output:
# ['PYTHON', 'JAVA', 'C++']


# =========================================================
# Nested List
# =========================================================

matrix = [

    [1,2,3],

    [4,5,6],

    [7,8,9]

]

print(matrix)

print(matrix[0])

print(matrix[1][2])

# Output:
# 6


# =========================================================
# Nested Loop
# =========================================================

for row in matrix:

    for value in row:

        print(value, end=" ")

    print()


# =========================================================
# Flatten Nested List
# =========================================================

flat = [item for row in matrix for item in row]

print(flat)

# Output:
# [1,2,3,4,5,6,7,8,9]


# =========================================================
# enumerate()
# =========================================================

"""
Returns index and value.
"""

fruits = ["Apple","Banana","Mango"]

for index, value in enumerate(fruits):

    print(index, value)

# Output:
# 0 Apple
# 1 Banana
# 2 Mango


# =========================================================
# zip()
# =========================================================

names = ["Vinita","Rahul","Amit"]

marks = [90,85,95]

result = list(zip(names, marks))

print(result)

# Output:
# [('Vinita',90), ('Rahul',85), ('Amit',95)]


# =========================================================
# Unzip
# =========================================================

students = [('Vinita',90), ('Rahul',85)]

names, marks = zip(*students)

print(names)

print(marks)


# =========================================================
# List as Stack
# =========================================================

"""
Stack -> LIFO
"""

stack = []

stack.append(10)

stack.append(20)

stack.append(30)

print(stack)

stack.pop()

print(stack)


# =========================================================
# List as Queue
# =========================================================

queue = []

queue.append("A")

queue.append("B")

queue.append("C")

print(queue)

queue.pop(0)

print(queue)


# =========================================================
# Shallow Copy Example
# =========================================================

list1 = [[1,2],[3,4]]

list2 = list1.copy()

list2[0][0] = 100

print(list1)

print(list2)

"""
Nested objects are shared.
"""


# =========================================================
# Time Complexity
# =========================================================

"""
Operation           Complexity

Append              O(1)

Insert              O(n)

Delete              O(n)

Search              O(n)

Access by Index     O(1)

Sort                O(n log n)
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a List?

Answer:
An ordered, mutable collection.

------------------------------------------------

2. Can Lists store different data types?

Answer:
Yes.

------------------------------------------------

3. Difference between append() and extend()?

append()

Adds one object.

extend()

Adds multiple elements.

------------------------------------------------

4. Difference between remove() and pop()?

remove()

Removes by value.

pop()

Removes by index.

------------------------------------------------

5. Difference between sort() and sorted()?

sort()

Changes original list.

sorted()

Returns new sorted list.

------------------------------------------------

6. Difference between copy() and aliasing?

Aliasing

Both variables point to same list.

Copy

Creates a new list.

------------------------------------------------

7. What is List Comprehension?

Answer:
A short syntax for creating lists.

------------------------------------------------

8. Which function returns list length?

Answer:
len()

------------------------------------------------

9. Can Lists contain Lists?

Answer:
Yes.

------------------------------------------------

10. Which operator concatenates two lists?

Answer:
+

------------------------------------------------

11. Which operator repeats a list?

Answer:
*

------------------------------------------------

12. Which method counts occurrences?

Answer:
count()

------------------------------------------------

13. Which method returns first index?

Answer:
index()

------------------------------------------------

14. Which function returns maximum value?

Answer:
max()

------------------------------------------------

15. Which function returns minimum value?

Answer:
min()

------------------------------------------------

16. Which function returns total?

Answer:
sum()

------------------------------------------------

17. What is slicing?

Answer:
Extracting part of a list.

------------------------------------------------

18. Are Lists mutable?

Answer:
Yes.

------------------------------------------------

19. What is enumerate()?

Answer:
Returns index and value.

------------------------------------------------

20. What is zip()?

Answer:
Combines multiple iterables.
"""

# =========================================================
# MINI PROJECT
# =========================================================

students = []

students.append(["Vinita", 90])

students.append(["Rahul", 85])

students.append(["Amit", 95])

print("\n========== STUDENT REPORT ==========")

for name, marks in students:

    print(f"Name : {name}")

    print(f"Marks: {marks}")

    print("-" * 25)

average = sum(mark for _, mark in students) / len(students)

print(f"Class Average: {average:.2f}")

print("=" * 40)


# =========================================================
# CHEAT SHEET
# =========================================================

"""
append()       -> Add one element

extend()       -> Add multiple elements

insert()       -> Insert at position

remove()       -> Remove by value

pop()          -> Remove by index

clear()        -> Remove all

sort()         -> Sort list

reverse()      -> Reverse list

copy()         -> Copy list

count()        -> Count occurrences

index()        -> Find index

len()          -> Length

sum()          -> Sum

min()          -> Minimum

max()          -> Maximum

sorted()       -> Sorted copy
"""


# =========================================================
# END OF FILE
# =========================================================