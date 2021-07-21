from gameoptions import GameOptions
import re
import getpass
import random



class GuessingGame(GameOptions):

   
    def _is_winner(self, person):
        GameOptions.player_won(person)
                
    def __main__(self):
        Break = False
        
        # game menu: single or multi?
        while not Break:
                mode = input('Single or Multiplayer? (single|1|one, multiplayer|multi|2) ').strip().lower()
                if mode in GameOptions.cmd:
                    Break = GameOptions._quit()
                elif re.search('^(m|t|2)',mode):
                    mode = 'Multi'
                    break
                elif re.search('^(s|o|1)',mode):
                    break
                else:
                    print("Invalid input")


        # select number of guesses
        while not Break:
            n = input("Enter number of guesses: ")
            try:
                assert int(n)
                break
            except ValueError:
                if n in GameOptions.cmd:
                    Break = GameOptions._quit()
                else:
                    print('Enter a valid integer or quit command')

        # select player
        while not Break:
            player = input('Which player is guessing the number? (1/2) ').strip().lower()
            
            if re.search('^(1|o)',player):
                player = 1
                break
            elif re.search('^(2|t)',player):
                player = 2
                break
            elif player in GameOptions.cmd:
                Break = GameOptions._quit()
            else:
                print('Enter valid player') 

             
        # main game loop
        while not Break:
            if mode == 'Multi':

                # select number to be guessed
                while not Break:
                    if player == 1:
                        ans = getpass.getpass(prompt='Player2 enter the number between 0 and 50:')
                    else:
                        ans = getpass.getpass(prompt='Player1 enter the number between 0 and 50:')
                    
                    try:
                        assert int(ans)
                        break
                    except ValueError:
                        if ans in GameOptions.cmd:
                            Break = GameOptions._quit()
                            
                        
                if Break:
                    break
                
                # guess: multiplayer
                print(f"Player {player}")
                self.play(person=player, answer=ans, ns=n, Multiplayer=True)
            
            # select number and guess: single player
            else:
                ans = random.randint(0,50)
                self.play(person=player, answer=ans, ns=n)

            Break = GameOptions.play_again(Break)

    # game logic loop         
    def play(self, person, answer, ns, Multiplayer=False):
        guesses = 0
        Break = False
        # enter guess, check if its correct
        while guesses <= int(ns) and not Break:
            # enter guess and validate data
            while not Break:
                guess = input('Guess...: ')
                try:
                    assert int(guess)
                    break
                except ValueError:
                    if guess in GameOptions.cmd:
                        Break = GameOptions._quit()
                        if Break:
                            break
                    else:
                        print('Enter a valid integer or quit command')
                
            if Break:
                break
                
            guesses += 1 
            
            # you win
            if int(guess) == int(answer):
                print('Thats correct!')
                self._is_winner(person)
                break
                

            # you lose
            elif int(guess) != int(answer) and guesses >= int(ns):
                print('Nope. You lose :(')
                break
                

            else:
                if int(guess) > int(answer):
                    print('Nope. Go lower. Keep guessing...')
                elif int(guess) < int(answer):
                    print('Nope. Go higher. Keep guessing...')
    
   

if __name__ == "__main__":
    GuessingGame().__main__()
    print(GameOptions.score)