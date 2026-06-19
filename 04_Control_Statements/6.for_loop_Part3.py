# =========================================================
#              PYTHON FOR LOOP (PART 3)
# =========================================================

# =========================================================
# Time Complexity
# =========================================================

"""
Operation                        Complexity

Simple for Loop                  O(n)

Nested for Loop                  O(n²)

range()                          O(1)

Traversal                        O(n)

Search                           O(n)

Pattern Printing                 O(n²)
"""


# =========================================================
# Pyramid Pattern
# =========================================================

"""
    *
   ***
  *****
 *******
*********
"""

rows = 5

for i in range(rows):

    spaces = " " * (rows - i - 1)

    stars = "*" * (2 * i + 1)

    print(spaces + stars)


# =========================================================
# Inverted Pyramid
# =========================================================

"""
*********
 *******
  *****
   ***
    *
"""

rows = 5

for i in range(rows):

    spaces = " " * i

    stars = "*" * (2 * (rows - i) - 1)

    print(spaces + stars)


# =========================================================
# Floyd's Triangle
# =========================================================

"""
1
2 3
4 5 6
7 8 9 10
"""

number = 1

for i in range(1, 5):

    for j in range(i):

        print(number, end=" ")

        number += 1

    print()


# =========================================================
# Multiplication Tables (1 to 10)
# =========================================================

for table in range(1, 11):

    print(f"\nTable of {table}")

    for i in range(1, 11):

        print(f"{table} x {i} = {table*i}")


# =========================================================
# Sum of Squares
# =========================================================

total = 0

for i in range(1, 6):

    total += i ** 2

print("Sum of Squares =", total)


# =========================================================
# Sum of Cubes
# =========================================================

total = 0

for i in range(1, 6):

    total += i ** 3

print("Sum of Cubes =", total)


# =========================================================
# Count Vowels
# =========================================================

text = "Python Programming"

count = 0

for ch in text.lower():

    if ch in "aeiou":

        count += 1

print("Vowels =", count)


# =========================================================
# Count Digits
# =========================================================

text = "Python12345"

digits = 0

for ch in text:

    if ch.isdigit():

        digits += 1

print("Digits =", digits)


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a for loop?

Answer:
A loop used to iterate over an iterable.

------------------------------------------------

2. What is an iterable?

Answer:
An object that can be traversed one element at a time.

Examples:
List
Tuple
Set
Dictionary
String
range()

------------------------------------------------

3. What does range(5) return?

Answer:
0 1 2 3 4

------------------------------------------------

4. Difference between break and continue?

break

Terminates the loop.

continue

Skips one iteration.

------------------------------------------------

5. What is pass?

Answer:
A placeholder statement.

------------------------------------------------

6. When does else execute in a for loop?

Answer:
When the loop completes normally
(without break).

------------------------------------------------

7. Which function returns index and value?

Answer:

enumerate()

------------------------------------------------

8. Which function combines multiple iterables?

Answer:

zip()

------------------------------------------------

9. Can we iterate over dictionaries?

Answer:
Yes.

------------------------------------------------

10. What is nested loop?

Answer:
A loop inside another loop.

------------------------------------------------

11. What is the complexity of a simple for loop?

Answer:

O(n)

------------------------------------------------

12. What is the complexity of nested loops?

Answer:

O(n²)

------------------------------------------------

13. Can we modify a list while iterating?

Answer:
Possible but generally not recommended.

------------------------------------------------

14. What does range(start, stop, step) mean?

Answer:

Start value

Stop value (exclusive)

Increment/Decrement

------------------------------------------------

15. Which keyword skips current iteration?

Answer:

continue

------------------------------------------------

16. Which keyword exits loop?

Answer:

break

------------------------------------------------

17. Can else exist without break?

Answer:
Yes.

------------------------------------------------

18. Which iterable is unordered?

Answer:

Set

------------------------------------------------

19. Can strings be iterated?

Answer:
Yes.

------------------------------------------------

20. Can tuples be iterated?

Answer:
Yes.
"""

# =========================================================
# MINI PROJECT
# =========================================================

students = {

    "Vinita": 95,

    "Rahul": 88,

    "Amit": 91,

    "Sneha": 84

}

print("\n========== STUDENT REPORT ==========")

total = 0

for name, marks in students.items():

    print(f"{name:10} : {marks}")

    total += marks

average = total / len(students)

print("-" * 30)

print(f"Average Marks : {average:.2f}")

highest = max(students.values())

lowest = min(students.values())

print(f"Highest Marks : {highest}")

print(f"Lowest Marks  : {lowest}")

print("=" * 40)


# =========================================================
# CHEAT SHEET
# =========================================================

"""
Basic Loop

for i in range(5):
    print(i)

------------------------------------

range(stop)

range(5)

------------------------------------

range(start, stop)

range(1,6)

------------------------------------

range(start, stop, step)

range(0,20,2)

------------------------------------

Reverse

range(10,0,-1)

------------------------------------

break

Exit Loop

------------------------------------

continue

Skip Iteration

------------------------------------

pass

Placeholder

------------------------------------

else

Runs if loop ends normally

------------------------------------

enumerate()

Index + Value

------------------------------------

zip()

Combine Iterables
"""


# =========================================================
# END OF FILE
# =========================================================