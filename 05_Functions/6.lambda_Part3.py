# =========================================================
#          PYTHON LAMBDA FUNCTIONS (PART 3)
# =========================================================

# =========================================================
# Lambda vs Normal Function
# =========================================================

"""
Normal Function

- Has a name
- Multiple statements
- Uses return keyword

Example

def square(x):
    return x * x

------------------------------------------

Lambda Function

- Anonymous
- One expression only
- Automatically returns result

Example

square = lambda x: x * x
"""

# =========================================================
# Time Complexity
# =========================================================

"""
Operation                         Complexity

Lambda Function                   O(1)

map()                             O(n)

filter()                          O(n)

reduce()                          O(n)

sorted()                          O(n log n)

max()/min()                       O(n)

any()                             O(n)

all()                             O(n)
"""


# =========================================================
# Real World Example
# =========================================================

students = [

    {"name": "Vinita", "marks": 92},

    {"name": "Rahul", "marks": 78},

    {"name": "Amit", "marks": 85},

    {"name": "Sneha", "marks": 95}

]

# Students scoring above 80

top_students = list(

    filter(

        lambda student: student["marks"] > 80,

        students

    )

)

print(top_students)


# =========================================================
# Employee Salary Increment
# =========================================================

salary = [30000, 45000, 50000, 70000]

updated_salary = list(

    map(

        lambda amount: amount * 1.10,

        salary

    )

)

print(updated_salary)


# =========================================================
# Highest Scoring Student
# =========================================================

highest = max(

    students,

    key=lambda student: student["marks"]

)

print(highest)


# =========================================================
# Lowest Scoring Student
# =========================================================

lowest = min(

    students,

    key=lambda student: student["marks"]

)

print(lowest)


# =========================================================
# Sort by Length
# =========================================================

languages = [

    "Python",

    "C",

    "Java",

    "JavaScript",

    "SQL"

]

languages.sort(

    key=lambda language: len(language)

)

print(languages)


# =========================================================
# Custom Sorting
# =========================================================

numbers = [5, -8, 2, -10, 1]

numbers.sort(

    key=lambda number: abs(number)

)

print(numbers)

# Output
# [1,2,5,-8,-10]


# =========================================================
# Chaining Operations
# =========================================================

numbers = range(1, 21)

result = list(

    map(

        lambda x: x ** 2,

        filter(

            lambda x: x % 2 == 0,

            numbers

        )

    )

)

print(result)


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a lambda function?

Answer:
An anonymous function.

------------------------------------------------

2. Can lambda contain multiple statements?

Answer:
No.

------------------------------------------------

3. Can lambda have multiple arguments?

Answer:
Yes.

------------------------------------------------

4. Does lambda use return?

Answer:
No.
It returns automatically.

------------------------------------------------

5. Difference between lambda and normal function?

Normal Function

Named

Multiple statements

Uses return

Lambda

Anonymous

One expression

Automatic return

------------------------------------------------

6. Which module contains reduce()?

Answer:

functools

------------------------------------------------

7. What does map() return?

Answer:
A map object.

------------------------------------------------

8. What does filter() return?

Answer:
A filter object.

------------------------------------------------

9. Why use list() with map()?

Answer:
To convert the iterator into a list.

------------------------------------------------

10. Which function combines all values?

Answer:

reduce()

------------------------------------------------

11. Which function transforms data?

Answer:

map()

------------------------------------------------

12. Which function filters data?

Answer:

filter()

------------------------------------------------

13. Which function checks at least one True value?

Answer:

any()

------------------------------------------------

14. Which function checks all True values?

Answer:

all()

------------------------------------------------

15. Can lambda return Boolean values?

Answer:
Yes.

------------------------------------------------

16. Can lambda be stored in variables?

Answer:
Yes.

------------------------------------------------

17. Can lambda be passed as an argument?

Answer:
Yes.

------------------------------------------------

18. Which function performs custom sorting?

Answer:

sorted()

or

sort()

------------------------------------------------

19. Which keyword creates a lambda?

Answer:

lambda

------------------------------------------------

20. Is lambda faster than normal functions?

Answer:
No significant difference.
Choose based on readability.
"""


# =========================================================
# MINI PROJECT
# =========================================================

students = [

    {"name": "Vinita", "marks": 95},

    {"name": "Rahul", "marks": 82},

    {"name": "Amit", "marks": 91},

    {"name": "Sneha", "marks": 76}

]

print("\n========== STUDENT REPORT ==========")

# Sort by Marks

students.sort(

    key=lambda student: student["marks"],

    reverse=True

)

for student in students:

    print(

        f"{student['name']:10}"

        f" {student['marks']}"

    )

average = sum(

    map(

        lambda student: student["marks"],

        students

    )

) / len(students)

print("-" * 35)

print(f"Average Marks : {average:.2f}")

highest = max(

    students,

    key=lambda student: student["marks"]

)

print(f"Topper : {highest['name']}")

print("=" * 40)


# =========================================================
# END OF FILE
# =========================================================