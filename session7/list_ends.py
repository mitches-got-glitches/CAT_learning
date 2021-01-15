### Solution to List Ends Challenge (12) on practicepython.org

def get_list_ends(list_):
    """Takes a list and returns the items at the start and end."""
    return [list_[0], list_[-1]]

def main():
    my_list = [765, 'ace', 20, 'twenty', 'bullseye']
    ends = get_list_ends(my_list)
    return ends

if __name__ == "__main__":
    ends = main()

def solution():
    print("""
def get_list_ends(list_):
    \"\"\"Takes a list and returns the items at the start and end\"\"\"
    return [list_[0], list_[-1]]

def main():
    my_list = [765, 'ace', 20, 'twenty', 'bullseye']
    ends = get_list_ends(my_list)
    return ends

if __name__ == "__main__":
    ends = main()
    """)

def hint1():
	print("""
Functions are defined in the following format:
	
def my_function(arg1, arg2, ...):
	\"\"\"Docstring describing the function...\"\"\"
	# Code that the does the work.
	return output
""")

def hint2():
	print("""
To get the last element in the list use negative indexing: my_list[-1]
""")

	