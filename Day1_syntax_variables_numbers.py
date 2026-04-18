# Day 1 - Syntax, Variables, and Numbers
# I just finished the Kaggle exercise on Python basics.
# This is my practice file with notes and examples.
# Nothing fancy — just getting comfortable with variables and math.

# --- Variables ---
# A variable is just a name for a value.
my_name = "Alex"
my_age = 25
height = 5.9

print("Name:", my_name)
print("Age:", my_age)
print("Height:", height)

# --- Numbers ---
# Python handles integers and decimals easily.
apples = 10
oranges = 7
total_fruit = apples + oranges
print("Total fruit:", total_fruit)

# Multiplication and division
price_per_apple = 0.5
cost = apples * price_per_apple
print("Cost for apples: $", cost)

# --- Syntax rules I learned ---
# 1. Variable names can't start with a number
# 2. Use underscores for long names: my_long_variable
# 3. Python reads code line by line, top to bottom

# --- Quick practice from the exercise ---
# Problem: Calculate how many seconds are in a week
days_in_week = 7
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

seconds_in_week = days_in_week * hours_in_day * minutes_in_hour * seconds_in_minute
print("Seconds in a week:", seconds_in_week)

# Problem: What's 1024 divided by 32?
result = 1024 / 32
print("1024 / 32 =", result)

# --- End of Day 1 ---
