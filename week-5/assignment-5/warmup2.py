# Week 5 - Warmup 2: Input Validation

number = 0

while number <= 0:
    try:
        number = int(input("Enter a positive integer: "))

        if number <= 0:
            print("That's not a positive integer. Try again.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

print(f"Got it: {number}")
