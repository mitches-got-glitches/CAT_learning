### The solution to List Less Than Ten challenge on practicepython.org

if __name__ == "__main__":
	# Define the list
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	
	for num in a:
		if num < 5:
			print(num)
	
	# Extra 1
	# Initialise an empty list
	new_a = []
	
	for num in a:
		if num < 5:
			new_a.append(a)
			
	# Extra 2
	new_a = [num for num in a if num < 5]
	
	
	# Extra 3
	this = int(input('Return values in the list less than this: '))
	new_a = [num for num in a if num < this]

def solution():
	print(
	"""
	# Define the list
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	
	for num in a:
		if num < 5:
			print(num)
	
	# Extra 1
	# Initialise an empty list
	new_a = []
	
	for num in a:
		if num < 5:
			new_a.append(a)
			
	# Extra 2
	new_a = [num for num in a if num < 5]
	
	
	# Extra 3
	this = int(input('Return values in the list less than this: '))
	new_a = [num for num in a if num < this]
	"""
	)