# Week 7 - Warmup 2
# Read a CSV file using DictReader

import csv

with open("../data/students.csv", "r", newline="") as file:
    students = csv.DictReader(file)

    for student in students:
        print(f"{student['name']}: {student['score']}")
