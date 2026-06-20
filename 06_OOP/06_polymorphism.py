"""
=========================================================
            PYTHON POLYMORPHISM
=========================================================

What is Polymorphism?
---------------------

Polymorphism means "Many Forms".

The same method or function can perform
different tasks depending on the object.

Types of Polymorphism in Python

1. Method Overriding
2. Operator Overloading
3. Duck Typing
"""

# =========================================================
# Method Overriding
# =========================================================

class Animal:

    def sound(self):

        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):

        print("Dog Barks")


class Cat(Animal):

    def sound(self):

        print("Cat Meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# =========================================================
# Runtime Polymorphism
# =========================================================

class Bird:

    def fly(self):

        print("Bird is Flying")


class Eagle(Bird):

    def fly(self):

        print("Eagle flies very high")


bird = Eagle()
bird.fly()


# =========================================================
# Duck Typing
# =========================================================

"""
"If it walks like a duck and
quacks like a duck,
it is a duck."

Python checks behavior,
not the object type.
"""

class Laptop:

    def start(self):

        print("Laptop Started")


class Car:

    def start(self):

        print("Car Started")


def begin(device):

    device.start()


begin(Laptop())
begin(Car())


# =========================================================
# Operator Overloading
# =========================================================

"""
Operators behave differently
for different data types.
"""

print(10 + 20)

print("Hello " + "Python")

print([1, 2] + [3, 4])


# =========================================================
# len() Polymorphism
# =========================================================

print(len("Python"))

print(len([10, 20, 30]))

print(len({"a": 1, "b": 2}))


# =========================================================
# Function Polymorphism
# =========================================================

def add(a, b):

    return a + b


print(add(10, 20))

print(add("Hello ", "World"))

print(add([1, 2], [3, 4]))


# =========================================================
# Real World Example
# =========================================================

class Payment:

    def pay(self):

        print("Payment Processing")


class CreditCard(Payment):

    def pay(self):

        print("Paid using Credit Card")


class UPI(Payment):

    def pay(self):

        print("Paid using UPI")


payments = [CreditCard(), UPI()]

for payment in payments:

    payment.pay()


# =========================================================
# Advantages
# =========================================================

"""
✔ Code Reusability

✔ Easy Extension

✔ Cleaner Code

✔ Flexibility
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is Polymorphism?

One interface,
multiple implementations.

-----------------------------------

2. Types of Polymorphism?

Method Overriding

Operator Overloading

Duck Typing

-----------------------------------

3. What is Method Overriding?

Child class provides its own
implementation.

-----------------------------------

4. What is Duck Typing?

Python checks object behavior
instead of object type.

-----------------------------------

5. Give an example of
Operator Overloading.

+

Works for

Numbers

Strings

Lists
"""


# =========================================================
# Mini Project
# =========================================================

class Shape:

    def area(self):

        pass


class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return 3.14 * self.radius ** 2


shapes = [

    Rectangle(10, 5),

    Circle(7)

]

print("\n========== AREAS ==========")

for shape in shapes:

    print(shape.area())


# =========================================================
# Cheat Sheet
# =========================================================

"""
Polymorphism

One Interface

Many Forms

-----------------------

Method Overriding

Child changes parent method

-----------------------

Duck Typing

Checks behavior

-----------------------

Operator Overloading

+  *  ==

Different behavior

-----------------------

Example

Dog.sound()

Cat.sound()
"""

# =========================================================
# END OF FILE
# =========================================================