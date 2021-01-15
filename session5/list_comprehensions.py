### Solution to the List Comprehensions challenge on practicepython.org

def main():
    # Use list comprehension to create the first 10 square numbers
    square_numbers = [x**2 for x in range(1, 11)]
    
    # Get a sublist of even numbers
    even_numbers = [x for x in square_numbers if x % 2 == 0]
    
    print("The even numbers are: {0}".format(even_numbers))


def solution():
    print("""
    ### Solution to the List Comprehensions challenge on practicepython.org
    
    # Use list comprehension to create the first 10 square numbers
    square_numbers = [x**2 for x in range(1, 11)]
    
    # Get a sublist of even numbers
    even_numbers = [x for x in square_numbers if x % 2 == 0]
    
    print("The even numbers are: {0}".format(even_numbers))
    """
    )

if __name__ == "__main__":
    main()