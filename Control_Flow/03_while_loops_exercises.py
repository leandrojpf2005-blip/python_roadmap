# ------------------
# Basic While Loop
# ------------------

# 1. Print numbers from 0 to 4 using a while loop
count = 0
while count < 5:
    print(count)
    count += 1

# ------------------
# Reverse Counting
# ------------------

# 2. Print numbers from 10 down to 1 using a while loop

count = 10
while count > 0:
    print(count)
    count -= 1

# ------------------
# Accumulator Pattern
# ------------------

# 3. Given:
numbers = [5, 10, 15, 20]
index = 0
total = 0 
# Use a while loop to calculate the sum of the numbers

while index < len(numbers):
    total += numbers[index]
    index += 1

print(total)

# ------------------
# Counting Pattern
# ------------------

# 4. Given:
numbers = [1, 2, 3, 4, 5, 6]
even_count = 0
index = 0

# Count how many numbers are odd using a while loop

while index < len(numbers):
    if numbers[index] %2 == 1:
        even_count += 1
    index += 1

print(f'Odds counted: {even_count}')

# ------------------
# Searching with Early Exit
# ------------------

# 5. Given
numbers = [10, 25, 30, 45, 50]
target = 30
index = 0

# Use a while loop to determine if target exists in the list
# Stop the loop immediately when found
# Print True or False

while index < len(numbers):
    if numbers[index] == target:
        print('true')
        break
    index += 1
else:
    print('False')


# ------------------
# Infinite Loop With Break
# ------------------

# 6. Create a while True loop that:
# - Prints numbers starting from 1
# - Stops when the number reaches 5
# Use break
number = 1
while True:
    print(number)
    number += 1
    if number > 5:
        break

# ------------------
# Continue Usage
# ------------------

# 7. Print numbers from 1 to 10
# Skip printing number 5
# Use continue explicitly

i = 1
while i <= 10:
    i += 1
    if i == 5:
        i += 1
        print(i)
        continue

# ------------------
# Sentinel Value Loop
# ------------------

# 8. Keep asking the user to input a word
# Stop when the user types "stop"
# Print each word entered (except "stop")

while True:
    word = input('Enter the word STOP: ')
    if word == 'stop':
        break
    else:
        print(word)


# ------------------
# Input Validation
# ------------------

# 9. Ask the user to enter a number greater than 0
# Keep asking until a valid number is entered
# Then print "Valid number"
number  = 0

while True:
    number2 = int(input('Enter a number greater than 0: '))
    if number2 > number:
        break
    else:
        print('Try again!')

# ------------------
# Multiplication Table
# ------------------

# 11. Print the multiplication table of 7:
# 7 x 1 = 7
# ...
# 7 x 10 = 70

# Use a while loop
table = 1
while True:
    multi = 7 * table
    print(multi)
    table += 1
    if table == 11:
        break

# ------------------
# While-else Behaviour
# ------------------
index = 0

# 12. Given:
numbers = [2, 4, 6, 8]

# Check if any number is odd
# If found, print "Odd found"
# If loop completes normally, print "All even"
# Use while-else

while index < len(numbers):
    if numbers[index] %2 == 1:
        print('Odd found')
        break
    index += 1
else:
    print('All even')

# ------------------
# Index Tracking
# ------------------

# 13. Given:
text = "Python"
index = 0

# Print each character using a while loop and index

while index < len(text):
    print(text[index])
    index += 1

# ------------------
# Accumulate User Input
# ------------------
# 14. Keep asking the user to enter numbers
# Stop when the user enters 0
# Print the total sum of all entered numbers (excluding 0)
total = 0
while True:
    number = int(input('Enter a number'))
    if number == 0:
        break
    else:
        total += number
print(total)

# ------------------
# Menu Loop
# ------------------

# 15. Create a simple menu loop:
# Print:
# 1 - Hello
# 2 - Bye
# exit - Quit
# - Execute the corresponding action
# - Keep looping until user types "exit"
while True:
    menu = input('Choose what to do next: (1/2/exit)')
    if menu == '1':
        print('Hello')
        continue
    elif menu == '2':
        print('Bye')
        continue
    elif menu == 'exit':
        print('Quit')
        break