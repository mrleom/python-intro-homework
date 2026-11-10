
def is_valid_score(score):
    return type(score) is int and 0 <= score <= 100


try:
    score = int(input("Enter a score between 0 and 100: "))

    if is_valid_score(score):
        print("Valid score.")
    else:
        print("Invalid score - must be between 0 and 100.")

except ValueError:
    print("Invalid score - please enter a whole number.")
