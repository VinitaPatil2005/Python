"""
=========================================================
                PYTHON ABSTRACTION
=========================================================

What is Abstraction?
--------------------

Abstraction means hiding implementation details
and showing only the essential features.

Example:
When you drive a car, you use the steering wheel,
accelerator, and brake. You don't need to know
how the engine works internally.

In Python, abstraction is implemented using the
ABC (Abstract Base Class) module.
"""

from abc import ABC, abstractmethod

# =========================================================
# Abstract Class
# =========================================================

"""
An abstract class cannot be instantiated.

It may contain:
1. Abstract methods
2. Normal methods
"""

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# animal = Animal()   ❌ Error


# =========================================================
# Implementing Abstract Method
# =========================================================

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
# Abstract Class with Normal Method
# =========================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle Stopped")


class Car(Vehicle):

    def start(self):
        print("Car Started")


car = Car()

car.start()
car.stop()


# =========================================================
# Real World Example
# =========================================================

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")


payments = [

    CreditCard(),

    UPI()

]

for payment in payments:

    payment.pay()


# =========================================================
# Why Use Abstraction?
# =========================================================

"""
✔ Hides unnecessary details

✔ Improves security

✔ Makes code cleaner

✔ Forces child classes to implement methods
"""


# =========================================================
# Difference
# =========================================================

"""
Abstraction

Hides implementation.

Focuses on WHAT to do.

----------------------------

Encapsulation

Hides data.

Focuses on HOW data is protected.
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is Abstraction?

Hiding implementation details.

------------------------------------

2. Which module is used?

abc

------------------------------------

3. What is an Abstract Class?

A class that cannot be instantiated.

------------------------------------

4. Which decorator is used?

@abstractmethod

------------------------------------

5. Can an abstract class have normal methods?

Yes.

------------------------------------

6. Can we create an object of an abstract class?

No.

------------------------------------

7. Why is abstraction used?

To provide a common interface and hide implementation.
"""


# =========================================================
# Mini Project
# =========================================================

class Shape(ABC):

    @abstractmethod
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


rectangle = Rectangle(10, 5)
circle = Circle(7)

print("\nRectangle Area :", rectangle.area())
print("Circle Area    :", round(circle.area(), 2))


# =========================================================
# Cheat Sheet
# =========================================================

"""
Import

from abc import ABC, abstractmethod

----------------------------

Abstract Class

class Demo(ABC):

----------------------------

Abstract Method

@abstractmethod

def show(self):
    pass

----------------------------

Child Class

Must implement all abstract methods.

----------------------------

Cannot Create Object

obj = Demo() ❌
"""

# =========================================================
# END OF FILE
# =========================================================