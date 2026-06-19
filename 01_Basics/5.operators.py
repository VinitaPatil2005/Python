"""
=========================================================
                PYTHON OPERATORS
=========================================================

What is an Operator?
--------------------
An operator is a symbol that performs an operation on one or
more operands (values or variables).

Example:
a = 10
b = 5

print(a + b)

Here,
+ is the operator.
a and b are operands.

=========================================================
TYPES OF OPERATORS
=========================================================

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
8. Ternary Operator (Conditional Expression)
"""

# =========================================================
# 1. ARITHMETIC OPERATORS
# =========================================================

"""
Arithmetic operators perform mathematical operations.

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus
**  Exponent
"""

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Output:
# Addition: 26
# Subtraction: 14
# Multiplication: 120
# Division: 3.333...
# Floor Division: 3
# Modulus: 2
# Exponent: 64000000


# =========================================================
# Division Example
# =========================================================

print(10 / 3)

# Output:
# 3.3333333333333335

print(10 // 3)

# Output:
# 3

print(10 % 3)

# Output:
# 1


# =========================================================
# 2. ASSIGNMENT OPERATORS
# =========================================================

"""
Assignment operators assign values to variables.

=   Assignment
+=  Add and Assign
-=  Subtract and Assign
*=  Multiply and Assign
/=  Divide and Assign
//= Floor Divide and Assign
%=  Modulus and Assign
**= Exponent and Assign
"""

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 2
print(x)

# =========================================================
# 3. COMPARISON OPERATORS
# =========================================================

"""
Comparison operators compare two values.

==   Equal
!=   Not Equal
>    Greater Than
<    Less Than
>=   Greater Than or Equal
<=   Less Than or Equal

Returns:
True or False
"""

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# =========================================================
# 4. LOGICAL OPERATORS
# =========================================================

"""
Logical operators combine conditions.

and
or
not
"""

x = 10

print(x > 5 and x < 20)
print(x > 20 or x < 20)
print(not(x > 5))

# Truth Table

print(True and True)
print(True and False)

print(True or False)

print(not True)

# =========================================================
# 5. IDENTITY OPERATORS
# =========================================================

"""
Identity operators compare whether two variables
refer to the same object in memory.

is
is not
"""

a = [1,2,3]
b = a

c = [1,2,3]

print(a is b)
print(a is c)

print(a == c)

"""
Explanation:

is
Checks Memory Address

==

Checks Value
"""

# =========================================================
# 6. MEMBERSHIP OPERATORS
# =========================================================

"""
Membership operators check whether an element
exists inside a collection.

in

not in
"""

fruits = ["Apple","Banana","Mango"]

print("Apple" in fruits)

print("Orange" in fruits)

print("Orange" not in fruits)

# =========================================================
# Membership with String
# =========================================================

text = "Python Programming"

print("Python" in text)

print("Java" in text)

# =========================================================
# 7. BITWISE OPERATORS
# =========================================================

"""
Bitwise operators work on binary numbers.

&
|

^

~

<<

>>
"""

a = 5
b = 3

print(a & b)

print(a | b)

print(a ^ b)

print(~a)

print(a << 1)

print(a >> 1)

# =========================================================
# 8. TERNARY OPERATOR (Conditional Expression)
# =========================================================

"""
The Ternary Operator is a shorthand way of writing
an if-else statement in a single line.

Syntax:

value_if_true if condition else value_if_false

It makes the code shorter and more readable.
"""

# Example 1

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

# Output:
# Adult


# ---------------------------------------------------------
# Example 2
# ---------------------------------------------------------

num = 15

message = "Positive" if num > 0 else "Negative"

print(message)

# Output:
# Positive


# ---------------------------------------------------------
# Example 3
# ---------------------------------------------------------

a = 25
b = 40

largest = a if a > b else b

print("Largest Number =", largest)

# Output:
# Largest Number = 40


# ---------------------------------------------------------
# Example 4
# ---------------------------------------------------------

marks = 75

status = "Pass" if marks >= 35 else "Fail"

print(status)

# Output:
# Pass


# ---------------------------------------------------------
# Nested Ternary Operator
# ---------------------------------------------------------

"""
A nested ternary operator is used when there are
multiple conditions.

Syntax:

value1 if condition1 else value2 if condition2 else value3
"""

marks = 88

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 50
    else "Fail"
)

print("Grade =", grade)

