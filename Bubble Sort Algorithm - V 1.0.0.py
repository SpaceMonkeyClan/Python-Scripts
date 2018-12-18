# Bubble Sort Algorithm - V 1.0.0
# Author: Dena, Rene
# Last Modified: 5/26/17

## Misc.

import sys


## Functions



def Main():
	
	nums = []
	while True:
	    try:
	        one = int(input("Please enter first integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        two = int(input("Please enter second integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        three = int(input("Please enter third integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        four = int(input("Please enter fourth integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        five = int(input("Please enter fifth integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        six = int(input("Please enter sixth integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        seven = int(input("Please enter seventh integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        eight = int(input("Please enter eighth integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        nine = int(input("Please enter ninth integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")
	while True:
	    try:
	        ten = int(input("Please enter tenth integer: "))
	        break
	    except ValueError:
	        print("Not a valid integer! Please try again ...")

	nums.append(one)
	nums.append(two)
	nums.append(three)
	nums.append(four)
	nums.append(five)
	nums.append(six)
	nums.append(seven)
	nums.append(eight)
	nums.append(nine)
	nums.append(ten)

	print('\nThe numbers you have entered include: {}'.format(nums))
	print('\n')
	print('\n\t\t\tWelcome to the MAIN CONSOLE!')
	print('The starting LIST is: {}'.format(nums))
	print('\nProcess now underway.....')
	print('\n')
	while True:
		print(nums)
		if nums[9] < nums[8]:
			a, b = nums.index(nums[9]), nums.index(nums[8])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		if nums[8] < nums[7]:
			a, b = nums.index(nums[8]), nums.index(nums[7])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		if nums[7] < nums[6]:
			a, b = nums.index(nums[7]), nums.index(nums[6])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		if nums[6] < nums[5]:
			a, b = nums.index(nums[6]), nums.index(nums[5])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		if nums[5] < nums[4]:
			a, b = nums.index(nums[5]), nums.index(nums[4])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		if nums[4] < nums[3]:
			a, b = nums.index(nums[4]), nums.index(nums[3])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		if nums[3] < nums[2]:
			a, b = nums.index(nums[3]), nums.index(nums[2])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		if nums[2] < nums[1]:
			a, b = nums.index(nums[2]), nums.index(nums[1])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		if nums[1] < nums[0]:
			a, b = nums.index(nums[1]), nums.index(nums[0])
			nums[b], nums[a] = nums[a], nums[b]
			print(nums)
		elif nums[0] < nums[1] and nums[1] < nums[2] and nums[2] < nums[3] and nums[3] < nums[4] and nums[4] < nums[5] and nums[5] < nums[6] and nums[6] < nums[7] and nums[7] < nums[8] and nums[8] < nums[9]:
			print('+-----------------------------+')
			print(nums)
			print('+-----/\.ASSORTED LIST./\-----+')
			print('\nAlgorithmic assortment is now complete!')
			while  True:
				choice = input('\nWould you like to RE-RUN the script? "yes" OR "no": ')
				if choice == 'yes':
					print('\nAwesome! You\'ve selected to RE-RUN the script.')
					print('\nHeading to the MAIN CONSOLE now!')
					print('\nLOADING...............')
					Main()
				elif choice == 'no':
					print('\nBummer! You\'ve decided to END the script.')
					print('\nHope you enjoyed.) You\'ll now be kicked from script shortly.')
					print('\nLOADING...............')
					print('\nYou have now been kicked from script. Good day :)')
					sys.exit()
				else:
					print('\nPlease only ENTER "yes" OR "no"! >:|')
			break


## Strictly Script

print('\n\t\t\tWelcome to "Bubble Sort Algorithms" Calculator!')

while True:
	name = input('\nBefore we begin, please ENTER you name: ')
	if name.isalpha():
		print('\nAwesome! We may now continue {}.'.format(name.title()))
		print('\nLet\'s head to the MAIN CONSOLE now!')
		print('\nLOADING................')
		print('\n')
		Main()
		break
	else:
		print('\nPlease only ENTER characters a-z only! >:|')

