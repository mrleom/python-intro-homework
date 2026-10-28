# Week 5 - Warmup 3: Linear Search

numbers = [8, 15, 3, 12, 20]

target = int(input("Enter a number to search for: "))

found_index = -1

for index in range(len(numbers)):
    print(f"Checking index {index}: {numbers[index]}")

    if numbers[index] == target:
        found_index = index
        break

if found_index != -1:
    print(f"Number {target} found at index {found_index}.")
else:
    print(f"Number {target} was not found.")
