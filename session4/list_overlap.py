### Solution to the list overlap challenge on practicepython.org

# Define the lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = []
for element in a:
    # Check that the element is in b, but not already in
    # common_elements so we don't get any duplicates
    if element in b and element not in common_elements:
        common_elements.append(element)

# Print out the common elements
print("The common elements in the pre-defined lists are: ")
print(common_elements)

## Extra challenge 1
# Import the built-in random library
import random

# Create lists a and b of random length between 1 and 100
# Fill the lists with random integers between 1 and 100
a = []
for x in range(1, random.randint(1, 101)):
    a.append(random.randint(1, 101))
    
b = []
for x in range(1, random.randint(1, 101)):
    b.append(random.randint(1, 101))
    
common_elements = []
for element in a:
    if element in b and element not in common_elements:
        common_elements.append(element)
        
print("The common elements in the random lists are: ")
print(common_elements)

## Extra challenge 2
# Use list comprehensions to define a and b
a = [random.randint(1, 101) for x in range(random.randint(1, 101))]
b = [random.randint(1, 101) for x in range(random.randint(1, 101))]

# Find the common elements using set theory
common_elements = list(set(a).intersection(b))

print("The common elements in the random lists are: ")
print(common_elements)

def solution():
    print("""
        ### Solution to the list overlap challenge on practicepython.org
        
        # Define the lists
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        common_elements = []
        for element in a:
            # Check that the element is in b, but not already in
            # common_elements so we don't get any duplicates
            if element in b and element not in common_elements:
                common_elements.append(element)
        
        # Print out the common elements
        print("The common elements in the pre-defined lists are: ")
        print(common_elements)
        
        # Extra 1
        # Import the built-in "random" library
        import random
        
        # Create lists a and b of random length between 1 and 100
        # Fill the lists with random integers between 1 and 100
        a = []
        for x in range(1, random.randint(1, 101)):
            a.append(random.randint(1, 101))
            
        b = []
        for x in range(1, random.randint(1, 101)):
            b.append(random.randint(1, 101))
            
        common_elements = []
        for element in a:
            if element in b and element not in common_elements:
                common_elements.append(element)
                
        print("The common elements in the random lists are: ")
        print(common_elements)
        
        # Extra 2
        
        # Use list comprehensions to define a and b
        a = [random.randint(1, 101) for x in range(random.randint(1, 101))]
        b = [random.randint(1, 101) for x in range(random.randint(1, 101))]
        
        # Find the common elements using set theory
        common_elements = list(set(a).intersection(b))
        
        print("The common elements in the random lists are: ")
        print(common_elements)
    """
    )
