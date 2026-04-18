# Day 5 - Loops and List Comprehensions
# Finished the Kaggle exercise today.
# Loops help me repeat things. List comprehensions are a shorter way to make lists.

# ----------------------------------
# 1. For loops - iterating over a list
# ----------------------------------

fruits = ["apple", "banana", "cherry"]

print("My fruits:")
for fruit in fruits:
    print(fruit)

# ----------------------------------
# 2. For loops with range()
# ----------------------------------

# range(stop) - 0 to 4
print("Numbers 0 to 4:")
for i in range(5):
    print(i)

# range(start, stop) - 2 to 5
print("Numbers 2 to 5:")
for i in range(2, 6):
    print(i)

# range(start, stop, step) - even numbers
print("Even numbers 0 to 10:")
for i in range(0, 11, 2):
    print(i)

# Count backwards
print("Countdown:")
for i in range(5, 0, -1):
    print(i)

# ----------------------------------
# 3. While loops
# ----------------------------------

# Count to 5 with while
count = 1
while count <= 5:
    print("Count:", count)
    count = count + 1

# Keep asking until correct answer
# (commented so it doesn't run automatically)
# guess = 0
# while guess != 7:
#     guess = int(input("Guess a number: "))
# print("You got it!")

# ----------------------------------
# 4. Breaking out of loops
# ----------------------------------

print("Find the first number divisible by 7:")
for num in range(1, 50):
    if num % 7 == 0:
        print("Found:", num)
        break  # stops the loop

# ----------------------------------
# 5. Continue - skip an iteration
# ----------------------------------

print("Numbers 1-10, skipping multiples of 3:")
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)

# ----------------------------------
# 6. Looping with enumerate() (get index and value)
# ----------------------------------

colors = ["red", "blue", "green", "yellow"]

for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# ----------------------------------
# 7. Looping through strings
# ----------------------------------

word = "python"
print("Letters in 'python':")
for letter in word:
    print(letter)

# ----------------------------------
# 8. Nested loops
# ----------------------------------

print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")

# ----------------------------------
# 9. List comprehensions - the simple way
# ----------------------------------

# Traditional way to make a list of squares
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print("Squares (traditional):", squares)

# List comprehension way
squares_comp = [x ** 2 for x in range(1, 6)]
print("Squares (comprehension):", squares_comp)

# ----------------------------------
# 10. List comprehensions with conditions
# ----------------------------------

# Get only even numbers from 0-20
evens = [x for x in range(21) if x % 2 == 0]
print("Even numbers:", evens)

# Get numbers greater than 5
greater_than_5 = [x for x in range(1, 11) if x > 5]
print("Greater than 5:", greater_than_5)

# ----------------------------------
# 11. List comprehensions with if-else
# ----------------------------------

# Mark numbers as "even" or "odd"
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
print("Even/odd labels:", labels)

# ----------------------------------
# 12. Practical examples from exercise
# ----------------------------------

# Double every number in a list
def double_list(numbers):
    return [num * 2 for num in numbers]

print("Double of [1,2,3,4]:", double_list([1, 2, 3, 4]))

# Get only words longer than 3 letters
def long_words(words):
    return [word for word in words if len(word) > 3]

print("Long words:", long_words(["hi", "hello", "hey", "greetings", "bye"]))

# Capitalize all words in a list
def capitalize_all(words):
    return [word.upper() for word in words]

print("Capitalized:", capitalize_all(["apple", "banana", "cherry"]))

# Sum of all numbers in a list (using loop)
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print("Sum of [10,20,30]:", sum_numbers([10, 20, 30]))

# Find all numbers divisible by 3 in a range
def divisible_by_three(limit):
    return [num for num in range(1, limit + 1) if num % 3 == 0]

print("Divisible by 3 up to 20:", divisible_by_three(20))

# ----------------------------------
# 13. More complex list comprehensions
# ----------------------------------

# Flatten a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# First letter of each word
words = ["apple", "banana", "cherry", "date"]
first_letters = [word[0] for word in words]
print("First letters:", first_letters)

# ----------------------------------
# 14. Loops with multiple lists (zip)
# ----------------------------------

names = ["Ali", "Sara", "John"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# ----------------------------------
# 15. My own practice
# ----------------------------------

# FizzBuzz - classic beginner problem
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print("FizzBuzz up to 15:")
fizzbuzz(15)

# ----------------------------------
# End of Day 5
# ----------------------------------
# Loops make repetition easy. List comprehensions are cleaner.
