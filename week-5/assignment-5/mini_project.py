
# Week 5 - Mini Project: Number Cruncher

# Original data provided by Code the Dream
numbers = [
    42, 17, 83, 5, 61, 29, 74, 8, 55, 93,
    31, 66, 14, 47, 78, 3, 59, 22, 86, 40
]

# Main menu
while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    # Option 1: Find minimum
    if choice == "1":
        smallest = numbers[0]

        for number in numbers:
            if number < smallest:
                smallest = number

        print(f"The minimum number is: {smallest}")

    # Option 2: Find maximum
    elif choice == "2":
        largest = numbers[0]

        for number in numbers:
            if number > largest:
                largest = number

        print(f"The maximum number is: {largest}")

    # Option 3: Search for a number
    elif choice == "3":
        try:
            target = int(input("Enter a number to search for: "))

            found_index = -1

            for index in range(len(numbers)):
                if numbers[index] == target:
                    found_index = index
                    break

            if found_index != -1:
                print(f"Number {target} found at index {found_index}.")
            else:
                print(f"Number {target} was not found.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Option 4: Bubble Sort
    elif choice == "4":
        swapped = True

        while swapped:
            swapped = False

            for index in range(len(numbers) - 1):
                if numbers[index] > numbers[index + 1]:
                    numbers[index], numbers[index + 1] = (
                        numbers[index + 1], numbers[index]
                    )
                    swapped = True

        print(f"Sorted numbers: {numbers}")

    # Option 5: Quit
    elif choice == "5":
        print("Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid option. Please choose a number from 1 to 5.")
