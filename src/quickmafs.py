from gameoptions import GameOptions
import numpy as np
import time 
import re
from threading import Timer
import concurrent.futures


class QuickMafs(GameOptions):
    
    def _gennumber(self,a_large=False, start=2):
        """
        generates four numbers:
        - two random integers between 2 and 100 with option to choose a > b and the min of range
        - two decimals with 0.01 precision between 0 and 1
        """
        a = np.random.randint(start,999)
        b = np.random.randint(start,999)
        a2 = round(np.random.random(),2)
        b2 = round(np.random.random(),2)
        if a_large:
            while b < a:
                b = np.random.randint(2,999)
        return a,b,a2,b2

    def play(self, math, ez, timerObj):
        # Subtraction
        if math == '-':
            a,b,a2,b2 = self._gennumber(True) 
        # Only generate numbers that will give positive results
            if not ez:
                a += a2
                b += b2
            
            print("\n"*5)
            startT = time.time()
            ans = input('%.2f - %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a-b,2)):
                print('Correct')
                return True
            else:
                print('Wrong')
                print("Answer:",round(a-b,2))
                return False
                
        # Summation    
        elif math == '+':
            a,b,a2,b2 = self._gennumber(False, 0)
            if not ez:
                a += a2
                b += b2
            
            print("\n"*5)
            startT = time.time()
            ans = input('%.2f + %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a+b,2)):
                print('Correct')
                return True
            else:
                print('Wrong')
                print("Answer:",round(a+b,2))
                return False
                

        # Multiplication      
        elif math == '*':
            a,b,a2,b2 = self._gennumber(False)
            if not ez:
                a += a2
                b += b2

            print("\n"*5)
            startT = time.time()
            ans = input('%.2f * %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a*b,2)):
                print('Correct')
                return True
            else:
                print('Wrong')
                print("Answer:",round(a*b,2))
                return False
                

        # Division
        elif math == '/':
            a,b,a2,b2 = self._gennumber(True)
            if not ez:
                a += a2
                b += b2
        
            print("\n"*5)
            startT = time.time()
            ans = input('%.2f / %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a/b),2) and not timerObj._is_stopped:
                print('Correct')
                return True
            else:
                print('Wrong')
                print("Answer: %.2f" %(round(a/b,2)))
                return False
                
    def _help(self):
        print('The aim of the game is for you to practice your mental maths skills.',
            'You can choose one of the four main operations to practice.',
            'Two random numbers will be generated and you will need to enter your answer.')
        print('The pass rate is 70\%. If you score higher', 
        'it would count as a win towards your score on the cartridge')    
        print('to quit type:')
        print(self.cmd)

    def __main__(self):
        Break = False
        def _print_score(question,score):
            try:
                print(f"Score: {score}/{question} ({round(score/question*100,2)}%)")
            except ZeroDivisionError:
                print("Score: 0/0 (0.0%)")
        
        question = 0
        score = 0
        timer = 5
        while not Break:
            # Main Menu 
            print("For the score, please enter: 'score'")
            print("For help, enter: 'help'")
            Break = False
            
            # which player is playing
            while not Break:
                player = input('Which player is playing? (1/2) ').strip().lower()
                if re.search('^(1|o)',player):
                    player = 1
                    break
                elif re.search('^(2|t)',player):
                    player = 2
                    break
                elif player in self.cmd:
                        Break = GameOptions._quit()
                        break
                
                elif re.search('^he',player):
                    self._help()

                elif re.search('^sc',player):
                    _print_score(question,score)

                else:
                    print('Enter valid player')    

                if Break:
                    break
            
            # choose difficulty
            while not Break:
                ez = input("choose difficulty: Easy (True), or hard (False)? ").strip().lower()
                if ez in self.cmd:
                        Break = GameOptions._quit()
                        break

                elif re.search('^he',ez):
                    self._help()

                elif re.search('^sc',ez):
                    _print_score(question,score)

                elif ["He chose hard" for letter in list(ez) if letter in ["f","h"]]:
                    ez = False
                    print("\nHard\n")
                    break
                else:
                    ez = True
                    print("\nEasy\n")
                    break
                
                if Break:
                    break
            
            
            # choose game style
            while not Break:
                math = input('Please choose from: +, -, *, / \n').strip().lower()

                if math in GameOptions.cmd:
                    Break = GameOptions._quit()

                elif re.search('^he',math):
                    self._help()

                elif re.search('^sc',math):
                    _print_score(question,score)

                elif math == "timer":
                    timer = int(input("Enter timer length as an integer: ").strip())
                    print(f"timer set for {timer} seconds")

                elif math in ["+","*","-","/"]:
                    try:
                        grade = round(score/question*100,2)
                    except ZeroDivisionError:
                        grade = 0
                    question += 1
                    
                    stopwatch = Timer(timer, print, ["too slow"])
                    stopwatch.start()
                    ans = self.play(math, ez, stopwatch)
                    stopwatch.cancel()
                    # if too slow then the entered number should not be accepted
                
                    if ans is True:
                        score += 1
                
                else:
                    print('Invalid input')

            if grade >= 70 and question >= 5:
                GameOptions.player_won(player)      


if __name__ == "__main__":
    QuickMafs().__main__()
    print(GameOptions.score)