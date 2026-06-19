# =========================================================
#              PYTHON RECURSION (PART 2)
# =========================================================

# =========================================================
# Greatest Common Divisor (GCD)
# =========================================================

"""
Euclidean Algorithm

GCD(a, b)

If b becomes 0,
then a is the GCD.
"""

def gcd(a, b):

    if b == 0:

        return a

    return gcd(b, a % b)

print(gcd(48, 18))

# Output
# 6


# =========================================================
# Decimal to Binary
# =========================================================

"""
Converts a decimal number
into binary using recursion.
"""

def decimal_to_binary(number):

    if number == 0:

        return ""

    return decimal_to_binary(number // 2) + str(number % 2)

number = 25

binary = decimal_to_binary(number)

print(binary)

# Output
# 11001


# =========================================================
# Palindrome using Recursion
# =========================================================

def palindrome(text):

    if len(text) <= 1:

        return True

    if text[0] != text[-1]:

        return False

    return palindrome(text[1:-1])

print(palindrome("madam"))

print(palindrome("python"))

# Output
# True
# False


# =========================================================
# Binary Search using Recursion
# =========================================================

"""
Binary Search works only on
a sorted list.
"""

def binary_search(numbers, target, left, right):

    if left > right:

        return -1

    mid = (left + right) // 2

    if numbers[mid] == target:

        return mid

    elif target < numbers[mid]:

        return binary_search(

            numbers,

            target,

            left,

            mid - 1

        )

    else:

        return binary_search(

            numbers,

            target,

            mid + 1,

            right

        )

numbers = [10,20,30,40,50,60,70]

index = binary_search(

    numbers,

    40,

    0,

    len(numbers)-1

)

print(index)

# Output
# 3


# =========================================================
# Tower of Hanoi
# =========================================================

"""
Move n disks

Source

Destination

Auxiliary
"""

def tower_of_hanoi(disks, source, destination, auxiliary):

    if disks == 1:

        print(

            f"Move Disk 1 from "

            f"{source} to {destination}"

        )

        return

    tower_of_hanoi(

        disks - 1,

        source,

        auxiliary,

        destination

    )

    print(

        f"Move Disk {disks} "

        f"from {source} to {destination}"

    )

    tower_of_hanoi(

        disks - 1,

        auxiliary,

        destination,

        source

    )

tower_of_hanoi(3, "A", "C", "B")


# =========================================================
# Print List using Recursion
# =========================================================

def print_list(data, index=0):

    if index == len(data):

        return

    print(data[index])

    print_list(data, index + 1)

numbers = [10,20,30,40]

print_list(numbers)


# =========================================================
# Find Maximum using Recursion
# =========================================================

def maximum(numbers):

    if len(numbers) == 1:

        return numbers[0]

    largest = maximum(numbers[1:])

    return numbers[0] if numbers[0] > largest else largest

print(maximum([20, 5, 90, 40, 60]))

# Output
# 90


# =========================================================
# Find Minimum using Recursion
# =========================================================

def minimum(numbers):

    if len(numbers) == 1:

        return numbers[0]

    smallest = minimum(numbers[1:])

    return numbers[0] if numbers[0] < smallest else smallest

print(minimum([20, 5, 90, 40, 60]))

# Output
# 5


# =========================================================
# Call Stack Example
# =========================================================

"""
factorial(3)

↓

factorial(2)

↓

factorial(1)

↓

Return 1

↓

Return 2

↓

Return 6

Every recursive call is stored
inside the Call Stack.
"""


# =========================================================
# Recursion Tree (Factorial)
# =========================================================

"""
factorial(4)

4 * factorial(3)

        |

3 * factorial(2)

        |

2 * factorial(1)

        |

1

Returns

1

2

6

24
"""

# =========================================================
# END OF PART 2
# =========================================================