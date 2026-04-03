# ------------------
# Basic Output
# ------------------

#1. Print the following exactly:
Name = 'Joao'
Age = 26
Country = 'Portugal'
# a) Using multiple print() statements
# b) Using a single multi-line string

print(Name)
print(Age)
print(Country)

print(Name, Age, Country)


#----------------
# Print Parameters
# ------------------

# 2. Print the numbers 1 to 5 on the same line separated by " | " --
numbers = list(range(1, 6))
print(' | '.join(map(str, numbers)))

# ------------------
# Basic Input & Type Conversion
# ------------------

# 3. Ask the user for:
# Their name
# Their birth year

name_input = input('Enter your name: ')
birth_input = input('Enter your birth year: ')

# a) Convert the birth year to an integer
# b) Calculate their approximate age (assume current year is 2026)
# c) Print: "Hello <name>, you are approximately <age> years old."

birth = int(birth_input)
age_calc = 2026 - birth
print(f'Hello {name_input}, you are approximately {age_calc} years old')

# ------------------
# Input Validation
# ------------------

# 4. Ask the user to enter a number.
# a) If the input is numeric, convert it to int and print its square
# b) If not numeric, print "Invalid number"

number_input = input('Enter a number: ')

if number_input.isdigit():
    number = int(number_input)
else:
    print('Invalid input')

# ------------------
# Advanced Input Validation
# ------------------

# 5. Ask the user to enter a floating-point number.
# Use try/except to:
# a) Attempt conversion using float()
# b) If conversion fails, print "Invalid input"
# c) If successful, print half of the number

number_input2 = input('enter a float number: ')

try:
    number_input2 = float(number_input2)
    print(number_input2 / 2)
except ValueError:
    print('Invalid input')


# ------------------
# String Formatting Practice
# ------------------

# 6. Ask the user for:
# - Product name
# - Product price (float)
# a) Format the price to 2 decimal places.
# b) Print: "<product> costs $<price>"

product_input = input('Enter product name: ')
price_input = input('Enter the product price: ')

try:
    price_input = float(price_input)
except ValueError:
    print('Invalid Price')

print(f'{product_input} costs ${price_input:.2f}')


# ------------------
# Writing To a File
# ------------------

# 7. Create a file called "user_info.txt"
# Ask the user for: name and age
# Write this to the file:
# Name <name>
# Age: <age>
# Use a with statement

with open('user_info.txt', "w") as file:
    name_input2 = input('Enter your Name: ')
    age_input2 = input('Enter your Age: ')
    file.write(f'Name: {name_input2}\n')
    file.write(f'Age: {age_input2}\n')


# ------------------
# Appending to a File
# ------------------

# 8. Append a new line to "user_info.txt":
# "Status: Active"

with open('user_info.txt', 'a') as file:
    file.write(f'Status: Active\n')

# ------------------
# Reading From a File
# ------------------

# 9. Read the contents of "user_info.txt"
with open('user_info.txt', 'r') as file:
    file_content = file.readlines()
    print(file_content)


# ------------------
# File Existence Handling
# ------------------

# 10. Attempt to open a file named "missing_file.txt"
# Use try/except
# Catch "FileNotFoundError"
# Print "File does not exist"

try:
    with open('missing_file.txt', 'r') as file:
        missing_cont = file.read()
except FileNotFoundError:
    print('File does not exist')


# ------------------
# Working With Numbers From a File
# ------------------

# 11. Create a file named "numbers.txt"
# Write the numbers 1 through 5 into it (one per line)
# Then:
# a) Read the file
# b) Convert each line to an integer
# c) Calculate the total sum
# D) Print the sum

with open('numbers.txt', 'w') as file:
    for number3 in range(1, 6):
        file.write(f'{number3}\n') 

with open('numbers.txt', 'r') as file:
    numbers4 = [int(line.strip()) for line in file.readlines()]
    total = sum(numbers4)
    print(total)


# ------------------
# Bonus: Simple Logger
# ------------------

# 12. Create a small logging system.
# Ask the user to enter a message.

message = input('Enter your log message: ')

with open('log.txt', 'a') as file:
    file.write(message + '\n')