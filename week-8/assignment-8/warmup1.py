# Week 8 - Warmup 1
# Validate numeric input

while True:
    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("That's not a valid number. Try again.")
    else:
        print(f"You entered: {number}")
        break
