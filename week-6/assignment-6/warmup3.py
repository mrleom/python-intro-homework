
# Example 1: Local variable scope

def show_player():
    player = "Marcus"
    print("Inside function:", player)


show_player()

# Trying to access player outside the function
# causes this error:
# NameError: name 'player' is not defined

# print(player)


# Example 2: Solving the problem with return

def get_player():
    player = "Marcus"
    return player


player_name = get_player()

print("Outside function:", player_name)
