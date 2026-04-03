# ------------------
# Basic Matching
# ------------------

# 1. Given:
day = "Sunday"

# Use match-case to print:
# - "Weekday" for Monday-Friday
# - "Weekend" for Saturday or Sunday
# - "Invalid day" otherwise

match day:
    case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
        print('Weekday')

    case 'Sunday' | 'Saturday':
        print('Weekend')

    case _:
        print('Invalid day')

# ------------------
# Number Matching
# ------------------

# 2. Given:
number = 3

# Use match-case to print:
# - "One" if 1
# - "Two" if 2
# - "Three" if 3
# - "Other" otherwise

match number:
    case 1:
        print('One')
    
    case 2:
        print('Two')

    case 3:
        print('Three')

    case _:
        print('Other')

# ------------------
# Multiple Values
# ------------------

# 3. Given:
status_code = 401

# Use match-case to print:
# - "Success" for 200
# - "Client Error" for 400, 401, 403
# - "Server Error" for 500
# - "Unknown Status" otherwise

match status_code:
    case 200:
        print('Success')
    
    case 400 | 401 | 403:
        print('Client Error')

    case 500:
        print('Server Error')

    case _:
        print('Unknown Status')

# ------------------
# Tuple Destructuring
# ------------------

# 4. Given:
command = ("move", 10, 20)

# If command is:
# ("move", x, y) -> print "Moving to x, y"
# ("stop",) -> print "Stopping"
# Otherwise -> print "Unknown command"

match command:
    case ('move', x, y):
        print('Moving to x, y')
    
    case 'stop':
        print('Stopping')
    
    case _:
        print('Otherwise')

# ------------------
# Guard Condition
# ------------------

number = 15

# Use match-case with a guard:
# - Print "Positive large number" if number > 10
# - Print "Positive small number" if number > 0
# - Print "Zero or negative" otherwise

match number:
    case number if number > 10:
        print('Positive large number')

    case number if number > 0:
        print('Positive small number')

    case _:
        print('Zero or negative')


# ------------------
# List Pattern Matching
# ------------------

# 6. Given:
data = [1, 2, 3, 4]

# Use match-case to:
# - Print "Starts with 1" if list starts with 1 (capture the rest)
# - Print "Empty list" if empty
# - Print "Other list" otherwise

#aaaaaaaaaaaaaaaaaaaaaaaaaa

# ------------------
# Exact List Match
# ------------------

data = [1, 2, 3]

# Match exactly [1, 2, 3] and print "Exact match"
# Otherwise print "Not exact"


# ------------------
# Dictionary Matching
# ------------------

# 8. Given:
person = {"name": "Ana", "age": 30}

# If dictionary contains keys "name" and "age"
# print "{name} is {age} years old"
# Otherwise print "Invalid structure"


# ------------------
# Nested Pattern
# ------------------

event = ("click", {"x": 100, "y": 200})

# If event matches:
# ("click", {"x": x, "y": y})
# print "Clicked at x, y"
# Otherwise print "Unknown event"


# ------------------
# Matching with Type Pattern
# ------------------

# 10. Given:
value = 42

# Use match-case to:
# - Print "Integer" if value is an int
# - Print "String" if value is a str
# - Print "Other type" otherwise


# ------------------
# Combined Pattern
# ------------------

# 11. Given:
point = (0, 5)

# Use match-case to:
# - Print "Origin" if (0, 0)
# - Print "On Y axis" if (0, y)
# - Print "On X axis" if (x, 0)
# - Print "Somewhere else" otherwise


# ------------------
# Wildcard and Unreachable Case Awareness
# ------------------

# 12. Given:
number = 2

# Write a match-case that:
# - Prints "Even" if number is even
# - Prints "Odd" if number is odd
# Use guards