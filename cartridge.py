import random
import re
import getpass
from nltk.corpus import words
import numpy as np
import time

class Cartrige():

    # init player commands
    cmd = ['quit','q', 'break', 'exit', 'n', 'no']
    cmd2 = ['yes', 'y', 'start']
    games = ['XnOs', 'Hangman','GuessingGame'] # add quickmafs, connect4
    score = {"Player1":0, "Player2":0}
    
    print("For game help and functionalities type 'help'")
    print("To quit type: ")
    print(cmd)
    
    def __init__(self):
        self._run = True
        
        
    
    def __main__(self):
        while self._run:
            print("\n")
            print('######### Main menu #########')
            print('scores:',self.score)
            # print list of games available to choose from 
            print('Choose game\n',self.games)

            # prompt player to select a game
            game = input()
                
            # game selection and confirmation to start
            
            #XnOs
            if re.search("^(X|x)", game):
                start = input(f'Start XnOs? (yes/no) ').strip().lower() 
                if start in self.cmd2:
                    XnOs().__main__()
                elif start in self.cmd:
                    pass
                else:
                    print('Unrecognisable input')

            # Hangman
            elif re.search("^(h|H)(a|A)", game):
                start = input(f'Start Hangman? (yes/no) ').strip().lower() 
                if start in self.cmd2:
                    Hangman().__main__()
                elif start in self.cmd:
                    pass
                else:
                    print('Unrecognisable input')
            # help
            elif re.search("^(h|H)(e|E)", game):
                need_help = input("Need help? (yes/no) ")
                if need_help in self.cmd2:
                    self._help()
                elif need_help in self.cmd:
                    pass
                else:
                    print('Unrecognisable input')
            
            #GuessingGame
            elif re.search("^(g|G)", game):
                start = input(f'Start GuessTheNumber? (yes/no) ').strip().lower() 
                if start in self.cmd2:
                    GuessingGame().__main__()
                elif start in self.cmd:
                    pass
                else:
                    print('Unrecognisable input')
                    
            # Quit 
            elif game in self.cmd:
                Break = input(f'Shutdown Cartrige? (yes/no) ').strip().lower()
                if Break in self.cmd2:
                    break
                elif Break in self.cmd:
                    pass
                else:
                    print('Unrecognisable input')
            
            elif re.search('^re',game):
                self.reset_score()
                continue
                
            else:
                print("For game help and functionalities type 'help'")
                print("To quit type: ")
                print(self.cmd)
                
                
                
    def _quit(self):
        confirm = input('Are you sure you want to quit? (yes/no) ')
        if confirm in self.cmd2:
            self._run = False
        else:
            print('Invalid input')
        
    def _help(self):
        string = '''
        Welcome to my game. The idea was to create a console Cartrige like that of Atari.
        Each cartrige has a few games. 
        You play the games with your friends and the cartrige keeps track of the scores. 
        I have tried to add as much freedom to the player as possible to if you mistype something the game wont break!
        You can quit any time using some keywords. *All inputs are case insensitive.*
        I have implemented regex to recognise the name of the game when you start on main menu.
        If you can think of new cool functionalities let me know and I'll add them in!
        Type "reset" to reset the scores
        '''
        print(string)
        
    def player_won(self, player):
        self.score["Player%i" %player] += 1
        
    def reset_score(self):
        self.score = {"Player1":0, "Player2":0}
        print("scores reset")


