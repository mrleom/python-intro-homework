
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# Only a name
greet("Jason")

# Name and custom greeting
greet("Jason", "Good morning")

# Greeting as a keyword argument
greet("Jason", greeting="Welcome")
