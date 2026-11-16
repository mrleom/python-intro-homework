# Week 4 - Warmup 2: Dictionary Operations

student = {
    "name": "Jason",
    "grade": 90,
    "subjects": ["Sports Science", "Math", "Physical Education"]
}

print(student["name"])
print(student["grade"])

print("\nAll student information:")

for key, value in student.items():
    print(key, ":", value)

student["graduated"] = False

print("\nUpdated student dictionary:")
print(student)
