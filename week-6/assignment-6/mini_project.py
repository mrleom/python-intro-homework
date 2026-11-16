
# Week 6 Mini Project: Number Cruncher
# Refactoring Week 5 using functions

numbers = [
    42, 17, 83, 5, 61, 29, 74, 8, 55, 93,
    31, 66, 14, 47, 78, 3, 59, 22, 86, 40
]


# Function 1: Find minimum
def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


# Function 2: Find maximum
def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


# Function 3: Linear search
def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


# Function 4: Bubble sort
def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    n = len(sorted_numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j]
                )

    return sorted_numbers


# Function 5: Display menu
def show_menu():
    print("\n=== NUMBER CRUNCHER ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort numbers")
    print("5. Quit")

    return input("Choose an option (1-5): ")


# Function 6: Main program
def main():
    while True:
        choice = show_menu()

        if choice == "1":
            print("Minimum:", find_min(numbers))

        elif choice == "2":
            print("Maximum:", find_max(numbers))

        elif choice == "3":
            try:
                target = int(input("Enter a number to search for: "))

                index = search(numbers, target)

                if index != -1:
                    print(f"Found at index {index}")
                else:
                    print("Not found")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print("Sorted numbers:", sorted_numbers)

        elif choice == "5":
            print("Thank you for using Number Cruncher!")
            break

        else:
            print("Invalid option. Choose between 1 and 5.")


main()
