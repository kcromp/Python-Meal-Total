_author_ = 'Kelsey Crompton'

# Program to choose lunch combo items

def main():
    sandwich = choose_sandwich()
    side = choose_side()
    drink = choose_drink()
    total = sum(sandwich, side, drink)
    print('Please pay this amount: $',total)



def choose_sandwich():
    print('Pick a sandwich: ')
    print('1. Grilled cheese sandwich $3.00')
    print('2. Chicken sandwich $3.50')
    print('3. Turkey sandwich $4.00')
    sandwich_choice = int(input('Please enter your choice: [1/2/3] '))
    if sandwich_choice == 1:
        selection = 3
    elif sandwich_choice == 2:
        selection = 3.5
    else:
        selection = 4
    return selection

def choose_side():
    print('Pick a side item: ')
    print('1. French fries $1.50')
    print('2. Mashed Potato $1.50')
    print('3. Green bean $1.25')
    print('4. Garden salad $2.00')
    side_choice = int(input('Please enter your choice: [1/2/3/4] '))
    if side_choice == 1:
        selection = 1.5
    elif side_choice == 2:
        selection = 1.5
    elif side_choice == 3:
        selection = 1.25
    else:
        selection = 2
    return selection

def choose_drink():
    print('Pick a drink: ')
    print('1. Coffee $1.25')
    print('2. Iced tea $1.00')
    print('3. Soda $1.00')
    drink_choice = int(input('Please enter your choice: [1/2/3] '))
    if drink_choice == 1:
        selection = 1.25
    elif drink_choice == 2:
        selection = 1
    else:
        selection = 1
    return selection

def sum(num1, num2, num3):
    result = num1 + num2 + num3
    return result

main()
