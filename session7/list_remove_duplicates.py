### Solution to List Remove Duplicates Challenge (14) on practicepython.org

def remove_duplicates_using_loop(list_):
    """Takes a list and returns a list of the unique values."""
    unique_values = []
    for elem in list_:
        if elem not in unique_values:
            unique_values.append(elem)
    return unique_values

def remove_duplicates_using_sets(list_):
    """Takes a list and returns a list of the unique values."""
    return list(set(list_))

def main():
    my_list = [2, 3, 65, 3, 'cheese', 'beans', 7, 3, 2, 'cheese', 765]
    print(remove_duplicates_using_loop(my_list))
    print(remove_duplicates_using_sets(my_list))

if __name__ == "__main__":
    main()
	
def solution():
	print("""
def remove_duplicates_using_loop(list_):
    \"\"\"Takes a list and returns a list of the unique values\"\"\"
    unique_values = []
    for elem in list_:
        if elem not in unique_values:
            unique_values.append(elem)
    return unique_values

def remove_duplicates_using_sets(list_):
    \"\"\"Takes a list and returns a list of the unique values\"\"\"
    return list(set(list_))

def main():
    my_list = [2, 3, 65, 3, 'cheese', 'beans', 7, 3, 2, 'cheese', 765]
    print(remove_duplicates_using_loop(my_list))
    print(remove_duplicates_using_sets(my_list))

if __name__ == "__main__":
    main()
	""")