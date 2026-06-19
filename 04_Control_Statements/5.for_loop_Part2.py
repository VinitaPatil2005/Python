# =========================================================
#              PYTHON FOR LOOP (PART 2)
# =========================================================

# =========================================================
# break Statement
# =========================================================

"""
break terminates the loop immediately.
"""

for i in range(1, 11):

    if i == 6:
        break

    print(i)

# Output
# 1 2 3 4 5


# =========================================================
# continue Statement
# =========================================================

"""
continue skips the current iteration.
"""

for i in range(1, 11):

    if i == 5:
        continue

    print(i)

# Output
# 1 2 3 4 6 7 8 9 10


# =========================================================
# pass Statement
# =========================================================

"""
pass does nothing.
Used as a placeholder.
"""

for i in range(5):
    pass

print("Loop Finished")


# =========================================================
# else with for Loop
# =========================================================

"""
The else block executes only if the loop
finishes normally (without break).
"""

for i in range(1, 6):

    print(i)

else:

    print("Loop Completed Successfully")


# =========================================================
# else with break
# =========================================================

for i in range(1, 6):

    if i == 3:
        break

    print(i)

else:

    print("This will NOT execute")


# =========================================================
# Print Even Numbers
# =========================================================

for i in range(2, 21, 2):

    print(i)


# =========================================================
# Print Odd Numbers
# =========================================================

for i in range(1, 20, 2):

    print(i)


# =========================================================
# Reverse Counting
# =========================================================

for i in range(20, 0, -1):

    print(i)


# =========================================================
# Sum of Even Numbers
# =========================================================

total = 0

for i in range(2, 21, 2):

    total += i

print("Sum =", total)


# =========================================================
# Prime Number
# =========================================================

number = 29

is_prime = True

if number <= 1:
    is_prime = False

else:

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            is_prime = False
            break

if is_prime:

    print(number, "is Prime")

else:

    print(number, "is NOT Prime")


# =========================================================
# Fibonacci Series
# =========================================================

terms = 10

a = 0
b = 1

print(a)
print(b)

for _ in range(terms - 2):

    c = a + b

    print(c)

    a = b
    b = c


# =========================================================
# Armstrong Number
# =========================================================

number = 153

original = number

digits = len(str(number))

total = 0

for digit in str(number):

    total += int(digit) ** digits

if total == original:

    print("Armstrong Number")

else:

    print("Not Armstrong")


# =========================================================
# Perfect Number
# =========================================================

number = 28

total = 0

for i in range(1, number):

    if number % i == 0:

        total += i

if total == number:

    print("Perfect Number")

else:

    print("Not Perfect")


# =========================================================
# Strong Number
# =========================================================

number = 145

original = number

total = 0

for digit in str(number):

    factorial = 1

    for i in range(1, int(digit) + 1):

        factorial *= i

    total += factorial

if total == original:

    print("Strong Number")

else:

    print("Not Strong")


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

for i in range(1, 6):

    print("*" * i)


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

for i in range(5, 0, -1):

    print("*" * i)


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

for i in range(1, 6):

    for j in range(1, i + 1):

        print(j, end="")

    print()


# =========================================================
# Pattern 4
# =========================================================

"""
11111
2222
333
44
5
"""

for i in range(5, 0, -1):

    print(str(6 - i) * i)


# =========================================================
# END OF PART 2
# =========================================================