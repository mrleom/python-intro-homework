# Week 8 - Warmup 2
# Safe division

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")
else:
    print(f"{numerator} ÷ {denominator} = {result}")
