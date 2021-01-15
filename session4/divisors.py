### Solution to the divisors challenge on practicepython.org

# Take the user input and store as a variable
user_num = input("Enter a number for a list of divisors: ")

# Test that the user input is integer, if not, ask again
integer = False
while not integer:
    try:
        user_num = int(user_num)
    except ValueError:
        print("{0} is not a valid integer.".format(user_num))
        user_num = input("Please enter a valid integer: ")
    else:
        integer = True

# Create a list of all integers from one up to and including the
# user defined number
possible_divs = range(1, user_num+1)

# Initialise an empty list for the divisors
divisors = []

# Loop through possible divisors, test if divisor, and if so - append.
for number in possible_divs:
    
    if user_num % number == 0:
        divisors.append(number)

# Print out the divisors using a list comprehension
print("The following numbers are divisors of {0}:".format(user_num))
print(divisors)

def solution():
    print("""
        ### Solution to the divisors challenge on practicepython.org
        
        # Take the user input and store as a variable
        user_num = input("Enter a number for a list of divisors: ")
        
        # Test that the user input is integer, if not, ask again
        integer = False
        while not integer:
            try:
                user_num = int(user_num)
            except ValueError:
                print("{0} is not a valid integer.".format(user_num))
                user_num = input("Please enter a valid integer: ")
            else:
                integer = True
        
        # Create a list of all integers from one up to and including the
        # user defined number
        possible_divs = range(1, user_num+1)
        
        # Initialise an empty list for the divisors
        divisors = []
        
        # Loop through possible divisors, test if divisor, and if so - append.
        for number in possible_divs:
    
            if user_num % number == 0:
                divisors.append(number)
        
        # Print out the divisors using a list comprehension
        print("The following numbers are divisors of {0}:".format(user_num))
        print(divisors)
    """
    )