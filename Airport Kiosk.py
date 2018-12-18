# The Airport Kiosk - V 1.0.0
# Author: Dena, Rene
# Last Modified: 5/1/17


# _Misc.
# _Functions
# _Strictly Script


print('\n\t\t\tWelcome to "THE AIRPORT KIOSK" script!')


while True:
    name = input('\nBefore we begin, what is your name?:')
    if name.isalpha():
        print('\nAwesome! We can now begin {}.'.format(name.title()))
        break
    else:
        print('\nCANNOT continue if space was left empty.')
        print('Also, please be sure to ENTER your name using \ a-z characters only.')


print('\n\t\t\tWelcome to the MAIN CONSOLE!')
print('\nHere, you will be given the option to to enter the price of your plane ticket, and how many bags you are checking in.')
print('\nLet\'s begin.')
print('\n{}, what was the price of your ticket?'.format(name.title()))


while True:
    try:
        ticket_price = int(input("Enter a number: "))
        print('\nAwesome! You\'ve stated your ticket price was ${}.'.format(ticket_price))
        break
    except ValueError:
        print("\nNot an integer value...")


print('\nNow we\'ll be calculating your total number of bags.')
print('\nHow many bags will you be checking in?')



while True:
    try:
        bags = int(input("Enter a number: "))
        print('\nAwesome! You\'ve stated you\'ll be checking in {} bags.'.format(bags))
        break
    except ValueError:
        print("\nNot an integer value...")



bags_cost = bags * 25 - 25


total_cost = ticket_price + bags_cost


print('\nGiven the information provided above, you total cost will accumulate to ${:.2f}'.format(total_cost))
print('Thank you for using "THE AIRPORT KIOSK" script! Hope to see you again soon :)')
