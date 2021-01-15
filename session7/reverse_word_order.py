### Solution to Reverse Word Order (15) on practicepython.org

def ask_for_long_string(message):
	"""Ask the user to input a string using message as a prompt."""
	return input(message)


def reverse_word_order(string):
	"""Return the words in the string in reverse order by splitting on 
	whitespace, reversing the list of word strings, then joining again
	on a single whitespace character.
	"""
	words = string.split()
	words.reverse()
	reversed_string = " ".join(words)
	return reversed_string


def main():
	message = "Please enter some words in a sentence: "
	reversed_string = reverse_word_order(ask_for_long_string(message))
	print(reversed_string)
	
	
if __name__ == "__main__":
	main()
	
	
def solution():
	print("""
def ask_for_long_string(message):
	\"\"\"Ask the user to input a string using message as a prompt\"\"\"
	return input(message)

def reverse_word_order(string):
	\"\"\"Return the words in the string in reverse order by splitting on 
	whitespace, reversing the list of word strings, then joining again
	on a single whitespace character.
	\"\"\"
	words = string.split()
	words.reverse()
	reversed_string = " ".join(words)
	return reversed_string

def main():
	message = "Please enter some words in a sentence: "
	reversed_string = reverse_word_order(ask_for_long_string(message))
	print(reversed_string)
	
if __name__ == "__main__":
	main()
	""")