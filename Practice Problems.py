## Practice Problems - V 1.0.0
## Author: Dena, Rene
## Last Modified: 7/7/16

#________________________________________________________Misc.__________________________________________________________

import random

#________________________________________________________Functions______________________________________________________

'''
def replay():
    while True:
        userChoiceI = float(input('So what\'s the chapter?: '))
        if userChoiceI == 0:
            print('\nYou\'ve selected to randomized a problem within all chapters.\n')
            chapters = [5.2, 5.4, 5.5, 5.6, 7.2, 7.3]
            chapter = random.choice(chapters)
            if chapter == 5.2:
            	nums = [41, 43, 45]
            	randNums = random.choice(nums)
            elif chapter == 5.4:
            	nums = [1,3,5,7,9,11,13,15,17,19,21,23,25,47,49]
            	randNums = random.choice(nums)
            elif chapter == 5.5:
                nums = [17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49]
                randNums = random.choice(nums)
            elif chapter == 5.6:
            	nums = [1,3,9,11,13,19]
            	randNums = random.choice(nums)
            elif chapter == 7.2:
            	nums = [0]
            	randNums = random.choice(nums)
            elif chapter == 7.3:
            	nums = [0]
            	randNums = random.choice(nums)
            print('Do problem #{} from chapter {}\n'.format(randNums, chapter))
            replay()
            break
        elif userChoiceI == 5.2:
        	print('\nYou\'ve selected to randomized a problem within chapter: {}\n'.format(userChoiceI))
        	chapter = 5.2
        	nums = [1, 2]
        	randNums = random.choice(nums)
        	print('Do problem #{} from chapter {}.\n'.format(randNums, chapter))
        	replay()
        	break
        elif userChoiceI == 5.4:
        	print('\nYou\'ve selected to randomized a problem within chapter: {}\n'.format(userChoiceI))
        	chapter = 5.4
        	nums = [3, 4]
        	randNums = random.choice(nums)
        	print('Do problem #{} from chapter {}.\n'.format(randNums, chapter))
        	replay()
        	break
        elif userChoiceI == 5.5:
        	print('\nYou\'ve selected to randomized a problem within chapter: {}\n'.format(userChoiceI))
        	chapter = 5.5
        	nums = [5, 6]
        	randNums = random.choice(nums)
        	print('Do problem #{} from chapter {}.\n'.format(randNums, chapter))
        	replay()
        	break
        elif userChoiceI == 5.6:
        	print('\nYou\'ve selected to randomized a problem within chapter: {}\n'.format(userChoiceI))
        	chapter = 5.6
        	nums = [7, 8]
        	randNums = random.choice(nums)
        	print('Do problem #{} from chapter {}.\n'.format(randNums, chapter))
        	replay()
        	break
        elif userChoiceI == 7.2:
        	print('\nYou\'ve selected to randomized a problem within chapter: {}\n'.format(userChoiceI))
        	chapter = 7.2
        	nums = [7, 8]
        	randNums = random.choice(nums)
        	print('Do problem #{} from chapter {}.\n'.format(randNums, chapter))
        	replay()
        	break
        elif userChoiceI == 7.3:
        	print('\nYou\'ve selected to randomized a problem within chapter: {}\n'.format(userChoiceI))
        	chapter = 7.3
        	nums = [7, 8]
        	randNums = random.choice(nums)
        	print('Do problem #{} from chapter {}.\n'.format(randNums, chapter))
        	replay()
        	break
        else:
            print('\nPlease ENTER a proper chapter! >:|')


print('\nIn starting, please select a certin chapther or ENTER \'0\' to randomize a problem within all chapter.\n')
'''

#________________________________________________________Strickly Script________________________________________________

# replay()

print('\n\t\t\tWelcome to the "Practice Problems" Script!')

while True:
    number_of_chapters = int(input('\nIn starting, please enter the total number of chapters: '))
    if number_of_chapters > 0:
        print('\nAwesome! You\'ve selected {} chapters.'.format(number_of_chapters))
        break
    else:
        print('\nPlease only enter a integer! >:|')

chapters = []
i = 1
while (i < (number_of_chapters+1)):
    if i == 1:
        chap = int(input('\nPlease enter the {}st chapter: '.format(i)))
        i += 1
        chapters.append(chap)
    if i == 2:
        chap = int(input('\nPlease enter the {}nd chapter: '.format(i)))
        i += 1
        chapters.append(chap)
    if i == 3:
        chap = int(input('\nPlease enter the {}rd chapter: '.format(i)))
        i += 1
        chapters.append(chap)
    else:
        chap = int(input('\nPlease enter the {}th chapter: '.format(i)))
        i += 1
        chapters.append(chap)

print(chapters)

print('\nNext, you\'ll need to enter the problems per chapther.')
print('\nSo let\'s do that now.')
print('\nLOADING...............')



i = 0
while (i < (number_of_chapters+1)):
    problem_numbers = []
    
