# Week 7 - Mini Project
# Expense Report Generator

import csv
import os
from datetime import datetime

# Step 1: Check if the data file exists
file_path = "../data/expenses.csv"

if not os.path.exists(file_path):
    print("Error: expenses.csv not found.")
else:
    # Step 2: Read the CSV into a list of dictionaries
    expenses = []

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Step 3: Convert the amount to a number
            row["amount"] = float(row["amount"])
            expenses.append(row)

    # Step 4: Filter expenses in the Food category
    food_expenses = []

    for expense in expenses:
        if expense["category"] == "Food":
            food_expenses.append(expense)

    # Step 5: Calculate the total
    total = 0

    for expense in food_expenses:
        total += expense["amount"]

    # Step 6: Write the report
    today = datetime.now().strftime("%B %d, %Y")

    with open("food_report.txt", "w") as report:
        report.write(
            f"Food Expense Report - generated {today}\n"
        )

        for expense in food_expenses:
            report.write(
                f"{expense['date']}: ${expense['amount']:.2f}\n"
            )

        report.write(f"Total: ${total:.2f}\n")

    print("Food expense report generated successfully.")
