# =========================================================
#          PYTHON DICTIONARIES (PART 3)
# =========================================================

# =========================================================
# Time Complexity
# =========================================================

"""
Operation                    Complexity

Access Value                 O(1)

Insert                       O(1)

Update                       O(1)

Delete                       O(1)

Search Key                   O(1)

Traversal                    O(n)

Copy                         O(n)
"""

# =========================================================
# Difference Between get() and []
# =========================================================

student = {
    "name": "Vinita"
}

print(student.get("age"))

# Output:
# None

# print(student["age"])

# KeyError


# =========================================================
# Copy vs Assignment
# =========================================================

student1 = {
    "name": "Vinita",
    "age": 21
}

student2 = student1

student2["age"] = 25

print(student1)
print(student2)

"""
Both dictionaries change because
they refer to the same object.
"""


# =========================================================
# copy()
# =========================================================

student1 = {
    "name": "Vinita",
    "age": 21
}

student2 = student1.copy()

student2["age"] = 25

print(student1)
print(student2)

"""
Original dictionary remains unchanged.
"""


# =========================================================
# Real-Life Example
# =========================================================

student = {
    "roll_no": 25,
    "name": "Vinita",
    "branch": "AIML",
    "cgpa": 9.15
}

print(student)

print("Name :", student["name"])

print("CGPA :", student["cgpa"])


# =========================================================
# Nested Dictionary Example
# =========================================================

college = {

    "Student1": {

        "Name": "Vinita",
        "Marks": 90

    },

    "Student2": {

        "Name": "Rahul",
        "Marks": 85

    }

}

for student, details in college.items():

    print(student)

    for key, value in details.items():

        print(key, ":", value)

    print()


# =========================================================
# Dictionary with Loop
# =========================================================

subjects = {

    "Python": 95,

    "Java": 85,

    "SQL": 90

}

for subject, marks in subjects.items():

    print(f"{subject} --> {marks}")


# =========================================================
# Interview Questions
# =========================================================

"""
1. What is a Dictionary?

Answer:
A mutable collection of key-value pairs.

------------------------------------------------

2. Are Dictionaries ordered?

Answer:
Yes (Python 3.7+)

------------------------------------------------

3. Can Dictionary keys be duplicated?

Answer:
No

------------------------------------------------

4. Can values be duplicated?

Answer:
Yes

------------------------------------------------

5. Difference between get() and []?

get()

Returns None

[]

Raises KeyError

------------------------------------------------

6. Which method returns all keys?

Answer:

keys()

------------------------------------------------

7. Which method returns all values?

Answer:

values()

------------------------------------------------

8. Which method returns key-value pairs?

Answer:

items()

------------------------------------------------

9. Which method removes a key?

Answer:

pop()

------------------------------------------------

10. Which method removes the last inserted item?

Answer:

popitem()

------------------------------------------------

11. Which method merges dictionaries?

Answer:

update()

------------------------------------------------

12. Which method copies a dictionary?

Answer:

copy()

------------------------------------------------

13. Which method removes all elements?

Answer:

clear()

------------------------------------------------

14. Which method creates a dictionary from keys?

Answer:

fromkeys()

------------------------------------------------

15. Which method inserts a default value?

Answer:

setdefault()

------------------------------------------------

16. Can a dictionary contain another dictionary?

Answer:
Yes

------------------------------------------------

17. Can a dictionary contain a list?

Answer:
Yes

------------------------------------------------

18. Which operator merges dictionaries in Python 3.9+?

Answer:

|

------------------------------------------------

19. Average time complexity for searching a key?

Answer:

O(1)

------------------------------------------------

20. Which loop is mostly used with dictionaries?

Answer:

for key, value in dictionary.items()

------------------------------------------------

21. Are dictionary keys mutable?

Answer:
No.
Keys must be immutable.

------------------------------------------------

22. Can tuples be dictionary keys?

Answer:
Yes

------------------------------------------------

23. Can lists be dictionary keys?

Answer:
No

------------------------------------------------

24. Which function returns dictionary length?

Answer:

len()

------------------------------------------------

25. How do you check whether a key exists?

Answer:

key in dictionary
"""

# =========================================================
# MINI PROJECT
# =========================================================

students = {

    101: {

        "Name": "Vinita",

        "Marks": 95

    },

    102: {

        "Name": "Rahul",

        "Marks": 88

    },

    103: {

        "Name": "Amit",

        "Marks": 91

    }

}

print("\n========== STUDENT REPORT ==========")

for roll_no, details in students.items():

    print(f"Roll No : {roll_no}")

    print(f"Name    : {details['Name']}")

    print(f"Marks   : {details['Marks']}")

    print("-" * 30)

average = sum(student["Marks"] for student in students.values()) / len(students)

print(f"Class Average : {average:.2f}")

print("=" * 40)


# =========================================================
# CHEAT SHEET
# =========================================================

"""
Create              {}

Access              dict[key]

Safe Access         get()

Keys                keys()

Values              values()

Items               items()

Update              update()

Add                 dict[key] = value

Delete              pop()

Delete Last         popitem()

Clear               clear()

Copy                copy()

Length              len()

Merge               update() or |

Loop                items()

Check Key           key in dict

Dictionary Comprehension

{key:value for ...}
"""


# =========================================================
# END OF FILE
# =========================================================