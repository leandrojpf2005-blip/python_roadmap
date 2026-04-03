# ------------------
# Numeric
# ------------------

# 1. Create two integers where:
# / returns a float
# // returns a different result

c = 13
d= 5

float_res = c / d
different_res = c // d

print(float_res)
print(different_res)

# 2. Create: a = "10"; b = 5
# Make the addition work without changing the value of a
# Then, make it work without changing the value of b

a = "10"
b = 5

print(int(a) + b)
print(a + str(b))

# ------------------
# String
# ------------------

# 1. Create a string: s = "python".
# Attempt to change the first character to uppercase using indexing.
# Observe the error
# Then, correctly produce "Python"

s = 'python'
z = s[0].upper() + s[1:]
print(z)

# 2. Without using loops, reverse: text = "DataTypes"

text = "DataTypes"
print(text[-1::-1])


# ------------------
# Lists
# ------------------

# 1. Append 99 to copy1
# Append 100 to copy 2
# Print all three lists and explain what happened

original = [1, 2, 3, 4, 5, 6]
copy1 = original.copy()
copy2 = original.copy()
copy1.append(99)
copy2.append(100)
print(original)
print(copy1)
print(copy2)


# ------------------
# Tuples
# ------------------

#1. Create t = (1, [2, 3], 4)
# Modify the list inside the tuple
# Explain why this works even though tuples are immutable

t = (1, [2, 3], 4)
t[1].append(8)
print(t)
#this works because theres a list inside of a tuple, so even if it tuples are immutable, the list inside can still be changed


# ------------------
# Sets
# ------------------

# 1. Given nums = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicates using a set
# Convert back to a list
# What property of sets make this work?

nums = [1, 2, 2, 3, 4, 4, 5]
my_set = set(nums)
my_list = list(my_set)
print(my_list)

# 2. Create two sets of numbers. Print: Union, Intersection, Elements only in first set. Explain each result

set1 = {1, 2, 3 ,4, 5}
set2 = {6, 7, 8, 9, 10}
print('Union: ', set1 | set2)
print('Intersection: ', set1 & set2)
print('Elements: ', set1 - set2)

# ------------------
# Dictionary
# ------------------

# 1. Create a dictionary: user = {"name": "Joao", "age": 26}
# Try to access a key "balance" safely without raising an error

user = {'name': 'Joao', "age": 26}
print(user.get('balance', 0))
# 2. Iterate through the dictionary and
# Print only keys
# Print only values
# Print both formatted with f-strings

print(user.keys())
print(user.values())

for key, value in user.items():
    print(f"{key} -> {value}")


# ------------------
# Booleans & Truthiness
# ------------------

# 1. Test the boolean value of:
# 0, 1, "", "text", [], [0], None
# Explain the pattern

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("text"))
print(bool([]))
print(bool([0]))
print(bool(None))
print('False values are values related to 0 or empty values')
print('True values are values that dont mean 0 or arent empty')
# ------------------
# Advanced Concepts
# ------------------

# 1. Check a == b; a is b
# Explain the difference

a = 100
b = 100

print(a == b)   
print(a is b)