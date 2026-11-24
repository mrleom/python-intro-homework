# Week 8 - Warmup 3
# Handle a missing file

try:
    with open("../data/missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print('Error: "missing.txt" was not found. Please check the file path and try again.')
