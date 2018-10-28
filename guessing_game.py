# Dear Treehouse Grader,
#	Thank you for taking the time to review my project. As you can see, I am shooting for the "Exceeds" score.
# However, if my project only "Meets" requirements, that is okay. In this case, please do not reject my project.
# Thanks again. Happy grading!
# -Jeremy

import random
import sys


attempt_history = []



def start_game():
    print("\nWelcome to the Number Guessing Game!\n")
    number = random.randint(1,10)
    guess = ()
    attempts = 0
    
    while guess != number:
        try:
            guess = input("Pick a number between 1 and 10: ")
            guess = int(guess)
            
            if guess > 10:
                raise ValueError
            elif guess < 1:
                raise ValueError
            attempts += 1
            if guess > number:
                print("It's lower!")
            elif guess < number:
                print("It's higher!")
            elif guess == number:
                print("You got it! It took you {} tries.".format(attempts))
                play_again = input("\nWould you like to play again? [y]es/[n]o: ")
                if play_again.lower() == "y":
                    attempt_history.append(attempts)
                    # asceding sort method from stackoverflow.com
                    # https://stackoverflow.com/questions/9758959/sort-a-list-of-numerical-strings-in-ascending-order
                    attempt_history.sort(key=int)
                    print("\nTHE HIGHSCORE IS {}".format(attempt_history[0]))
                    start_game()
                else:
                    sys.exit("\nClosing game, thank you for playing!!!")
        except ValueError:
            print("\nOh no, that is not a valid input! Please try again.")
        
        
if __name__ == '__main__':
    start_game()
    