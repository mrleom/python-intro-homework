
# Week 3 - Mini Project: Day Planner
# Code the Dream - Python Intro 26.4

# Step 1: Ask the user for the day and time
day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

print("Day:", day)
print("Time:", time)

# Step 2: Friday activities
if day == "friday" and time == "morning":
    print("Suggestion: Go for a morning jog.")

elif day == "friday" and time == "afternoon":
    print("Suggestion: Practice Python for one hour.")

elif day == "friday" and time == "evening":
    print("Suggestion: Enjoy a movie with your family.")

# Step 3: Saturday activities
elif day == "saturday" and time == "morning":
    print("Suggestion: Play soccer with friends.")

elif day == "saturday" and time == "afternoon":
    print("Suggestion: Visit a park with your family.")

elif day == "saturday" and time == "evening":
    print("Suggestion: Cook a delicious dinner.")

# Step 4: Sunday activities
elif day == "sunday" and time == "morning":
    print("Suggestion: Enjoy breakfast with your family.")

elif day == "sunday" and time == "afternoon":
    print("Suggestion: Go for a bike ride.")

elif day == "sunday" and time == "evening":
    print("Suggestion: Prepare your schedule for next week.")

# Step 5: Handle unrecognized days and times
elif day not in ("friday", "saturday", "sunday"):
    print("Sorry, I don't recognize that day. Try Friday, Saturday, or Sunday.")

else:
    print("Sorry, I don't recognize that time. Try morning, afternoon, or evening.")
