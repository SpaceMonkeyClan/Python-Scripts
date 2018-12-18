import random

def OptionZero():
    randFunc = [OptionOne(), OptionTwo(), OptionThree(), OptionFour(), OptionFive(), OptionSix(), OptionSeven(), OptionEigth()]
    pass


def OptionOne():
    chapter = 3.2
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    randNums = random.choice(nums)
    print('\nDo problem #{} from chapter {}.'.format(randNums, chapter)



print('\n\t\t\tWelcome to the "RANDOMIZED NUMBER CALCULATOR"!\n\n')

print('\nIn starting, please select a certin chapther or ENTER \'0\' to randomize a problem within all chapter.\n')

 
while True:
    userChoiceI = float(input('\nSo what\'s the chapter?: '))
    if userChoiceI == 0:
        print('\nYouv\'ve selected to randomized a problem within all chapters.\n')
        OptionZero()
        break
    elif userChoiceI == 3.2:
        print('\nYouv\'ve selected to randomized a problem within chapter {}.'.format(userChoiceI))
        OptionOne()
        break
    else:
        print('\nPlease ENTER a proper chapter! >:|')
