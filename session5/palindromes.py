### Solution to the String Lists challenge on practicepython.org

def main():
    user_string = input('Input a string to test if it\'s a palindrome: ')
    
    # String reversal method
    rvs = user_string[::-1]
    
    # For loops and function method
    def reverse(word):
        x = ''
        for i in range(len(word)):
            x += word[(len(word)-1) - i]
        return x
    
    rvs2 = reverse(user_string)
    
    # Change both strings to lowercase before testing equality
    if user_string.lower() == rvs.lower():
        print('{0} is a palindrome.'.format(user_string))
    else:
        print('That\'s not a palindrome.')


def solution():
    print("""
    ### Solution to the String Lists challenge on practicepython.org

    user_string = input('Input a string to test if it\'s a palindrome: ')
    
    # String reversal method
    rvs = user_string[::-1]
    
    # For loops and function method
    def reverse(word):
        x = ''
        for i in range(len(word)):
            x += word[(len(word)-1) - i]
        return x
    
    rvs2 = reverse(user_string)
    
    # Change both strings to lowercase before testing equality
    if user_string.lower() == rvs.lower():
        print('{0} is a palindrome.'.format(user_string))
    else:
        print('That\'s not a palindrome.')
    """
    )
    
if __name__ == "__main__":
    main()