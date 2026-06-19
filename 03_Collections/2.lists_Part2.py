# =========================================================
#            PYTHON LISTS (PART 2)
# =========================================================

# =========================================================
# Traversing a List using for Loop
# =========================================================

"""
Traversing means visiting every element of a list.
"""

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

# Output:
# Apple
# Banana
# Mango
# Orange


# =========================================================
# Traversing using Index
# =========================================================

numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print(f"Index {i} = {numbers[i]}")


# =========================================================
# Traversing using while Loop
# =========================================================

numbers = [100, 200, 300, 400]

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1


# =========================================================
# Membership Operators
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)

print("Orange" in fruits)

print("Orange" not in fruits)

# Output:
# True
# False
# True


# =========================================================
# List Concatenation
# =========================================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)

# Output:
# [1,2,3,4,5,6]


# =========================================================
# List Repetition
# =========================================================

numbers = [10, 20]

print(numbers * 3)

# Output:
# [10,20,10,20,10,20]


# =========================================================
# count()
# =========================================================

"""
Returns the number of occurrences.
"""

numbers = [10, 20, 30, 20, 20]

print(numbers.count(20))

# Output:
# 3


# =========================================================
# index()
# =========================================================

"""
Returns the first occurrence of a value.
"""

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))

# Output:
# 1


# =========================================================
# sort()
# =========================================================

"""
Sorts the original list in ascending order.
"""

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# Output:
# [10,20,30,40]


# =========================================================
# Descending Order
# =========================================================

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# Output:
# [40,30,20,10]


# =========================================================
# Sorting Strings
# =========================================================

fruits = ["Mango", "Apple", "Orange", "Banana"]

fruits.sort()

print(fruits)

# Output:
# ['Apple','Banana','Mango','Orange']


# =========================================================
# reverse()
# =========================================================

"""
Reverses the original list.
"""

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)

# Output:
# [5,4,3,2,1]


# =========================================================
# sorted()
# =========================================================

"""
Returns a NEW sorted list.

Original list remains unchanged.
"""

numbers = [40, 20, 50, 10]

new_list = sorted(numbers)

print(new_list)

print(numbers)

# Output:
# [10,20,40,50]
# [40,20,50,10]


# =========================================================
# min()
# =========================================================

numbers = [40, 10, 70, 20]

print(min(numbers))

# Output:
# 10


# =========================================================
# max()
# =========================================================

print(max(numbers))

# Output:
# 70


# =========================================================
# sum()
# =========================================================

numbers = [10, 20, 30]

print(sum(numbers))

# Output:
# 60


# =========================================================
# Aliasing
# =========================================================

"""
Both variables point to the SAME list.
"""

list1 = [10, 20, 30]

list2 = list1

list2.append(40)

print(list1)
print(list2)

# Both lists change.


# =========================================================
# Copy using copy()
# =========================================================

"""
Creates a separate copy.
"""

list1 = [10, 20, 30]

list2 = list1.copy()

list2.append(40)

print(list1)
print(list2)

# list1 remains unchanged.


# =========================================================
# Copy using list()
# =========================================================

numbers = [1, 2, 3]

copy_numbers = list(numbers)

print(copy_numbers)


# =========================================================
# Copy using Slicing
# =========================================================

numbers = [10, 20, 30]

copy_numbers = numbers[:]

print(copy_numbers)


# =========================================================
# Nested Lists
# =========================================================

students = [
    ["Vinita", 21],
    ["Rahul", 22],
    ["Amit", 20]
]

print(students)

print(students[0])

print(students[0][0])

print(students[1][1])

# Output:
# Vinita
# 22


# =========================================================
# Nested List Traversal
# =========================================================

for student in students:
    print(student)

print()

for name, age in students:
    print(name, age)


# =========================================================
# Comparison Operators
# =========================================================

a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2]

print(a == b)

print(a != c)

# Output:
# True
# True


# =========================================================
# Summary Table
# =========================================================

"""
Method              Purpose

count()             Count occurrences

index()             Find position

sort()              Sort original list

sorted()            Return sorted copy

reverse()           Reverse list

copy()              Create copy

min()               Smallest value

max()               Largest value

sum()               Total of elements
"""


# =========================================================
# END OF PART 2
# =========================================================