# =========================================================
#              PYTHON RECURSION (PART 3)
# =========================================================

# =========================================================
# Types of Recursion
# =========================================================

"""
1. Direct Recursion
   A function directly calls itself.

2. Indirect Recursion
   Function A calls Function B,
   and Function B calls Function A.

3. Head Recursion
   Recursive call happens first.

4. Tail Recursion
   Recursive call happens last.
"""

# =========================================================
# Head Recursion
# =========================================================

def head(number):

    if number == 0:
        return

    head(number - 1)

    print(number)

head(5)

# Output
# 1
# 2
# 3
# 4
# 5


# =========================================================
# Tail Recursion
# =========================================================

def tail(number):

    if number == 0:
        return

    print(number)

    tail(number - 1)

tail(5)

# Output
# 5
# 4
# 3
# 2
# 1


# =========================================================
# Indirect Recursion
# =========================================================

def even(number):

    if number == 0:
        return True

    return odd(number - 1)

def odd(number):

    if number == 0:
        return False

    return even(number - 1)

print(even(10))
print(odd(7))


# =========================================================
# Time Complexity
# =========================================================

"""
Operation                      Complexity

Factorial                      O(n)

Sum of Numbers                 O(n)

Power                          O(n)

Reverse String                 O(n)

Count Digits                   O(n)

Binary Search                  O(log n)

Tower of Hanoi                 O(2ⁿ)

Fibonacci (Simple)             O(2ⁿ)

Fibonacci (Optimized)          O(n)
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is recursion?

Answer:
A function calling itself.

------------------------------------------------

2. What are the two parts of recursion?

Answer:

Base Case

Recursive Case

------------------------------------------------

3. Why is the base case important?

Answer:
To stop recursion.

------------------------------------------------

4. What happens without a base case?

Answer:
RecursionError

------------------------------------------------

5. What is a call stack?

Answer:
Stores active function calls.

------------------------------------------------

6. What is head recursion?

Answer:
Recursive call before processing.

------------------------------------------------

7. What is tail recursion?

Answer:
Recursive call after processing.

------------------------------------------------

8. What is direct recursion?

Answer:
Function directly calls itself.

------------------------------------------------

9. What is indirect recursion?

Answer:
Two functions call each other.

------------------------------------------------

10. Difference between recursion and iteration?

Recursion

Uses function calls

Uses call stack

Consumes more memory

Elegant

Iteration

Uses loops

Less memory

Usually faster

------------------------------------------------

11. Which algorithm commonly uses recursion?

Answer:

Binary Search

------------------------------------------------

12. Which data structure supports recursion?

Answer:

Stack

------------------------------------------------

13. Is recursion always slower?

Answer:
Usually yes because of function call overhead.

------------------------------------------------

14. What is stack overflow?

Answer:
Too many recursive calls.

------------------------------------------------

15. Can every recursive solution be written iteratively?

Answer:
Yes, in most cases.

------------------------------------------------

16. Complexity of Binary Search?

Answer:

O(log n)

------------------------------------------------

17. Complexity of Tower of Hanoi?

Answer:

O(2ⁿ)

------------------------------------------------

18. Complexity of simple factorial recursion?

Answer:

O(n)

------------------------------------------------

19. Which recursion is easier to optimize?

Answer:

Tail Recursion

------------------------------------------------

20. When should recursion be used?

Answer:
When problems naturally break into smaller
subproblems.
"""


# =========================================================
# MINI PROJECT
# =========================================================

def factorial(number):

    if number <= 1:
        return 1

    return number * factorial(number - 1)

print("\n========== FACTORIAL TABLE ==========")

for i in range(1, 11):

    print(f"{i:2}! = {factorial(i)}")

print("=" * 40)


# =========================================================
# END OF FILE
# =========================================================