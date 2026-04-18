# Day 3 - Booleans and Conditionals
# Finished the Kaggle exercise today.
# Booleans are just True/False. Conditionals let you make decisions in code.

# ----------------------------------
# 1. Boolean values
# ----------------------------------

is_raining = True
is_sunny = False

print("Is it raining?", is_raining)
print("Is it sunny?", is_sunny)

# ----------------------------------
# 2. Comparison operators
# ----------------------------------

x = 10
y = 20

print(x == y)   # False (equal to)
print(x != y)   # True  (not equal to)
print(x < y)    # True  (less than)
print(x > y)    # False (greater than)
print(x <= 10)  # True  (less than or equal)
print(y >= 20)  # True  (greater than or equal)

# ----------------------------------
# 3. Combining conditions with and / or
# ----------------------------------

age = 25
has_license = True

# Both must be True
can_drive = age >= 18 and has_license
print("Can drive?", can_drive)  # True

# At least one must be True
has_money = False
has_card = True
can_pay = has_money or has_card
print("Can pay?", can_pay)  # True

# ----------------------------------
# 4. If statements
# ----------------------------------

temperature = 30

if temperature > 25:
    print("It's hot outside!")

# ----------------------------------
# 5. If-else statements
# ----------------------------------

score = 85

if score >= 50:
    print("You passed!")
else:
    print("You failed.")

# ----------------------------------
# 6. If-elif-else chains
# ----------------------------------

grade = 92

if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")
elif grade >= 60:
    print("D grade")
else:
    print("F grade")

# ----------------------------------
# 7. Practical examples from the exercise
# ----------------------------------

# Check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(5))   # Positive
print(check_number(-3))  # Negative
print(check_number(0))   # Zero

# Check if someone can vote
def can_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Too young to vote"

print(can_vote(20))  # Eligible to vote
print(can_vote(16))  # Too young to vote

# Find the largest of three numbers
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Largest of 5, 12, 8:", largest_of_three(5, 12, 8))  # 12

# ----------------------------------
# 8. Using bool() function
# ----------------------------------

# bool() converts values to True/False
print(bool(1))      # True
print(bool(0))      # False
print(bool("hi"))   # True
print(bool(""))     # False
print(bool([]))     # False (empty list)
print(bool([1,2]))  # True

# ----------------------------------
# 9. Nested conditionals
# ----------------------------------

def get_discount(customer_type, amount):
    if customer_type == "member":
        if amount > 100:
            return 0.20  # 20% discount
        else:
            return 0.10  # 10% discount
    else:
        if amount > 100:
            return 0.05  # 5% discount
        else:
            return 0     # no discount

print("Member with $150:", get_discount("member", 150))  # 0.2
print("Regular with $80:", get_discount("regular", 80))  # 0

# ----------------------------------
# 10. Simple password checker I wrote
# ----------------------------------

def check_password(password):
    if len(password) < 6:
        return "Too short"
    elif len(password) > 20:
        return "Too long"
    else:
        return "Password looks good"

print(check_password("hi"))        # Too short
print(check_password("secure123")) # Password looks good

# ----------------------------------
# End of Day 3
# ----------------------------------
# Booleans and conditionals make so much sense now.
