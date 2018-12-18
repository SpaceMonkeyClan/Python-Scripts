#Cut Conversion Calculator V.1.0.0
#Author: Dena, Rene

print ('\nWelcome to "Cut Conversion Calculator!". This program will take the initial price of your product, and then calculate both the Owner\'s cut and the Shop\'s cut of the product after sale.')

name = input("\nWhat is your name?")
print ("\nWelcome", name,"!", "Lets get started.")

Product_price = int(input("\nWhat is the intial price of your product?:"))

Owners_cut = 60/100 * Product_price
Shops_cut = 40/100 * Product_price

print ("\nGiven the sale of your product valued at","'",'$',Product_price,"'",',', "the Owners's cut will be", "'",'$',Owners_cut,"'",',', "whereas the Shops's cut will be", "'",'$',Shops_cut,"'.",)

First_month = Product_price * 0.8
Second_month = Product_price * 0.6
Third_month = Product_price * 0.4

OwnersCutFM = 60/100 * First_month
ShopsCutFM = 40/100 * First_month

OwnersCutSM = 60/100 * Second_month
ShopsCutSM = 40/100 * Second_month

OwnersCutTM = 60/100 * Third_month
ShopsCutTM = 40/100 * Third_month

print ("Would you like to see Owners's cut & Shop's cut for the first three months of which the product does not sell given its 20% reduced sale price?")

UserChoice = input('\n yes OR no?:')
if UserChoice != 'yes':
    print ('\nThanks for using "Cut Conversion Calcilator!"')
    input ('Please press ENTER to exit')
    
elif UserChoice == 'yes':
    print ('\nHere are the cuts for the Owner & Shop thereafter reduced price apllication for the 1st, 2nd, and 3rd month')
    print ('\n\nCuts after first month of price reduction:')
    print ("The Owners cut after the first month of price reduction will be $%.2f whereas the Shop\'s cut will be $%.2f." % (OwnersCutFM, ShopsCutFM))
    print ('\n\nCuts after second month of price reduction:')
    print ("The Owners cut after the first month of price reduction will be $%.2f whereas the Shop\'s cut will be $%.2f." % (OwnersCutSM, ShopsCutSM))
    print ('\n\nCuts after third month of price reduction:')
    print ("The Owners cut after the first month of price reduction will be $%.2f whereas the Shop\'s cut will be $%.2f." % (OwnersCutTM, ShopsCutTM))
           
input ("\nPlease press ENTER to exit")
