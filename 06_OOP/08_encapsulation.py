"""
=========================================================
              PYTHON ENCAPSULATION
=========================================================

What is Encapsulation?
----------------------

Encapsulation means wrapping data (variables)
and methods (functions) into a single unit (class).

It also restricts direct access to data to
protect it from accidental modification.

Python supports:

1. Public Members
2. Protected Members
3. Private Members
"""

# =========================================================
# Public Members
# =========================================================

"""
Public members can be accessed from anywhere.
"""

class Student:

    def __init__(self, name):

        self.name = name

student = Student("Vinita")

print(student.name)


# =========================================================
# Protected Members
# =========================================================

"""
Protected members start with a single underscore (_).

They should be accessed only inside the class
or child classes.

(It is a convention, not strict protection.)
"""

class Employee:

    def __init__(self):

        self._salary = 50000

employee = Employee()

print(employee._salary)


# =========================================================
# Private Members
# =========================================================

"""
Private members start with double underscores (__).

Python performs name mangling to make them
harder to access directly.
"""

class BankAccount:

    def __init__(self):

        self.__balance = 10000

    def show_balance(self):

        print("Balance =", self.__balance)

account = BankAccount()

account.show_balance()

# print(account.__balance)   - Error


# =========================================================
# Name Mangling
# =========================================================

"""
Private variables can still be accessed
using name mangling.
(Not recommended in real projects.)
"""

print(account._BankAccount__balance)


# =========================================================
# Getter Method
# =========================================================

class Student:

    def __init__(self):

        self.__marks = 95

    def get_marks(self):

        return self.__marks

student = Student()

print(student.get_marks())


# =========================================================
# Setter Method
# =========================================================

class Student:

    def __init__(self):

        self.__marks = 0

    def set_marks(self, marks):

        if 0 <= marks <= 100:

            self.__marks = marks

        else:

            print("Invalid Marks")

    def get_marks(self):

        return self.__marks

student = Student()

student.set_marks(90)

print(student.get_marks())


# =========================================================
# Property Decorator
# =========================================================

"""
@property allows getter methods
to be accessed like variables.
"""

class Circle:

    def __init__(self, radius):

        self.radius = radius

    @property
    def area(self):

        return 3.14 * self.radius ** 2

circle = Circle(7)

print(circle.area)


# =========================================================
# Advantages
# =========================================================

"""
- Data Security
- Better Control
- Easy Maintenance
- Prevents Invalid Data
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is Encapsulation?

Wrapping data and methods together.

------------------------------------

2. Types of access modifiers?

Public

Protected

Private

------------------------------------

3. Symbol for protected member?

_single

------------------------------------

4. Symbol for private member?

__double

------------------------------------

5. What is Name Mangling?

Python changes private variable names
internally.

------------------------------------

6. Why use Getter and Setter?

To safely read and modify private data.

------------------------------------

7. What is @property?

Converts a method into a read-only property.
"""


# =========================================================
# Mini Project
# =========================================================

class ATM:

    def __init__(self):

        self.__balance = 5000

    def deposit(self, amount):

        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

        else:

            print("Insufficient Balance")

    def balance(self):

        print("Balance =", self.__balance)

atm = ATM()

atm.deposit(1000)

atm.withdraw(2000)

atm.balance()


# =========================================================
# END OF FILE
# =========================================================