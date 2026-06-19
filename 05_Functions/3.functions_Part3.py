# =========================================================
#              PYTHON FUNCTIONS (PART 3)
# =========================================================

# =========================================================
# Function Annotations (Type Hints)
# =========================================================

"""
Type hints improve code readability.

They do NOT enforce types at runtime.
"""

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))


# =========================================================
# Positional-only Parameters (/)
# =========================================================

"""
Parameters before / must be passed
positionally.
"""

def divide(a, b, /):
    return a / b

print(divide(20, 5))

# divide(a=20, b=5) ❌


# =========================================================
# Keyword-only Parameters (*)
# =========================================================

"""
Parameters after * must be passed
using keyword arguments.
"""

def student(name, *, age, city):

    print(name)

    print(age)

    print(city)

student("Vinita", age=21, city="Pune")


# =========================================================
# Positional + Keyword-only
# =========================================================

def employee(id, /, name, *, salary):

    print(id)

    print(name)

    print(salary)

employee(101, "Rahul", salary=50000)


# =========================================================
# Function to Find Maximum
# =========================================================

def maximum(a, b):

    if a > b:
        return a

    return b

print(maximum(20, 30))


# =========================================================
# Function to Find Minimum
# =========================================================

def minimum(a, b):

    if a < b:
        return a

    return b

print(minimum(20, 30))


# =========================================================
# Function to Check Prime
# =========================================================

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            return False

    return True

print(is_prime(17))

print(is_prime(20))


# =========================================================
# Function to Calculate Factorial
# =========================================================

def factorial(number):

    result = 1

    for i in range(1, number + 1):

        result *= i

    return result

print(factorial(5))


# =========================================================
# Function to Reverse String
# =========================================================

def reverse(text):

    return text[::-1]

print(reverse("Python"))


# =========================================================
# Function to Count Vowels
# =========================================================

def count_vowels(text):

    count = 0

    for ch in text.lower():

        if ch in "aeiou":

            count += 1

    return count

print(count_vowels("Programming"))


# =========================================================
# Function to Calculate Average
# =========================================================

def average(*numbers):

    return sum(numbers) / len(numbers)

print(average(10, 20, 30, 40))


# =========================================================
# Function with Exception Handling
# =========================================================

def safe_division(a, b):

    if b == 0:

        return "Cannot divide by zero."

    return a / b

print(safe_division(10, 2))

print(safe_division(10, 0))


# =========================================================
# Time Complexity
# =========================================================

"""
Simple Function             O(1)

Loop inside Function        O(n)

Nested Loops                O(n²)

Recursion                   Depends on problem

Dictionary Lookup           O(1)

List Traversal              O(n)
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a function?

Answer:
A reusable block of code.

------------------------------------------------

2. Why use functions?

Answer:
To avoid code duplication.

------------------------------------------------

3. Difference between parameter and argument?

Parameter

Variable in function definition.

Argument

Actual value passed.

------------------------------------------------

4. What is return?

Answer:
Sends value back to caller.

------------------------------------------------

5. Can a function return multiple values?

Answer:
Yes.

------------------------------------------------

6. What happens if return is omitted?

Answer:
Function returns None.

------------------------------------------------

7. What are default parameters?

Answer:
Parameters having default values.

------------------------------------------------

8. What are keyword arguments?

Answer:
Arguments passed using parameter names.

------------------------------------------------

9. What is *args?

Answer:
Accepts multiple positional arguments.

------------------------------------------------

10. What is **kwargs?

Answer:
Accepts multiple keyword arguments.

------------------------------------------------

11. What is local variable?

Answer:
Exists inside a function.

------------------------------------------------

12. What is global variable?

Answer:
Accessible throughout the program.

------------------------------------------------

13. What is the global keyword?

Answer:
Allows modifying global variables.

------------------------------------------------

14. What is recursion?

Answer:
A function calling itself.

------------------------------------------------

15. What is a lambda function?

Answer:
Anonymous function.

------------------------------------------------

16. What is a Higher-Order Function?

Answer:
Accepts or returns another function.

------------------------------------------------

17. What is a docstring?

Answer:
Documentation of a function.

------------------------------------------------

18. Can functions be assigned to variables?

Answer:
Yes.

------------------------------------------------

19. Can functions be passed as arguments?

Answer:
Yes.

------------------------------------------------

20. What is function annotation?

Answer:
Type hints for parameters and return values.
"""


# =========================================================
# MINI PROJECT
# =========================================================

def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 35:
        return "Pass"

    return "Fail"


students = {

    "Vinita": 95,

    "Rahul": 82,

    "Amit": 67,

    "Sneha": 91

}

print("\n========== STUDENT REPORT ==========")

for name, marks in students.items():

    print(f"Name  : {name}")

    print(f"Marks : {marks}")

    print(f"Grade : {calculate_grade(marks)}")

    print("-" * 30)


# =========================================================
# END OF FILE
# =========================================================