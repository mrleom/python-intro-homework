
# Week 5 - Warmup 3: Linear Search

# List of names
names = ["Leo", "Mia", "Carlos", "Marcus", "Sara"]

# Ask the user for a name
target = input("Enter a name to search for: ")

# -1 means the name has not been found
found_index = -1

# Search through the list one name at a time
for index in range(len(names)):
    if names[index] == target:
        found_index = index
        break

# Display the result
if found_index != -1:
    print(f'Found "{target}" at index {found_index}.')
else:
    print(f'"{target}" was not found in the list.')
