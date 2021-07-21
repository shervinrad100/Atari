from gameoptions import GameOptions
import re
import getpass
import random
from nltk.corpus import words
            
class Hangman(GameOptions):
    
    def __init__(self):        
        
        # init game mode options 
        self.single_mode = ['1','1v1','single']
        
        # initialise game graphics
        self.a_hanged_man = ['|----------'
                            ,'|         |  '
                            ,'|        (X) '
                            ,'|        /|\\'
                            ,'|         |  '
                            ,'|        / \\'
                            ,'|____________']

    def __win(self):
        if '_' in self.word_space:
            return False
        return True

    def print_the_man(self,lives):
        print(f'lives: {lives}')
        print('\n'.join(self.a_hanged_man[lives:]))
        
    def __main__(self):
        Break = False
        
        # main menu loop 

        # allow player to choose game mode
        while True:
            mode = input('Single or Multiplayer? ').strip().lower()
            if mode in GameOptions.cmd:
                Break = GameOptions._quit()
                break

            elif re.search('^(m|2|t)',mode) or mode not in self.single_mode:
                mode = 'Multi'
                break

            elif re.search('^(s|1|o)',mode) or mode in self.single_mode:
                mode = 'Single'
                break
            
            else:
                print("Invalid input")

        # who is guessing the word? 
        while not Break:
            player = input('Which player is guessing the word? (1/2) ').strip().lower()
            if player in GameOptions.cmd:
                Break = GameOptions._quit()
                break
            elif re.search('^(1|o)',player):
                player = 1
                break
            elif re.search('^(2|t)',player):
                player = 2
                break
            else:
                print("Invalid input")
                
        # word selection
        while not Break:     
            # if multiplayer, let one player choose word
            if mode == 'Multi':                    
                # enter the word
                while not Break:
                    if player == 1:
                        word = getpass.getpass(prompt='Player2 enter the word: ').lower()
                        break
                    elif player == 2:
                        word = getpass.getpass(prompt='Player1 enter the word: ').lower()
                        break
                    else:
                        print("Invalid input")

                if word in GameOptions.cmd:
                    Break = GameOptions._quit()  
                       
                                
            # if playing against computer, computer will pick a word at random    
            else:
                word = random.sample(words.words(),1)[0].lower()

            # initialise game variables
            self.word_space = ['_' for _ in range(len(word))]
            lives = 7 
            indexed_word = {index:letter for index,letter in enumerate(word)}
            guessed = []
                
            # game phase: guess the word
            while not Break:
                print(' '.join(self.word_space))

                # guess input and data validation loop
                while not Break:
                    guess = input('Enter your guess: ').strip().lower() 
                        
                    # data validation and quit check
                    try:
                        assert len(guess) == 1
                        break
                    except AssertionError:
                        if len(guess) != 1 and type(guess) != 'str':
                            if guess in GameOptions.cmd:
                                Break = GameOptions._quit()
                                if Break:
                                    break
                            else:
                                guess = input('Enter one letter as your guess: ').strip().lower()

                # check to see if they guessed it correctly   
                if guess not in word and guess not in guessed:
                    # if wrong take one life off and appened guessed list
                    lives -= 1
                    self.print_the_man(lives)
                    guessed.append(guess)
                elif guess in word and guess not in guessed:
                    # if correct, preview letter and append guessed list
                    guessed.append(guess)
                    for index,letter in indexed_word.items():
                        if letter == guess:
                            self.word_space[index] = guess
                elif guess in guessed:
                    # if letter already guessed give them another try
                    print('You have already guessed this')
                    print('')
                else:
                    print('Invalid input')

                # check to see if game is over: win
                if self.__win():
                    print('')
                    print('##### YOU WIN! #####')
                    print('')
                    GameOptions.player_won(player) 
                    print('The word is', ''.join(self.word_space).upper())
                    break
                    
                # check to see if game is over: lose
                if lives == 0:
                    print('')
                    print('##### You have been hanged #####')
                    print('')
                    print(f'The answer is: {word}')
                    break

            

            Break = GameOptions.play_again(Break)
    
    
            
    



if __name__ == "__main__":
    Hangman().__main__()
    print(GameOptions.score)