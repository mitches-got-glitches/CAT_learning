### Solution to Check Primality Functions in practicepython.org

def get_integer(prompt):
    """Returns integer value for input. Prompt is displayed as text."""
    return int(input(prompt))

def check_prime(number):
    """Returns True for prime numbers, False otherwise."""
    divisors = [x for x in range(1, number+1) if number % x == 0]
    if divisors == [1, number]:
        return True
    else:
        return False
    
def print_prime(number):
    """Checks if a number is prime and prints the outcome."""
    prime = check_prime(number)
    if prime:
        print("{0} is a prime number.".format(number))
    else:
        print("{0} is not a prime number.".format(number))
    
def main():
    while True:
        prompt = "Enter a number to check prime. Ctrl+C to exit: "
        print_prime(get_integer(prompt))
        
if __name__ == "__main__":
    main()
    
def solution():
    print("""
    ### Solution to Check Primality Functions in practicepython.org

    def get_integer(prompt):
        \"\"\"Returns integer value for input. Prompt is displayed as text.\"\"\"
        return int(input(prompt))
    
    def check_prime(number):
        \"\"\"Returns True for prime numbers, False otherwise.\"\"\"
        divisors = [x for x in range(1, number+1) if number % x == 0]
        if divisors == [1, number]:
            return True
        else:
            return False
        
    def print_prime(number):
        \"\"\"Checks if a number is prime and prints the outcome.\"\"\"
        prime = check_prime(number)
        if prime:
            print("{0} is a prime number.".format(number))
        else:
            print("{0} is not a prime number.".format(number))
        
    def main():
        while True:
            prompt = "Enter a number to check prime. Ctrl+C to exit: "
            print_prime(get_integer(prompt))
        
if __name__ == "__main__":
    main()
    """)