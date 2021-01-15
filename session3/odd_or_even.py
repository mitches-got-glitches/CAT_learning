### Solution to Odd Or Even challenge on practicepython.org

if __name__ == "__main__":
	# Ask for a number
	test_number = input('Please type a number: ')

	# Convert the string to an int so that you can use arithmetic
	test_number = int(test_number)

	if test_number % 2 == 0:
		print('That number is even!')
	else:
		print('The number is odd.')
		
	if test_number % 4 == 0:
		print('And it\'s also divisible by 4!')
		
	num = int(input('Give me another number: '))
	check = int(input('Type a number to check if divisible by: '))

	if num % check == 0:
		print('{0} is divisible by {1}!'.format(num, check))
	else:
		print('It\'s not divisible, there\'s a remainder of {0}'.format(num % check))

def solution():
	print("""
	# Ask for a number
	test_number = input('Please type a number: ')

	# Convert the string to an int so that you can use arithmetic
	test_number = int(test_number)

	if test_number % 2 == 0:
		print('That number is even!')
	else:
		print('The number is odd.')
		
	if test_number % 4 == 0:
		print('And it\'s also divisible by 4!')
		
	num = int(input('Give me another number: '))
	check = int(input('Type a number to check if divisible by: '))

	if num % check == 0:
		print('{0} is divisible by {1}!'.format(num, check))
	else:
		print('It\'s not divisible, there\'s a remainder of {0}'.format(num % check))
	""")