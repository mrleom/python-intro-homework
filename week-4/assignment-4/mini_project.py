# Week 4 - Mini Project: Student Roster Analyzer

# Student data provided by Code the Dream
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

print("Total students:", len(students))
print("First student:", students[0]["name"])

# Find the highest-scoring student without max()

top_student = students[0]

for student in students:
    if student["score"] > top_student["score"]:
        top_student = student

print("Top student:", top_student["name"])
print("Highest score:", top_student["score"])

# Calculate the average score

total_score = 0

for student in students:
    total_score += student["score"]

average_score = total_score / len(students)

print("Total score:", total_score)
print("Average score:", average_score)

# Find all unique subjects

unique_subjects = set()

for student in students:
    unique_subjects.add(student["subject"])

print("Unique subjects:", unique_subjects)

# Find students with scores above 75

high_scorers = []

for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print("Students above 75:", high_scorers)
