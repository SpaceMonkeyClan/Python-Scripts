#Car Dealership Conversion Calculator V.1.0.0
#Author: Dena, Rene

print ('\nWelcome to "Car Dealership Conversion Calculator!"')
print ("\nThis program will essentily allow tou to see the profit of a sale by insertsing both the sale and purcahse price of a vehicle.")

name = input("\nIn starting, what is your name?")
print ("\nWelcome", name,"!", "Lets begin.")

Sale_price = int(input("\nWhat is the sale price of the vehical?:"))
Purchase_price = int(input("\nWhat is was the purchase price of the vehical?:"))

Profit = Purchase_price - Sale_price

if Profit < 0:
    print ("\nYour total loss was $%.2f" % (Profit))
elif Profit >= 0:
    print ("\nYour total profit was $%.2f" % (Profit))



           
input ("\nPlease press ENTER to exit")
