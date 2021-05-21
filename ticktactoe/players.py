import math
import random

class Player:
    def __init__(self, letter):
        # letter = x or o
        self.letter = letter
    
    def getMove(self, game):
        pass

class RandomComPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        # get a random valid spot for the next move
        square = random.choice(game.availalbeMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # we are going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.availalbeMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid square. Try again.')

        return val
        
        

        