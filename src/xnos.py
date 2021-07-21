from random import gammavariate
from re import X
from gameoptions import GameOptions


class XnOs(GameOptions):
        
    def __init__(self):
        # init 3x3 grid and available spaces for players to place pin
        
        self.available = []
        self.grid = [[None for _ in range(3)] for _ in range(3)]
        for row in range(1,4):
            for col in range(1,4):
                self.grid[row-1][col-1] = str(row)+str(col)
                self.available.append(str(row)+str(col))
    
    def __main__(self): 
        Break = False
        while not Break:
            self.__init__()
            print("\n#### XnOs MENU ####\n")
            print(GameOptions.score)
            # display grid
            for row in range(len(self.grid)):
                print(self.grid[row])
            print("")
            
            # start with player 1 and let them pick their pin
            player = 1
            XO = input(f'Player {player} pick your pin (X or O):').strip().lower()
            if XO in GameOptions.cmd:
                Break = GameOptions._quit()
                    
            # pin input assertion 
            try:
                assert XO in ['x','o']
            except AssertionError:
                # if player wants to quit take them to main menu (__main__)
                while XO not in ['x','o']:
                    if XO in GameOptions.cmd:
                        Break = GameOptions._quit()
                        break
                    else:
                        XO = input(f"Player {player} pick either 'X' or 'O': ")
            
            # start game
            while not Break:

                # player input location they want to place at
                rowcol = input(f'''Player {player} enter the grid num you want to place your pin: ''').strip()
                
                # input assertion
                try:
                    assert rowcol in self.available
                except AssertionError:
                    # if player wants to quit take them to main menu (__main__)
                    while rowcol not in self.available:
                        if rowcol in GameOptions.cmd:
                            Break = GameOptions._quit()
                            break
                        else:
                            rowcol = input(f'''Player {player} enter the grid num you want to place your pin. Choose from:\n{self.available}\n''').strip()

                if Break:
                    break
                    
                self.__insert(XO, rowcol)
                self.available.remove(rowcol)
            
                    
                # did anyone win?
                if self.__is_winner():
                    print(f"Player {player} is the winner")
                    self.player_won(player)
                    break
                # did they draw?
                elif len(self.available) == 0:
                    print("\nDraw!\n")
                    break
                
                # if no one drew or won then the game is still going
                # change player turn and continue
                if player == 1:
                    player = 2
                else:
                    player = 1
                
                if XO.lower() == 'x':
                    XO = 'O'
                else:
                    XO = 'X'

            Break = GameOptions.play_again(Break)
            
            
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
 

if __name__ == "__main__":
    XnOs().__main__()
    print(GameOptions.score)