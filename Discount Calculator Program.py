## Discount Calculator - V 1.0.0
## Author: Dena, Rene
## Last Modified: 12/12/17

#________________________________________________________Misc.__________________________________________________________



#________________________________________________________Functions______________________________________________________

def Results_Menu():
    print('\n=============================================================================')
    print('\n\n\t\t\tRESULTS CONSOLE!')
    print('\nGiven:')
    print('\nApplied discount is: ${:.2f}'.format(constant))
    print('Original price is: ${:.2f}'.format(originalPrice))
    print('Current price is:${:.2f}'.format(currentPrice))
    print('\nThe new:')

    newPrice = currentPrice - constant

    thirtyDis = .30 * originalPrice
    thirtyPrice = originalPrice - thirtyDis

    fourtyDis = .40 * originalPrice
    fourtyPrice = originalPrice - fourtyDis

    fifthyDis = .50 * originalPrice
    fifthyPrice = originalPrice - fifthyDis

    seventyDis = .70 * originalPrice
    seventyPrice = originalPrice - seventyDis

    if fourtyPrice < newPrice < thirtyPrice :
        print('\nDiscount percentage is: 30%')
    elif fifthyPrice < newPrice < fourtyPrice:
        print('\nDiscount percentage is: 40%')
    elif seventyPrice < newPrice < fifthyPrice:
        print('\nDiscount percentage is: 50%')
    elif 0 < newPrice < seventyPrice:
        print('\nDiscount percentage is: 70%')

    print('Sale price is: ${:.2f}'.format(newPrice))

    Hash_Menu()


def Hash_Menu():
	print('\n____________________________________________________________________________')
	global originalPrice, currentPrice
	print('\n\n\t\t\tWelcome to the HASH CONSOLE!')
	while True:
		userChoiceIII = input('\nPlease ENTER the ORIGINAL price of the item: $')
		try:
			originalPrice = float(userChoiceIII)
            #print('\nAwesome! You have selected ${:.2f} as the original price of the item. :D'.format(originalPrice))
			break
		except ValueError:
			print('\nPlease be sure to only ENTER a integer or a decimal. No alphabetic characters! >:|')
	while True:
	    userChoiceIV = input('\nNext, please ENTER the CURRENT price of the item: $')
	    try:
	        currentPrice = float(userChoiceIV)
            #print('\nAwesome! You have selected ${:.2f} as the current price of the item. :D'.format(currentPrice))
	        break
	    except ValueError:
	           print('\nPlease be sure to only ENTER a integer or a decimal. No alphabetic characters! >:|')
	Results_Menu()



def Discount_Menu():
    global constant
    print('\n\n\t\t\tWelcome to the DISCOUNT CONSOLE!')
    while True:
        userChoiceII = input('\nPlease ENTER the constant applied discount: $')
        try:
            constant = float(userChoiceII)
            print('\nAwesome! You have selected ${:.2f} as your auto-applied discount. :D'.format(constant))
            print('\nWe can now head to the Hash Console.!')
            print('\nLOADING...............')
            Hash_Menu()
            break
        except ValueError:
               print('\nPlease be sure to only ENTER a integer or a decimal. No alphabetic characters! >:|')


def mainConsole():
    print('\n\n\t\t\tWelcome to the MAIN CONSOLE!')
    print('\nIf you would like to begin the discount process, please ENTER "1": ')
    print('If you would like to view the final report, please ENTER "2": ')
    print('If you would like to kill the script, please ENTER "3": ')
    while True:
        userChoiceI = int(input('\nPlease ENTER "1", "2", or "3": '))
        if userChoiceI == 1:
            print('\nYou\'ve decided to begin the discount process. Let\'s head there now.')
            print('\nLOADING...............')
            Discount_Menu()
            break
        elif userChoiceI == 2:
            print('\nYou\'ve decided to view the final report. Let\'s head there now.')
            print('\nLOADING...............')
            Final_Report()
            break
        elif userChoiceI == 3:
            print('\nUnfortunate......you\'ve decided to kill the script. :[')
            print('\nHope we\'ve helped and hope to see you back soon.')
            print('\nWe will now kick you from script.')
            print('\nLOADING...............')
            print('\nYou have now been kicked from script.')
            print('\nGOOD DAY! :)')
            print('\n')
            break
        else:
            print('\nPlease only ENTER the integers prompted too........')

#________________________________________________________Strickly Script______________________________________________

print('\n\t\t\tWelcome to the "Discount Calculator" program!')

print('\nThis script will essentially allow you to ENTER both the original price and sale price of an item, apply an  additional discount on that item, and finally output the applied discount via percentage.')

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
