# =========================================================
#              PYTHON WHILE LOOP (PART 2)
# =========================================================

# =========================================================
# break Statement
# =========================================================

"""
break immediately terminates the loop.
"""

i = 1

while i <= 10:

    if i == 6:
        break

    print(i)

    i += 1

# Output
# 1 2 3 4 5


# =========================================================
# continue Statement
# =========================================================

"""
continue skips the current iteration.
"""

i = 0

while i < 10:

    i += 1

    if i == 5:
        continue

    print(i)

# Output
# 1 2 3 4 6 7 8 9 10


# =========================================================
# pass Statement
# =========================================================

"""
pass is a placeholder statement.
"""

i = 1

while i <= 5:

    pass

    print(i)

    i += 1


# =========================================================
# while...else
# =========================================================

"""
The else block executes only if the loop
ends normally (without break).
"""

i = 1

while i <= 5:

    print(i)

    i += 1

else:

    print("Loop Completed Successfully")


# =========================================================
# while...else with break
# =========================================================

i = 1

while i <= 5:

    if i == 3:
        break

    print(i)

    i += 1

else:

    print("This will NOT execute")


# =========================================================
# Palindrome Number
# =========================================================

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


# =========================================================
# Armstrong Number
# =========================================================

number = 153

original = number

digits = len(str(number))

total = 0

while number > 0:

    digit = number % 10

    total += digit ** digits

    number //= 10

if total == original:

    print("Armstrong Number")

else:

    print("Not Armstrong")


# =========================================================
# Prime Number
# =========================================================

number = 29

divisor = 2

is_prime = True

while divisor <= number // 2:

    if number % divisor == 0:

        is_prime = False

        break

    divisor += 1

if number <= 1:

    print("Not Prime")

elif is_prime:

    print("Prime Number")

else:

    print("Not Prime")


# =========================================================
# Perfect Number
# =========================================================

number = 28

i = 1

total = 0

while i < number:

    if number % i == 0:

        total += i

    i += 1

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

while number > 0:

    digit = number % 10

    factorial = 1

    i = 1

    while i <= digit:

        factorial *= i

        i += 1

    total += factorial

    number //= 10

if total == original:

    print("Strong Number")

else:

    print("Not Strong")


# =========================================================
# Number Guessing Game
# =========================================================

"""
Uncomment to play

secret = 7

guess = 0

while guess != secret:

    guess = int(input("Enter Guess: "))

    if guess < secret:

        print("Too Small")

    elif guess > secret:

        print("Too Large")

print("Correct Guess!")
"""


# =========================================================
# Login System
# =========================================================

"""
Uncomment to test

username = "admin"

password = "python"

attempts = 3

while attempts > 0:

    user = input("Username: ")

    pwd = input("Password: ")

    if user == username and pwd == password:

        print("Login Successful")

        break

    else:

        attempts -= 1

        print("Attempts Left:", attempts)

else:

    print("Account Locked")
"""


# =========================================================
# ATM Simulation
# =========================================================

"""
Uncomment to test

balance = 10000

while True:

    print("\n1. Check Balance")

    print("2. Withdraw")

    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        print("Balance =", balance)

    elif choice == 2:

        amount = int(input("Enter Amount: "))

        if amount <= balance:

            balance -= amount

            print("Withdraw Successful")

        else:

            print("Insufficient Balance")

    elif choice == 3:

        print("Thank You!")

        break

    else:

        print("Invalid Choice")
"""


# =========================================================
# Menu Driven Program
# =========================================================

"""
Uncomment to test

while True:

    print("\n1. Addition")

    print("2. Subtraction")

    print("3. Exit")

    choice = int(input("Choice: "))

    if choice == 1:

        print(10 + 20)

    elif choice == 2:

        print(20 - 10)

    elif choice == 3:

        break

    else:

        print("Invalid Choice")
"""


# =========================================================
# END OF PART 2
# =========================================================