class XnOs(Cartrige):
        
    def __init__(self):
        # init 3x3 grid and available spaces for players to place pin
        super(XnOs,self).__init__()
        self.available = []
        self.grid = [[None for _ in range(3)] for _ in range(3)]
        for row in range(1,4):
            for col in range(1,4):
                self.grid[row-1][col-1] = str(row)+str(col)
                self.available.append(str(row)+str(col))
    
    def __main__(self): 
        
        # display grid
        for row in range(len(self.grid)):
            print(self.grid[row])
    
        
        # start with player 1 and let them pick their pin
        player = 1
        XO = input(f'Player {player} pick your pin (X or O):')

        

        # start game
        while self._run:
            # pin input assertion 
            try:
                assert XO.lower() in ['x','o']
            except AssertionError:
                # if player wants to quit take them to main menu (__main__)
                while XO.lower() not in ['x','o']:
                    if XO.lower() in self.cmd:
                        self._quit()
                        break
                    else:
                        XO = input(f"Player {player} pick either 'X' or 'O': ")
            
            if not self._run:
                break
            
            # player input location they want to place at
            rowcol = input(f'''Player {player} enter the grid num you want to place your pin: ''').strip()
            
            # input assertion
            try:
                assert rowcol in self.available
            except AssertionError:
                # if player wants to quit take them to main menu (__main__)
                while rowcol.lower() not in self.available:
                    if rowcol.lower() in self.cmd:
                        self._quit()
                        break
                    else:
                        rowcol = input(f'''Player {player} enter the grid num you want to place your pin. Choose from:
{self.available}\n''').strip()
            
            if not self._run:
                break
                
            self.__insert(XO, rowcol)
            self.available.remove(rowcol)
        
                
            # did anyone win?
            if self.__is_winner():
                print(f"Player {player} is the winner")
                self.player_won(player)
                break
            # Draw conditions
            elif len(self.available) == 0:
                print("\nDraw!\n")
                break

            if player == 1:
                player = 2
            else:
                player = 1
            
            if XO.lower() == 'x':
                XO = 'O'
            else:
                XO = 'X'
            
            
    def __is_winner(self):
        
        win = []

        # diagonal
        for i in range(3):
            win.append(self.grid[i][i])
        if win[0] == win[1] and win[0] == win[2]:
            return True
        
        # conjugated diag
        for i in reversed(range(3)):
            win[-(i+1)] = self.grid[i][-(i+1)]
        if win[0] == win[1] and win[0] == win[2]:
            return True
        
        # horizontal
        for i in range(3):
            win = []
            for j in range(3):
                win.append(self.grid[i][j])
            if win[0] == win[1] and win[0] == win[2]:
                return True
            else:
                continue 
                
        # vertical
        for i in range(3):
            win = []
            for j in range(3):
                win.append(self.grid[j][i])
            if win[0] == win[1] and win[0] == win[2]:
                return True
            else:
                continue 
                
    def __insert(self,XO, rowcol):
        '''insert your shape (assertion: X or O)
        and enter the number shown on the grid where you want to enter your pin'''
        assert XO.lower() in ['x','o']
        row, col = int(str(rowcol)[0])-1,int(str(rowcol)[1])-1
        self.grid[row][col] = XO.upper()
        for row in self.grid:
            print(row)
            

class Hangman(Cartrige):
    # init game mode options 
    single_mode = ['1','1v1','single']
    
    def __init__(self):
        # initialise super class runtime variable
        super().__init__()
        
        # allow player to choose game mode
        self.mode = input('Single or Multiplayer? ').strip().lower()
        if re.search('^m',self.mode) or self.mode not in self.single_mode:
            self.mode = 'Multi'
        
        # initialise game graphics
        self.a_hanged_man = ['|----------'
,'|         |  '
,'|        (X) '
,'|        /|\\'
,'|         |  '
,'|        / \\'
,'|____________']
        
        
        
        
    def __main__(self):
        
        if self.mode == 'Multi':
            # who is guessing the word? #####################data validation needed
            player = input('Which player is guessing the word? (1/2) ').strip().lower()
            if re.search('^(1|o)',player):
                player = 1
            else:
                player = 2
            
            # enter the word
            if player == 1:
                print('Player2 enter the word:')
            else:
                print('Player1 enter the word:')
            
            self.word = getpass.getpass().lower()
            self.play()
            
            if self.__win():
                self.player_won(player) 
        # if playing against computer, computer will pick a word at random    
        else:
            self.word = random.sample(words.words(),1)[0].lower()
            self.play()

        
    def play(self):
        
        # initialise game variables
        self.word_space = ['_' for _ in range(len(self.word))]
        self.lives = 7 
        self.indexed_word = {index:letter for index,letter in enumerate(self.word)}
        self.guessed = []
        
        while self._run:
            print(' '.join(self.word_space))
            
            guess = input('Enter your guess: ').strip().lower() ## assert len = 1
            
            try:
                assert len(guess) == 1
                assert type(guess) == 'str'
            except AssertionError:
                while len(guess) != 1 and type(guess) != 'str':
                    if guess in self.cmd:
                        self._quit()
                        break
                    else:
                        guess = input('Enter a letter as your guess: ').strip().lower()
                
            if guess not in self.word and guess not in self.guessed:
                self.lives -= 1
                self.print_the_man(self.lives)
                self.guessed.append(guess)
            elif guess in self.word and guess not in self.guessed:
                self.guessed.append(guess)
                for index,letter in self.indexed_word.items():
                    if letter == guess:
                        self.word_space[index] = guess
            elif guess in self.guessed:
                print('You have already guessed this')
                print('')
            else:
                print('Invalid input')
                        
            if self.__win():
                print('')
                print('##### YOU WIN! #####')
                print('')
                print('The word is', ''.join(self.word_space).upper())
                break
                
            if self.lives == 0:
                print('')
                print('##### You have been hanged #####')
                print('')
                print(f'The answer is: {self.word}')
                break
                
    
    def print_the_man(self,life):
        print(f'lives: {self.lives}')
        print('\n'.join(self.a_hanged_man[self.lives:]))
            
    def __win(self):
        if '_' in self.word_space:
            return False
        return True


