# Week 7 - Warmup 1
# Read a text file line by line

with open("../data/notes.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(f"Line {number}: {line.strip()}")
