# =========================================================
#           PYTHON IF...ELSE (PART 2)
# =========================================================

# =========================================================
# Logical Operators with if
# =========================================================

"""
Logical Operators

and

Returns True only if both conditions are True.

or

Returns True if at least one condition is True.

not

Reverses the result.
"""

age = 22
salary = 60000

if age >= 18 and salary >= 50000:
    print("Eligible for Premium Loan")

# Output:
# Eligible for Premium Loan


# =========================================================
# OR Operator
# =========================================================

marks = 85
sports = True

if marks >= 90 or sports:
    print("Eligible for Scholarship")

# Output:
# Eligible for Scholarship


# =========================================================
# NOT Operator
# =========================================================

is_raining = False

if not is_raining:
    print("Go for a Walk")

# Output:
# Go for a Walk


# =========================================================
# Membership Operator
# =========================================================

languages = ["Python", "Java", "C++"]

if "Python" in languages:
    print("Python Found")

if "SQL" not in languages:
    print("SQL Not Found")


# =========================================================
# Identity Operator
# =========================================================

list1 = [1, 2, 3]

list2 = list1

list3 = [1, 2, 3]

if list1 is list2:
    print("Same Object")

if list1 == list3:
    print("Same Values")


# =========================================================
# Positive / Negative Number
# =========================================================

num = -15

if num > 0:
    print("Positive")

elif num < 0:
    print("Negative")

else:
    print("Zero")


# =========================================================
# Even / Odd
# =========================================================

number = 18

if number % 2 == 0:
    print("Even")

else:
    print("Odd")


# =========================================================
# Largest of Two Numbers
# =========================================================

a = 40
b = 75

if a > b:
    print("Largest =", a)

else:
    print("Largest =", b)


# =========================================================
# Largest of Three Numbers
# =========================================================

a = 20
b = 70
c = 50

if a >= b and a >= c:
    largest = a

elif b >= a and b >= c:
    largest = b

else:
    largest = c

print("Largest =", largest)


# =========================================================
# Smallest of Three Numbers
# =========================================================

a = 20
b = 10
c = 30

if a <= b and a <= c:
    smallest = a

elif b <= a and b <= c:
    smallest = b

else:
    smallest = c

print("Smallest =", smallest)


# =========================================================
# Leap Year
# =========================================================

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")

else:
    print(year, "is NOT a Leap Year")


# =========================================================
# Grade Calculator
# =========================================================

marks = 82

if marks >= 90:
    grade = "A+"

elif marks >= 80:
    grade = "A"

elif marks >= 70:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 35:
    grade = "D"

else:
    grade = "Fail"

print("Grade =", grade)


# =========================================================
# Voting Eligibility
# =========================================================

age = 19

if age >= 18:
    print("Eligible to Vote")

else:
    print("Not Eligible")


# =========================================================
# Driving License Eligibility
# =========================================================

age = 21
has_documents = True

if age >= 18 and has_documents:
    print("Driving License Approved")

else:
    print("Driving License Rejected")


# =========================================================
# Login System
# =========================================================

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")

else:
    print("Invalid Credentials")


# =========================================================
# ATM Withdrawal
# =========================================================

balance = 15000
withdraw = 3000

if withdraw <= balance:
    balance -= withdraw
    print("Transaction Successful")
    print("Remaining Balance =", balance)

else:
    print("Insufficient Balance")


# =========================================================
# Electricity Bill
# =========================================================

units = 180

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = units * 7

else:
    bill = units * 10

print("Electricity Bill =", bill)


# =========================================================
# BMI Calculator
# =========================================================

weight = 68
height = 1.72

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal")

elif bmi < 30:
    print("Overweight")

else:
    print("Obese")


# =========================================================
# Calculator
# =========================================================

num1 = 25
num2 = 10

operator = "+"

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("Invalid Operator")


# =========================================================
# END OF PART 2
# =========================================================