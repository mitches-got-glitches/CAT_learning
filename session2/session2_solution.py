# My program to calculate the year the user turns 100

def solution():
	print("""
		name = input('Please enter you name: ')
		print('Your name is ' + name)

		age = input('Please enter your age: ')
		print('Your age is ' + age)

		current_year = 2019
		birth_year = current_year - int(age)
		year100 = birth_year + 100

		message = name + ', you will turn 100 in the year ' + str(year100)
		print(message)

		# Extension 1
		repeats = int(input('How many times would you like me to tell you? '))
		print(message * repeats)

		# Extension 2
		print(('\n' + message) * repeats) """)