# Output:
# Grade = B

# =========================================================
# OPERATOR PRECEDENCE
# =========================================================

"""
Operator Precedence determines the order in which
operations are performed.

Operators with higher precedence are evaluated first.

If two operators have the same precedence,
evaluation usually happens from LEFT to RIGHT.

Parentheses () can be used to change the order
of evaluation.
"""

# ---------------------------------------------------------
# Precedence Table
# ---------------------------------------------------------

"""
Highest Precedence

1. Parentheses               ()

2. Exponent                  **

3. Unary Operators           +x  -x  ~x

4. Multiplication            *  /  //  %

5. Addition                  +  -

6. Bitwise Shift             <<  >>

7. Bitwise AND               &

8. Bitwise XOR               ^

9. Bitwise OR                |

10. Comparison               == != > < >= <=

11. Logical NOT              not

12. Logical AND              and

13. Logical OR               or

Lowest Precedence
"""

# ---------------------------------------------------------
# Example 1
# ---------------------------------------------------------

result = 2 + 3 * 4

print(result)

# Output:
# 14

# Multiplication happens before Addition.


# ---------------------------------------------------------
# Example 2
# ---------------------------------------------------------

result = (2 + 3) * 4

print(result)

# Output:
# 20

# Parentheses are evaluated first.


# ---------------------------------------------------------
# Example 3
# ---------------------------------------------------------

result = 2 ** 3 * 4

print(result)

# Output:
# 32

# Exponent has higher precedence than Multiplication.


# ---------------------------------------------------------
# Example 4
# ---------------------------------------------------------

result = 10 + 20 / 5

print(result)

# Output:
# 14.0

# Division happens before Addition.


# ---------------------------------------------------------
# Example 5
# ---------------------------------------------------------

result = (10 + 20) / 5

print(result)

# Output:
# 6.0


# ---------------------------------------------------------
# Example 6
# ---------------------------------------------------------

print(True or False and False)

# Output:
# True

# AND has higher precedence than OR.


# ---------------------------------------------------------
# Example 7
# ---------------------------------------------------------

print(not False and True)

# Output:
# True

# NOT executes before AND.


# ---------------------------------------------------------
# Example 8
# ---------------------------------------------------------

print(10 > 5 and 20 > 10)

# Output:
# True


# ---------------------------------------------------------
# Remember
# ---------------------------------------------------------

"""
PEMDAS Rule

P → Parentheses

E → Exponent

MD → Multiplication & Division

AS → Addition & Subtraction

After arithmetic,
comparison operators are evaluated,
followed by logical operators.
"""

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================

"""
1. What is an operator?

Answer:
A symbol used to perform operations on operands.

------------------------------------------------

2. How many types of operators are there in Python?

Answer:

Arithmetic

Assignment

Comparison

Logical

Identity

Membership

Bitwise

------------------------------------------------

3. Difference between / and // ?

/

Returns decimal value.

//

Returns integer quotient.

------------------------------------------------

4. Difference between = and == ?

=

Assignment operator.

==

Comparison operator.

------------------------------------------------

5. Difference between is and == ?

==

Compares values.

is

Compares memory location.

------------------------------------------------

6. Which operator checks membership?

Answer:

in

not in

------------------------------------------------

7. What is the output?

print(2 ** 3)

Answer:
8

------------------------------------------------

8. What is modulus (%) used for?

Answer:

Returns remainder.

------------------------------------------------

9. Which operator has the highest precedence?

Answer:

()

------------------------------------------------

10. Which logical operator returns True only
when both conditions are True?

Answer:

and
"""

# =========================================================
# PRACTICE PROGRAMS
# =========================================================

"""
1. Perform all arithmetic operations on two numbers.

2. Find quotient and remainder.

3. Compare two numbers.

4. Check whether a student passed using logical operators.

5. Check if a character exists in a string.

6. Check if a number exists in a list.

7. Swap two numbers using assignment operators.

8. Use bitwise operators on two integers.

9. Find the square of a number using **.

10. Demonstrate operator precedence.
"""

# =========================================================
# MINI EXERCISE
# =========================================================

num1 = 15
num2 = 4

print("\n===== MINI EXERCISE =====")

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)

print("Greater:", num1 > num2)
print("Equal:", num1 == num2)

print("Logical AND:", num1 > 10 and num2 < 10)

# =========================================================
# END OF FILE
# =========================================================