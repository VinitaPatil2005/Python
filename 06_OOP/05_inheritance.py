"""
=========================================================
                PYTHON INHERITANCE
=========================================================

What is Inheritance?
--------------------

Inheritance is an OOP concept where one class
(child class) acquires the properties and methods
of another class (parent class).

Advantages
----------
✔ Code Reusability
✔ Easy Maintenance
✔ Less Code Duplication
✔ Extensibility

Syntax

class Parent:
    ...

class Child(Parent):
    ...
"""

# =========================================================
# Single Inheritance
# =========================================================

class Animal:

    def eat(self):
        print("Animal is Eating")


class Dog(Animal):

    def bark(self):
        print("Dog is Barking")


dog = Dog()

dog.eat()
dog.bark()


# =========================================================
# Multilevel Inheritance
# =========================================================

class Grandparent:

    def house(self):
        print("Grandparent's House")


class Parent(Grandparent):

    def car(self):
        print("Parent's Car")


class Child(Parent):

    def bike(self):
        print("Child's Bike")


child = Child()

child.house()
child.car()
child.bike()


# =========================================================
# Multiple Inheritance
# =========================================================

class Father:

    def skills(self):
        print("Driving")


class Mother:

    def talent(self):
        print("Cooking")


class Son(Father, Mother):

    pass


son = Son()

son.skills()
son.talent()


# =========================================================
# Hierarchical Inheritance
# =========================================================

class Person:

    def show(self):
        print("I am a Person")


class Student(Person):

    pass


class Teacher(Person):

    pass


student = Student()
teacher = Teacher()

student.show()
teacher.show()


# =========================================================
# Hybrid Inheritance
# =========================================================

"""
Hybrid inheritance is a combination of
multiple inheritance types.

Python supports it,
but it is generally used in larger projects.
"""


# =========================================================
# super() Function
# =========================================================

"""
super() calls the parent class constructor
or methods.
"""

class Animal:

    def __init__(self):

        print("Animal Constructor")


class Dog(Animal):

    def __init__(self):

        super().__init__()

        print("Dog Constructor")


dog = Dog()


# =========================================================
# Method Overriding
# =========================================================

"""
A child class provides its own implementation
of a parent class method.
"""

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog = Dog()

dog.sound()


# =========================================================
# Method Resolution Order (MRO)
# =========================================================

"""
MRO determines the order in which
Python searches for methods.

Use:

ClassName.mro()
"""

print(Son.mro())


# =========================================================
# isinstance() and issubclass()
# =========================================================

print(isinstance(dog, Dog))        # True

print(isinstance(dog, Animal))     # True

print(issubclass(Dog, Animal))     # True


# =========================================================
# Types of Inheritance
# =========================================================

"""
1. Single

Parent
   |
 Child

------------------------

2. Multilevel

Grandparent
     |
 Parent
     |
 Child

------------------------

3. Multiple

Father   Mother
     \   /
      Child

------------------------

4. Hierarchical

      Parent
      /   \
 Child1 Child2

------------------------

5. Hybrid

Combination of multiple types.
"""


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is inheritance?

Acquiring properties of another class.

-----------------------------------

2. Why use inheritance?

Code reusability.

-----------------------------------

3. Which function calls parent constructor?

super()

-----------------------------------

4. What is method overriding?

Child class redefining parent method.

-----------------------------------

5. What is MRO?

Method Resolution Order.

-----------------------------------

6. Difference between isinstance() and issubclass()?

isinstance()

Checks object.

issubclass()

Checks class.
"""


# =========================================================
# Mini Project
# =========================================================

class Vehicle:

    def start(self):

        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):

        print("Car is Driving")


car = Car()

car.start()

car.drive()


# =========================================================
# Cheat Sheet
# =========================================================

"""
Inheritance

class Child(Parent)

------------------------

super()

Calls parent constructor

------------------------

Method Overriding

Child redefines method

------------------------

MRO

ClassName.mro()

------------------------

Types

Single

Multilevel

Multiple

Hierarchical

Hybrid
"""

# =========================================================
# END OF FILE
# =========================================================