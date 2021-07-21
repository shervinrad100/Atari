
class GameOptions():
    # init player commands and scores
    cmd = ['quit','q', 'break', 'exit', 'n', 'no']
    cmd2 = ['yes', 'y', 'start']
    games = ['XnOs', 'Hangman','GuessingGame', 'QuickMafs'] # add connect4
    score = {"Player1":0, "Player2":0}
    
    helpstring = '''
    Welcome to my game. The idea was to create a console Cartrige like that of Atari.
    Each cartrige has a few games. 
    You play the games with your friends and the cartrige keeps track of the scores. 
    I have tried to add as much freedom to the player as possible to if you mistype something the game wont break!
    You can quit any time using some keywords. *All inputs are case insensitive.*
    I have implemented regex to recognise the name of the game when you start on main menu.
    If you can think of new cool functionalities let me know and I'll add them in!
    Type "reset" to reset the scores
    '''

    @classmethod
    def reset_score(cls):
        cls.score = {"Player1":0, "Player2":0}
        print("scores have been reset!")
        print(cls.score)

    @classmethod
    def _quit(cls):
        confirm = input('Are you sure you want to quit? (yes/no) ')
        if confirm in cls.cmd2:
            return True
        elif confirm in cls.cmd:
            return False
        else:
            print('Invalid input')
            

    @classmethod
    def player_won(cls, player):
        cls.score["Player%i" %player] += 1

    @staticmethod
    def play_again(Break):
    # play again? 
        while not Break:
            again = input("Play again? ")
            if again in GameOptions.cmd2:
                break
            elif again in GameOptions.cmd:
                Break = GameOptions._quit()
                break
            else: print("Invalid input")
        return Break