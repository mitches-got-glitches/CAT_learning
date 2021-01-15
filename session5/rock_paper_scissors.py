### Solution for Rock Paper Scissors on practicepython.org

def take_pick(player_no):
    """Asks for a play from the player number determined by the argument."""
    def ask_for_pick():
        pick = input("Player {0}: Rock, Paper or Scissors? ".format(player_no))
        return pick.lower()
    
    def check_pick(pick):
        "Checks for a valid pick. If pick is not valid it will ask again."""
        while pick not in ['rock', 'paper', 'scissors']:
            print("That\'s not a valid selection, please pick again.")
            pick = ask_for_pick()
        return pick
    
    pick = ask_for_pick()
    pick = check_pick(pick)
    
    return pick

def play_game():
    """
    A two-player game of rock, paper, scissors. Both player select their play,
    and the winner is determined.    
    """
    p1 = take_pick(player_no=1)
    p2 = take_pick(player_no=2)
    while p1 == p2:
        print("A draw! Both picked {0}. Pick again.".format(p1))
        p1 = take_pick(1)
        p2 = take_pick(2)
    
    if p1 == 'rock':
        if p2 == 'scissors':
            return("P1 wins with rock. Rock blunts scissors.")
        else:
            return("P2 wins with paper. Paper wraps rock.")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return("P1 wins with scissors. Scissors cut paper.")
        else:
            return("P2 wins with rock. Rock blunts scissors.")
    elif p1 == 'paper':
        if p2 == 'scissors':
            return("P2 wins with scissors. Scissors cut paper.")
        else:
            return("P1 wins with paper. Paper wraps rock.")

def main():
    in_play = True

    while in_play:        
        print(play_game())
        
        play_again = input("Do you want to play again? (y/n) ").strip().lower()
        if play_again == 'n':
            in_play = False

if __name__ == "__main__":
    main()

def solution():
    print("""
    ### Solution for Rock Paper Scissors on practicepython.org
    
    def take_pick(player_no):
        \"\"\"Asks for a play from the player number determined by the argument.\"\"\"
        def ask_for_pick():
            pick = input("Player {0}: Rock, Paper or Scissors? ".format(player_no))
            return pick.lower()
        
        def check_pick(pick):
            "Checks for a valid pick. If pick is not valid it will ask again. \"\"\"
            while pick not in ['rock', 'paper', 'scissors']:
                print("That\'s not a valid selection, please pick again.")
                pick = ask_for_pick()
            return pick
        
        pick = ask_for_pick()
        pick = check_pick(pick)
        
        return pick
    
    def play_game():
         \"\"\"
        A two-player game of rock, paper, scissors. Both player select their play,
        and the winner is determined.    
         \"\"\"
        p1 = take_pick(player_no=1)
        p2 = take_pick(player_no=2)
        while p1 == p2:
            print("A draw! Both picked {0}. Pick again.".format(p1))
            p1 = take_pick(1)
            p2 = take_pick(2)
        
        if p1 == 'rock':
            if p2 == 'scissors':
                return("P1 wins with rock. Rock blunts scissors.")
            else:
                return("P2 wins with paper. Paper wraps rock.")
        elif p1 == 'scissors':
            if p2 == 'paper':
                return("P1 wins with scissors. Scissors cut paper.")
            else:
                return("P2 wins with rock. Rock blunts scissors.")
        elif p1 == 'paper':
            if p2 == 'scissors':
                return("P2 wins with scissors. Scissors cut paper.")
            else:
                return("P1 wins with paper. Paper wraps rock.")
    
    def main():
        in_play = True
    
        while in_play:        
            print(play_game())
            
            play_again = input("Do you want to play again? (y/n) ").strip().lower()
            if play_again == 'n':
                in_play = False
    
    if __name__ == "__main__":
        main()
    """
    )