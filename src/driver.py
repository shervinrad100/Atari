from hangman import Hangman
from gameoptions import GameOptions
from xnos import XnOs
from quickmafs import QuickMafs
from guessinggame import GuessingGame
import re

class Driver(GameOptions):
    def __init__(self):
        self._run = True
    
    def __main__(self):
        while self._run:
            print("\n")
            print('######### Main menu #########')
            print('scores:',GameOptions.score)

            # prompt player to select a game
            prompt = input(f'Choose game\n{GameOptions.games}\n').strip().lower()
                
            # game selection and confirmation to start
            
            # Quit 
            if prompt in GameOptions.cmd:
                Break = input(f'Shutdown Cartrige? (yes/no) ')
                if Break in GameOptions.cmd2:
                    break
                elif Break in GameOptions.cmd:
                    pass
                else:
                    print('Unrecognisable input')

            #XnOs
            elif re.search("^x", prompt):
                start = input(f'Start XnOs? (yes/no) ').strip().lower() 
                if start in GameOptions.cmd2:
                    XnOs().__main__()
                elif start in GameOptions.cmd:
                    pass
                else:
                    print('Unrecognisable input')

            # Hangman
            elif re.search("^ha", prompt):
                start = input(f'Start Hangman? (yes/no) ').strip().lower() 
                if start in GameOptions.cmd2:
                    Hangman().__main__()
                elif start in GameOptions.cmd:
                    pass
                else:
                    print('Unrecognisable input')
            
            # help
            elif re.search("^he", prompt):
                need_help = input("Need help? (yes/no) ")
                if need_help in GameOptions.cmd2:
                    print(GameOptions.helpstring)
                elif need_help in GameOptions.cmd:
                    pass
                else:
                    print('Unrecognisable input')
            
            #GuessingGame
            elif re.search("^gue", prompt):
                start = input(f'Start GuessTheNumber? (yes/no) ').strip().lower() 
                if start in GameOptions.cmd2:
                    GuessingGame().__main__()
                elif start in GameOptions.cmd:
                    pass
                else:
                    print('Unrecognisable input')


            #QuickMafs
            elif re.search("maf", prompt):
                start = input(f'Start QuickMafs? (yes/no) ').strip().lower() 
                if start in GameOptions.cmd2:
                    QuickMafs().__main__()
                elif start in GameOptions.cmd:
                    pass
                else:
                    print('Unrecognisable input')
            
            # reset scores
            elif re.search('^reset',prompt) or re.search('^r+sc',prompt): 
                confirm = input("Are you sure? ")
                if confirm in GameOptions.cmd2:
                    GameOptions.reset_score()
                elif Break in GameOptions.cmd:
                    pass
                else:
                    print('Unrecognisable input')
                
            else:
                print("For game help and functionalities type 'help'")
                print("To quit type: ")
                print(GameOptions.cmd)
                

if __name__ == "__main__":
    Driver().__main__()