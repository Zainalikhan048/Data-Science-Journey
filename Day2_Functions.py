# Day 2 - Functions and Getting Help
# Finished the Kaggle exercise on functions today.
# Writing down what I learned + my practice code.

# ----------------------------------
# 1. Built-in functions
# ----------------------------------

# print() - shows stuff on screen
print("Hello, learning functions today!")

# type() - tells you what type of data something is
name = "Ali"
age = 24
height = 5.8

print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
print(type(height)) # <class 'float'>

# len() - gives you the length of a string or list
word = "python"
print(len(word))    # 6

# ----------------------------------
# 2. Getting help with help()
# ----------------------------------

# help() shows you documentation for any function
# I tried these in the interactive shell:

# help(print)
# help(len)
# help(round)

# The round() function rounds numbers
print(round(3.14159, 2))  # 3.14

# ----------------------------------
# 3. Defining my own functions
# ----------------------------------

# Basic function - greets someone
def greet(name):
    return f"Hello {name}, nice to meet you!"

print(greet("Zara"))

# Function with two arguments
def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(15, 27))  # 42

# ----------------------------------
# 4. Functions from the exercise
# ----------------------------------

# Problem: Convert hours to minutes
def hours_to_minutes(hours):
    minutes = hours * 60
    return minutes

print("3 hours =", hours_to_minutes(3), "minutes")
print("5.5 hours =", hours_to_minutes(5.5), "minutes")

# Problem: Check if a number is even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))

# Problem: Return the larger of two numbers
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

print("Larger of 8 and 12:", max_of_two(8, 12))

# ----------------------------------
# 5. Functions calling other functions
# ----------------------------------

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def add_then_multiply(x, y, z):
    step1 = add(x, y)
    result = multiply(step1, z)
    return result

print("(2 + 3) * 4 =", add_then_multiply(2, 3, 4))  # 20

# ----------------------------------
# 6. What I learned about docstrings
# ----------------------------------

# Docstrings are notes inside functions to explain what they do
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    
    Parameters:
    length (float): Length of the rectangle
    width (float): Width of the rectangle
    
    Returns:
    float: Area of the rectangle
    """
    return length * width

print("Area of 5x3 rectangle:", calculate_area(5, 3))

# You can see the docstring with help(calculate_area)

# ----------------------------------
# End of Day 2
# ----------------------------------
# Feeling more confident with functions.
# Next: Booleans and conditionals.