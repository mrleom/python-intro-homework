# Week 4 - Warmup 3: Set Operations

# Programming languages used by two sports analytics teams
student_a = ["Python", "Java", "C++"]
student_b = ["Python", "JavaScript", "Java"]

set_a = set(student_a)
set_b = set(student_b)

print("Team A:", set_a)
print("Team B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