class GuessingGame(Cartrige):
    single_mode = ['1','1v1','single']
    
    def __init__(self):
        
        self.guesses = 0
        self._on = True
   
                
    def __main__(self):
        Break = False
      
        while self._on: 
            # single or multiplayer?
            while True:
                mode = input('Single or Multiplayer? (single|1|one, multiplayer|multi|2) ').strip().lower()
                if re.search('^(m|t|2)',mode):
                    mode = 'Multi'
                    break
                elif re.search('^(s|o|1)',mode) or mode in self.single_mode:
                    break
                elif mode in self.cmd:
                    confirm = input('Do you want to quit? (yes/no) ')
                    if confirm in self.cmd2:
                            self._on = False
                            Break = True
                            break
                    elif confirm in self.cmd:
                        pass
                    else:
                        print('Invalid Input')
                else:
                    print('Invalid input')
            
            if Break:
                break
                
            # select number of guesses
            self.select_n()
            if self.Break:
                break
             
            
            if mode == 'Multi':
                
                # who is guessing the word?
                while True:
                    player = input('Which player is guessing the number? (1/2) ').strip().lower()
                    if re.search('^(1|o)',player):
                        player = 1
                        break
                    elif re.search('^(2|t)',player):
                        player = 2
                        break
                    elif player in self.cmd:
                        confirm = input('Do you want to quit? (yes/no) ')
                        if confirm in self.cmd2:
                            self._on = False
                            Break = True
                            break
                        elif confirm in self.cmd:
                            pass
                        else:
                            print('Invalid Input')
                    else:
                        print('Enter valid player')                    

                if Break:
                    break
                
                # select number to be guessed
                while True:
                    if player == 1:
                        print('Player2 enter the number between 0 and 50:')
                    else:
                        print('Player1 enter the number between 0 and 50:')
                        
                    self.ans = getpass.getpass()
                    try:
                        assert int(self.ans)
                        break
                    except ValueError:
                        if self.ans in self.cmd:
                            confirm = input('Do you want to quit? (yes/no) ')
                            if confirm in self.cmd2:
                                    self._on = False
                                    Break = True
                                    break
                            elif confirm in self.cmd:
                                pass
                            else:
                                print('Invalid Input')
                        else:
                            print('Enter a valid integer or quit command')
                if Break:
                    break
                
                # win/loss conditions and score amendment
                self.play(Multiplayer=True, person=player)
            
            # single player: set random number between 0 and 50
            else:
                self.ans = random.randint(0,50)
                self.play()
    
    def select_n(self):
        self.Break = False
        while True:
            self.n = input("Enter number of guesses: ")
            try:
                assert int(self.n)
                break
            except ValueError:
                if self.n in self.cmd:
                    confirm = input('Do you want to quit? (yes/no) ')
                    if confirm in self.cmd2:
                        self._on = False
                        self.Break = True
                        break
                    elif confirm in self.cmd:
                        pass
                    else:
                        print('Invalid Input')
                else:
                    print('Enter a valid integer or quit command')
                    
    def play(self, Multiplayer=False, person=None):
        Break = False
        while self.guesses <= int(self.n):
            while True:
                guess = input('Guess...: ')
                try:
                    assert int(guess)
                    break
                except ValueError:
                    if guess in self.cmd:
                        confirm = input('Do you want to quit? ')
                        if confirm in self.cmd2:
                            self._on = False
                            Break = True
                            break
                        elif confirm in self.cmd:
                            pass
                        else:
                            print('Invalid Input')
                    else:
                        print('Enter a valid integer or quit command')
                
            if Break:
                break
                
            self.guesses += 1 
            if int(guess) == int(self.ans):
                print('Thats correct!')
                self._on = False
                if Multiplayer:
                    self._is_winner(person)
                break
            elif int(guess) != int(self.ans) and self.guesses == int(self.n):
                print('Nope. You lose :(')
                self._on = False
                break
            else:
                if int(guess) > int(self.ans):
                    print('Nope. Go lower. Keep guessing...')
                elif int(guess) < int(self.ans):
                    print('Nope. Go higher. Keep guessing...')
            
            
    def _is_winner(self, person):
        self.player_won(person)
        
if __name__ == "__main__":
    Cartrige().__main__()