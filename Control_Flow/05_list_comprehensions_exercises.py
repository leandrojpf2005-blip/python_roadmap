# ------------------
# Basic Creation
# ------------------

# 1. Create a list of numbers from 1 to 10 using list comprehension

numbers_comp = [i for i in range(11)]
print(numbers_comp)
# 2. Create a list of squares from 1 to 10

numbers_squares = [ i ** 2 for i in range(11)]
print(numbers_squares)

# 3. Create a list of numbers from 1 to 20 that are divisible by 3
numbers_div = [i for i in range(1, 21) if i %3 == 0]
print(numbers_div)

# ------------------
# Working With Strings
# ------------------

# 4. Given:

words = ["apple", "banana", "cherry", "kiwi"]

# Create a list with the length of each word
list_len = [len(word) for word in words]
print(list_len)

# 5. From the same list, create a new list containing only words with more than 5 letters
list_len2 = [word for word in words if len(word) > 5]
print(list_len2)

# 6. Create a list with all words converted to uppercase
list_upper = [word.upper() for word in words]
print(list_upper)

# ------------------
# If-Else Inside Comprehension
# ------------------

# 7. Create a list from 1 to 10 where:
# - Even numbers become "Even"
# - Odd numbers become "Odd"
list7 = ['Even' if i %2 == 0 else 'Odd' for i in range(1, 11)]
print(list7)

# 8. Given
numbers = [10, 15, 20, 25, 30]

# Create a list where:
# - If number > 20 -> "High"
# - Otherwise -> "Low"

list8 = ['high' if i > 20 else 'Low' for i in numbers]
print(list8)

# ------------------
# Nested Comprehension
# ------------------

# 9. Given:
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Flatten this matrix into a single list.

list9 = [i for r in matrix for i in r]
print(list9)

# 10. Create a list of all pairs (x, y)
# where x is from 1 to 3
# and y is from 1 to 2

list10 = [(x, y) for x in range(1, 4) for y in range(1, 3)]
print(list10)

# ------------------
# Multiple Conditions
# ------------------

# 11. Create a list of numbers from 1 to 50
# that are divisible by both 2 and 5

list11 = [i for i in range(1,51) if i %5 == 0 and i %2 == 0]
print(list11)

# 12. Create a list of numbers from 1 to 30
# that are divisible by 3 but NOT divisible by 2

list12 = [i for i in range(1,31) if i %3 == 0 and i %2 != 0]
print(list12)

# ------------------
# Dictionary Comprehension
# ------------------

# 13. Create a dictionary where:
# - Keys are numbers from 1 to 5
# - Values are the square of each number

list13 = {x: x**2 for x in range(1,6)}
print(list13)

# 14. Given:
names = ["Ana", "Joao", "Carlos"]

# Create a dictionary where:
# - Key is the name
# - Value is the length of the name

list14 = {name: len(name) for name in names}
print(list14)

# ------------------
# Sets Comprehension
# ------------------

# 15. Given:
numbers = [1, 2, 2, 3, 4, 4, 5]

# Create a set of unique squared values

list15 = {i**2 for i in numbers}
print(list15)

# ------------------
# Advanced Thinking
# ------------------

# 16. Given:
values = [1, -2, 3, -4, 5]

# Create a list with absolute values of each number

list16 = [abs(i) for i in values]
print(list16)

# 17. Create a list of all lowercase letters
# from the string "Hello World"
# (ignore spaces)
text = 'Hello World'
list17 = [char.lower() for char in text if char != ' ']
print(list17)

# 18. Create a list of tuples (number, square)
# for numbers from 1 to 10

list18 = [(i, i**2) for i in range(1, 11)]
print(list18)

# 19. Given:
numbers = [1, 2, 3, 4, 5, 6]

# Create a list containing only numbers greater than 3 but multiplied by 10

list19 = [i * 10 for i in numbers if i > 3]
print(list19)

# 20. Bonus:
# Create a 3x3 multiplication table as a nested list using list comprehension
# Expected structure:
# [
#   [1, 2, 3],
#   [2, 4, 6],
#   [3, 6, 9]
# ]
list20 = [
    [i * j for j in range(1, 4)]
    for i in range(1, 4)
]
print(list20)