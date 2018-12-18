## Tax Calculator - V 1.0.0
## Author: Dena, Rene
## Last Modified:

#________________________________________________________Misc.__________________________________________________________

## Requirements:
# input costs
# country/state
# output tax and total cost

stateList = {'Alabama': 4.00, 'Alaska': None, 'Arizona': 5.60, 'Arkansas': 6.50, 'California': 7.50, 'Colorado': 2.90, 'Connecticut': 6.35, 'Delaware': None, 'Florida': 6.00, 'Georgia': 4.00, 'Hawaii': 4.00, 'Idaho': 6.00, 'Illinois': 6.25, 'Indiana': 7.00, 'Iowa': 6.00, 'Kansas': 6.15, 'Kentucky': 6.00, 'Louisiana': 4.00, 'Maine': 5.50, 'Maryland': 6.00, 'Massachusetts': 6.25, 'Michigan': 6.00, 'Minnesota': 6.875, 'Mississippi': 7.00, 'Missouri': 4.225, 'Montana': None, 'Nebraska': 5.50, 'Nevada': 6.85, 'New Hampshire': None, 'New Jersey': 7.00, 'New Mexico': 5.125, 'New York': 4.00, 'North Carolina': 4.75, 'North Dakota': 5.00, 'Ohio': 5.75, 'Oklahoma': 4.50, 'Oregon': None, 'Pennsylvania': 6.00, 'Rhode Island': 7.00, 'South Carolina': 6.00, 'South Dakota': 4.00, 'Tennessee': 7.00, 'Texas': 6.25, 'Utah': 5.95, 'Vermont': 6.00, 'Virginia': 5.30, 'Washington': 6.50, 'West Virginia': 6.00, 'Wisconsin': 5.00, 'Wyoming': 4.00, 'DC': 5.75};


#________________________________________________________Functions______________________________________________________

def mainConsole():
    print('\n\n\t\t\tWelcome to the MAIN CONSOLE!')

    while True:
        salePrice = float(input('\nPlease ENTER the combined sale price of the item(s): '))
        if salePrice is float:
            print('\nPlease be sure to only ENTER an integer! >:|')
        else:
            print('\nAwesome! You\'ve stated that the combined sale price is ${}.'.format(salePrice))
            break

    while True:
        state = input('\nNext, please ENTER the state: ')
        if state.title() not in stateList:
            print('\nPlease ENTER a proper state! >:|')
        else:
            print('\nNice! Youv\'ll selected {} as the state.'.format(state.title()))
            break

    for x in stateList:
        if x == state.title():
            stateTax = stateList[x]
            postTax = stateTax/10
            totalTax = salePrice * postTax
            totalCost = salePrice + totalTax
            print('\nGiven the sale state tax of {} is {}%, the Total Cost will be ${}¢.'.format(state.title(), stateTax, totalCost))

    print('\nHope we\'ve helped! :)')

    while True:
        usersOption = input('\n\nWould you like to re-run the script?("yes" OR "no"): ')
        if usersOption == 'yes' or usersOption == 'YES':
            print('\mAwesom!, You\'ve decided to re-run the script! :)')
            print('\nNow heading to the MAIN CONSOLE.')
            print('\nLOADING.................&nd DONE!')
            mainConsole()
            break
        elif usersOption == 'no' or usersOption == 'NO':
            print('\nBummer! :(. You\'ve decided to end the script.')
            print('\nYou\'ll now be kicked from the script shortly...........')
            print('\nHope to see you back soon :)')
            print('\n\n')
            print('\nYou have now been kicked from the script!')
            print('\nHave yourself a good day.....Cheers! :)')
            print('\n')
            break
        else:
            print('\nPlease only ENTER "yes" OR "no".')


#________________________________________________________Strictly Script________________________________________________

print('\n\t\t\tWelcome to the "Tax Calculator" script!')

print('\nThis script will essentially let you input the sale price of an item, the state, and thus then return the sales tax percentage of that state with the new total cost of the item.')

while True:
    usersName = input('\nIn starting, please ENTER you name: ')
    if usersName.isalpha() and len(usersName) > 0:
        print('\nAwesome! We may now continue {}.'.format(usersName.title()))
        break
    else:
        print('\nPlease only ENTER characters a-z! >:|')

print('\nNow heading to the Main Console........')
print('\nLOADING...............&nd DONE!!!')

mainConsole()
