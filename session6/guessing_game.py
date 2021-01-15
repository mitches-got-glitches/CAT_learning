# Solution to Guessing Game One on practicepython.org

import random

def main():
    guess = None
    guess_count = 0
    win_count = 0
    
    print("Game started...")
    print("At any time type 'exit' to quit the game.")
    
    while guess != 'exit':
        number = random.randint(1, 9)

        while guess != number:
            guess = input("Can you guess the number between"
                          + " 1 and 9 (inclusive)?: ")
            
            if guess == 'exit':
                print("Game ended...")
                print("Thanks for playing, you guessed correctly"
                      + " {0} times out of {1}!".format(win_count,guess_count))
                break
            
            try:
                int(guess)
            except ValueError:
                print("Did you mean 'exit'. "
                      + "Type a number or type 'exit' to quit the game.")
                continue
            
            guess = int(guess)
            
            if guess >= 10 or guess <= 0:
                print("You entered a number outside the range.")
                continue
            elif guess == number:
                print("You guessed correctly! Well done.")
                win_count += 1
            elif guess < number:
                print("You were too low, guess again!")
            else:
                print("You were too high, guess again!")
        
            guess_count += 1
                
if __name__ == "__main__":
    main()
    
def solution():
    print("""
    import random

    def main():
        guess = None
        guess_count = 0
        win_count = 0
        
        print("Game started...")
        print("At any time type 'exit' to quit the game.")
        
        while guess != 'exit':
            number = random.randint(1, 9)
    
            while guess != number:
                guess = input("Can you guess the number between"
                              + " 1 and 9 (inclusive)?: ")
                
                if guess == 'exit':
                    print("Game ended...")
                    print("Thanks for playing, you guessed correctly"
                          + " {0} times out of {1}!".format(win_count, guess_count))
                    break
                
                try:
                    int(guess)
                except ValueError:
                    print("Did you mean 'exit'. "
                          + "Type a number or type 'exit' to quit the game.")
                    continue
                
                guess = int(guess)
                
                if guess >= 10 or guess <= 0:
                    print("You entered a number outside the range.")
                    continue
                elif guess == number:
                    print("You guessed correctly! Well done.")
                    win_count += 1
                elif guess < number:
                    print("You were too low, guess again!")
                else:
                    print("You were too high, guess again!")
            
                guess_count += 1
                    
    if __name__ == "__main__":
        main()
    """)
