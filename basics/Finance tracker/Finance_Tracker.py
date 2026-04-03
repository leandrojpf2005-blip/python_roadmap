name_input = input('Enter your Name: ')

#Age
while True:
    age_input = input('Enter your age: ')
    try:
        age = int(age_input)
        break
    except ValueError:
        print('Invalid input, Try again!')

#Income 
while True:
    income_input = input('Enter your Monthly Income: ')
    try:
        income = float(income_input)
        break
    except ValueError:
        print('Invalid input, Try again!')

#Rent Expenses
while True:
    rent_input = input('Enter your Rent: ')
    try:
        rent = float(rent_input)
        break
    except ValueError:
        print('Invalid input, Try Again!')

#Food Expenses
while True:
    food_input = input('Enter your Food expenses: ')
    try:
        food = float(food_input)
        break
    except ValueError:
        print('Invalid input, Try Again!')

#Transport Expensions
while True:
    transport_input = input('Enter your Transport expenses: ')
    try:
        transport = float(transport_input)
        break
    except ValueError:
        print('Invalid input, Try Again!')

#Entertainment Expenses
while True:
    entertainment_input = input('Enter your Entertainment expenses: ')
    try:
        entertainment = float(entertainment_input)
        break
    except ValueError:
        print('Invalid input, Try Again!')
        
#Other expenses
while True:
    other_input = input('Enter your Other expenses: ')
    try:
        other = float(other_input)
        break
    except ValueError:
        print('Invalid input, Try Again!')

#Calc
total_expenses = rent + food + transport + entertainment + other
remaining_balance = income - total_expenses
rent_percentage = (rent / income) * 100
food_percentage = (food / income) * 100
transport_percentage = (transport / income) * 100
entertainment_percentage = (entertainment / income) * 100
other_percentage = (other / income) * 100

#File Write
with open('finance_tracker.txt', 'w') as file:
    file.write(f'Summary for {name_input}, Age {age}\n')
    file.write('============================\n')
    file.write(f'Monthly Income: ${income:.2f}\n')
    file.write(f'Monthly Expenses: ${total_expenses:.2f}\n')
    file.write(f'Remaining Balance: ${remaining_balance:.2f}\n')
    if remaining_balance < 0:
        file.write("Warning: You are over budget!\n")
    file.write(f'\nExpenses Breakdown: \n')
    file.write(f'Rent: ${rent:.2f} ({rent_percentage:.2f}%)\n')
    file.write(f'Food: ${food:.2f} ({food_percentage:.2f}%)\n')
    file.write(f'Transportation: ${transport:.2f} ({transport_percentage:.2f}%)\n')
    file.write(f'Entertainment: ${entertainment:.2f} ({entertainment_percentage:.2f}%)\n')
    file.write(f'Others: ${other:.2f} ({other_percentage:.2f}%)\n')

#Read File
with open('finance_tracker.txt', 'r') as file:
    summary = file.read()
    print(summary)
