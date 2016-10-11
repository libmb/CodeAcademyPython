# challenge lesson
# lesson one; create three dictionaries with given names and keys:

# what's the score; add homework quiz and test scores to dictionary:

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# put it together; put three dictionaries in list together:
students = [lloyd, alice, tyler]

# for the record; for each student in students list print out student data:
# this took awhile
for x in students:
    print(x["name"])
    print(x["homework"])
    print(x["quizzes"])
    print(x["tests"])

# it's okay to be average; write a function average that takes a list of numbers and returns the average


def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
