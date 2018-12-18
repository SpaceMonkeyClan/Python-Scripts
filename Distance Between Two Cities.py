# Distance Between Two Cities - V 1.0.0
# Author: Dena, Rene
# last Modified: 8/11/17

## Misc._______________________________________________________________________________________________________________
import math

## Functions___________________________________________________________________________________________________________

def mainConsole():
    print('\n\t\t\tWelcome to the "MAIN CONSOLE!"')
    print('\nIn starting, you\'ll first have to ENTER the LATITUDE of each city.')
    print('\nFOR EXAMPLE: Consider Albuqurque, New Mexico.')
    print('If its LATITUDE is "25.08°N", you should ENTER as "25.08".')

    ## City 1
    while True:
        cityI = input('\nIn begginging, please ENTER the name of the first city: ')
        if cityI.isalpha() and len(cityI) > 0:
            print('\nAwesome! You\'ve stated that the first city is {}.'.format(cityI.title()))
            break
        else:
            print('\nPlease only ENTER chars a-z! >:|')


    while True:
        latitudeI = float(input('\nSuch being said, please ENTER the LATITUDE of {}: '.format(cityI.title())))
        if latitudeI is not float and latitudeI > 0:
            print('\nAwesome! You\'ve stated that the LATITUDE of {} is {}°N.'.format(cityI, latitudeI))
            break
        else:
            print('\nPlease ENTER a proper LATITUDE! >:|')


    ## City 2
    while True:
        cityII = input('\n\nNext, please ENTER the name of the second city: ')
        if cityII.isalpha() and len(cityII) > 0:
            print('\nAwesome! You\'ve stated that the first city is {}.'.format(cityII.title()))
            break
        else:
            print('\nPlease only ENTER chars a-z! >:|')


    while True:
        latitudeII = float(input('\nPlease ENTER the LATITUDE of {}: '.format(cityII.title())))
        if latitudeII is not float and latitudeII > 0:
            print('\nCool! You\'ve stated that the LATITUDE of {} is {}°N.'.format(cityII, latitudeII))
            break
        else:
            print('\nPlease ENTER a proper LATITUDE! >:|')

    ## AL = r * theta
    angle = latitudeI - latitudeII
    inRadian = math.radians(angle)
    inRadianRounded = float(format(inRadian, '.2f'))
    ## Earth Radius == 3960
    arcLength = 3960 * inRadianRounded
    arcLengthRounded = float(format(arcLength, '.2f'))

    print('\nAlmost done! :)')
    print('\nIn ending, what distance unit would you like us to output?')
    while True:
        distanceUnit = input('\nPlease choose between "miles", "km", or "meters": ')
        if distanceUnit == 'miles' or 'MILES':
            print('\nWe will thus ouput the distance between the two cities in MILES.')
            print('\n\nCalculation process now under progress.....')
            print('Progress - 25%')
            print('Progress - 47%')
            print('Progress - 59%')
            print('Progress - 72%')
            print('Progress - 99%')
            print('Progress is now COMPLEATE!!!')
            print('\nThe distance between {} and {} is {} miles.'.format(cityI.title(), cityII.title(), arcLengthRounded))
            break
        if distanceUnit == 'km' or 'KM':
            print('\nWe will thus ouput the distance between the two cities in KM.')
            print('\n\nCalculation process now under progress.....')
            print('Progress - 25%')
            print('Progress - 47%')
            print('Progress - 59%')
            print('Progress - 72%')
            print('Progress - 99%')
            print('Progress is now COMPLEATE!!!')
            arcLengthRounded = arcLengthRounded * 1.609347
            print('\nThe distance between {} and {} is {} KM.'.format(cityI.title(), cityII.title(), arcLengthRounded))
            break
        if distanceUnit == 'meters' or 'METERS':
            print('\nWe will thus ouput the distance between the two cities in METERS.')
            print('\n\nCalculation process now under progress.....')
            print('Progress - 25%')
            print('Progress - 47%')
            print('Progress - 59%')
            print('Progress - 72%')
            print('Progress - 99%')
            print('Progress is now COMPLEATE!!!')
            arcLengthRounded = arcLengthRounded * 1609.344
            print('\nThe distance between {} and {} is {} METERS.'.format(cityI.title(), cityII.title(), arcLengthRounded))
            break
        else:
            print('\nPlease only choose between "miles", "km", or "meters"! >:|')

## Script______________________________________________________________________________________________________________

print('\n\t\t\tWelcom to the "Distance Between Two Cities" Script!')

print('\nThis script will essentily calculate the distance between two cities using the specifed unit of distance as requested by the user.')

while True:
    usersName = input('\nIn begginging, please ENTER your name: ')
    if usersName.isalpha() and len(usersName) > 0:
        print('\nAwesome! We may now continue {}.'.format(usersName.title()))
        break
    else:
        print('\nPlease only ENTER chars a-z! >:|')

print('\nYou will now be taken to the MAIN CONSOLE.')
print('\nLet\'s head there now.')

print('\nLOADING.................')
print('\n&nd DONE!')

mainConsole()
