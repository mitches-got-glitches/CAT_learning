### Solution to Fibonacci Challenge (13) on practicepython.org

def ask_for_numbers(message):
    """Prompts the user for a number with the given message.
    Returns the user input as an integer.
    """
    return int(input(message))


def fibonacci_generator(x):
    """Generates a Fibonacci sequence of length x."""
    if x >= 1:
        fib_seq = [1]
    if x >= 2:
        fib_seq.append(1)
    if x >= 3:
        for i in range(2, x):
            fib_seq.append(sum(fib_seq[-2:]))
    
    return fib_seq


def main():
    message = "How many Fibonacci numbers do you want? "
    return fibonacci_generator(ask_for_numbers(message))


if __name__ == "__main__":
    fib_seq = main()
    print(fib_seq)
    
    
def solution():
    print("""
def ask_for_numbers(message):
    \"\"\"Prompts the user for a number with the given message.
    Returns the user input as an integer.
    \"\"\"
    return int(input(message))


def fibonacci_generator(x):
    \"\"\"Generates a Fibonacci sequence of length x\"\"\"
    if x >= 1:
        fib_seq = [1]
    if x >= 2:
        fib_seq.append(1)
    if x >= 3:
       for i in range(2, x):
            fib_seq.append(sum(fib_seq[-2:]))
        
    return fib_seq


def main():
    message = "How many Fibonacci numbers do you want? "
    return fibonacci_generator(ask_for_numbers(message))


if __name__ == "__main__":
    fib_seq = main()
    print(fib_seq)
    """)
    