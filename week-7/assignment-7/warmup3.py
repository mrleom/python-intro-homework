# Week 7 - Warmup 3
# Working with the os module

import os

# 1. Display the current working directory
print("Current directory:", os.getcwd())

# 2. Check whether expenses.csv exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# 3. Build the file path using os.path.join()
file_path = os.path.join("..", "data", "expenses.csv")
print("File path:", file_path)
