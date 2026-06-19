# =========================================================
#           PYTHON IF...ELSE (PART 3)
# =========================================================

# =========================================================
# Time Complexity
# =========================================================

"""
The time complexity of an if statement depends on the
condition being checked.

Simple if Statement         O(1)

if...else                   O(1)

if...elif...else            O(n) (Worst Case)

Nested if                   Depends on nesting

Logical Operators           O(1)
"""


# =========================================================
# Best Practices
# =========================================================

"""
1. Keep conditions simple.

2. Avoid deeply nested if statements.

3. Use meaningful variable names.

4. Prefer elif instead of multiple if statements
   when only one condition should execute.

5. Use logical operators to reduce code.

6. Use Ternary Operator only for simple conditions.

7. Maintain proper indentation.
"""


# =========================================================
# Common Interview Programs
# =========================================================

# ---------------------------------------------------------
# Check Palindrome Number
# ---------------------------------------------------------

number = 121

original = number

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if original == reverse:
    print("Palindrome")

else:
    print("Not Palindrome")


# ---------------------------------------------------------
# Divisible by 5 and 11
# ---------------------------------------------------------

number = 55

if number % 5 == 0 and number % 11 == 0:

    print("Divisible by both")

else:

    print("Not Divisible")


# ---------------------------------------------------------
# Character Check
# ---------------------------------------------------------

ch = "A"

if ch.isalpha():

    print("Alphabet")

elif ch.isdigit():

    print("Digit")

else:

    print("Special Character")


# ---------------------------------------------------------
# Vowel or Consonant
# ---------------------------------------------------------

letter = "e"

if letter.lower() in "aeiou":

    print("Vowel")

else:

    print("Consonant")


# ---------------------------------------------------------
# Number of Digits
# ---------------------------------------------------------

number = 12345

count = len(str(number))

print("Digits =", count)


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is an if statement?

Answer:
Executes a block of code only if the condition is True.

------------------------------------------------

2. What is the difference between if and if...else?

if
Runs only when the condition is True.

if...else
Chooses between two blocks.

------------------------------------------------

3. When should we use elif?

Answer:
When checking multiple conditions.

------------------------------------------------

4. What is Nested if?

Answer:
An if statement inside another if statement.

------------------------------------------------

5. What is a Ternary Operator?

Answer:
A one-line if...else expression.

Syntax:

value_if_true if condition else value_if_false

------------------------------------------------

6. Which keyword represents "do nothing"?

Answer:

pass

------------------------------------------------

7. Which operators are commonly used with if?

Answer:

Comparison Operators

Logical Operators

Membership Operators

Identity Operators

------------------------------------------------

8. Which comparison operator checks equality?

Answer:

==

------------------------------------------------

9. Difference between = and == ?

=

Assignment Operator

==

Comparison Operator

------------------------------------------------

10. What happens if indentation is incorrect?

Answer:
IndentationError

------------------------------------------------

11. Which operator checks multiple conditions?

Answer:

and

or

------------------------------------------------

12. Which operator reverses a condition?

Answer:

not

------------------------------------------------

13. Can an if statement exist without else?

Answer:
Yes.

------------------------------------------------

14. Can an else exist without if?

Answer:
No.

------------------------------------------------

15. Does Python support switch?

Answer:
Python 3.10 introduced match...case.

------------------------------------------------

16. Which statement exits a loop?

Answer:

break

------------------------------------------------

17. Which statement skips one iteration?

Answer:

continue

------------------------------------------------

18. Can conditions return only True or False?

Answer:
Yes.

------------------------------------------------

19. What is Boolean data type?

Answer:
True or False.

------------------------------------------------

20. Which keyword checks multiple conditions?

Answer:

elif
"""

# =========================================================
# MINI PROJECT
# =========================================================

print("\n========== STUDENT RESULT ==========")

name = "Vinita"

marks = 86

attendance = 90

print("Name       :", name)

print("Marks      :", marks)

print("Attendance :", attendance, "%")

if attendance < 75:

    result = "Detained"

elif marks >= 90:

    result = "Grade A+"

elif marks >= 80:

    result = "Grade A"

elif marks >= 70:

    result = "Grade B"

elif marks >= 60:

    result = "Grade C"

elif marks >= 35:

    result = "Pass"

else:

    result = "Fail"

print("Result     :", result)

print("=" * 40)


# =========================================================
# CHEAT SHEET
# =========================================================

"""
if

if condition:
    statements

------------------------------------

if...else

if condition:
    statements
else:
    statements

------------------------------------

if...elif...else

if condition:
    ...
elif condition:
    ...
else:
    ...

------------------------------------

Nested if

if condition:
    if condition:
        ...

------------------------------------

Ternary

value_if_true if condition else value_if_false

------------------------------------

pass

if condition:
    pass
"""


# =========================================================
# END OF FILE
# =========================================================