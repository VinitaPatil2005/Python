# =========================================================
#              PYTHON WHILE LOOP (PART 3)
# =========================================================

# =========================================================
# Time Complexity
# =========================================================

"""
Operation                        Complexity

Simple while Loop                O(n)

Nested while Loop                O(n²)

Traversal                        O(n)

Search                           O(n)

Pattern Printing                 O(n²)
"""


# =========================================================
# Fibonacci Series
# =========================================================

terms = 10

a = 0
b = 1

count = 0

while count < terms:

    print(a)

    c = a + b

    a = b

    b = c

    count += 1


# =========================================================
# Sum of Digits
# =========================================================

number = 98765

total = 0

while number > 0:

    digit = number % 10

    total += digit

    number //= 10

print("Sum =", total)


# =========================================================
# Product of Digits
# =========================================================

number = 234

product = 1

while number > 0:

    digit = number % 10

    product *= digit

    number //= 10

print("Product =", product)


# =========================================================
# GCD (Greatest Common Divisor)
# =========================================================

a = 48
b = 18

while b != 0:

    a, b = b, a % b

print("GCD =", a)


# =========================================================
# LCM (Least Common Multiple)
# =========================================================

num1 = 12
num2 = 18

a = num1
b = num2

while b != 0:

    a, b = b, a % b

gcd = a

lcm = (num1 * num2) // gcd

print("LCM =", lcm)


# =========================================================
# Pattern 1
# =========================================================

"""
*
**
***
****
*****
"""

i = 1

while i <= 5:

    print("*" * i)

    i += 1


# =========================================================
# Pattern 2
# =========================================================

"""
*****
****
***
**
*
"""

i = 5

while i >= 1:

    print("*" * i)

    i -= 1


# =========================================================
# Pattern 3
# =========================================================

"""
1
12
123
1234
12345
"""

i = 1

while i <= 5:

    j = 1

    while j <= i:

        print(j, end="")

        j += 1

    print()

    i += 1


# =========================================================
# Count Vowels
# =========================================================

text = "Python Programming"

index = 0

count = 0

while index < len(text):

    if text[index].lower() in "aeiou":

        count += 1

    index += 1

print("Vowels =", count)


# =========================================================
# Count Digits
# =========================================================

text = "Python12345"

index = 0

digits = 0

while index < len(text):

    if text[index].isdigit():

        digits += 1

    index += 1

print("Digits =", digits)


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a while loop?

Answer:
A loop that executes as long as the condition is True.

------------------------------------------------

2. Difference between for and while?

for

Known number of iterations.

while

Unknown number of iterations.

------------------------------------------------

3. What happens if the condition is always True?

Answer:
Infinite Loop.

------------------------------------------------

4. Which keyword exits the loop?

Answer:

break

------------------------------------------------

5. Which keyword skips one iteration?

Answer:

continue

------------------------------------------------

6. What is pass?

Answer:
Placeholder statement.

------------------------------------------------

7. When does while...else execute?

Answer:
When loop finishes normally.

------------------------------------------------

8. Can while loop run zero times?

Answer:
Yes.

------------------------------------------------

9. What causes an infinite loop?

Answer:
Condition never becomes False.

------------------------------------------------

10. Which loop is better for menu-driven programs?

Answer:

while

------------------------------------------------

11. Which loop is better when iterations are known?

Answer:

for

------------------------------------------------

12. Can we nest while loops?

Answer:
Yes.

------------------------------------------------

13. Complexity of simple while loop?

Answer:

O(n)

------------------------------------------------

14. Complexity of nested while loop?

Answer:

O(n²)

------------------------------------------------

15. Which loop is preferred for traversing lists?

Answer:

for

------------------------------------------------

16. Can break terminate a while loop?

Answer:
Yes.

------------------------------------------------

17. Can continue skip one iteration?

Answer:
Yes.

------------------------------------------------

18. Does else execute after break?

Answer:
No.

------------------------------------------------

19. Which statement does nothing?

Answer:

pass

------------------------------------------------

20. Can while loop be used with True?

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

names = list(students.keys())

index = 0

while index < len(names):

    name = names[index]

    marks = students[name]

    print(f"{name:10} : {marks}")

    total += marks

    index += 1

average = total / len(students)

print("-" * 35)

print(f"Average Marks : {average:.2f}")

print(f"Highest Marks : {max(students.values())}")

print(f"Lowest Marks  : {min(students.values())}")

print("=" * 40)


# =========================================================
# CHEAT SHEET
# =========================================================

"""
Basic Loop

while condition:
    statements

------------------------------------

Infinite Loop

while True:
    ...

------------------------------------

break

Exit loop immediately

------------------------------------

continue

Skip current iteration

------------------------------------

pass

Placeholder statement

------------------------------------

while...else

while condition:
    ...
else:
    ...

------------------------------------

Reverse Number

digit = number % 10

number //= 10

------------------------------------

Factorial

factorial *= i

------------------------------------

Count Digits

number //= 10

------------------------------------

Fibonacci

a, b = b, a + b
"""


# =========================================================
# END OF FILE
# =========================================================