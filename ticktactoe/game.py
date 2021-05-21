from players import HumanPlayer, RandomComPlayer


class TicTacToe:
    def __init__(self):

        # use * to represent empty slot (3 x 3)
        self.board = ['*','*','*',
                      '*','*','*',
                      '*','*','*',]

        # keep track of winner
        self.currentWinner = None 
    
    def printBoard(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' |' .join(row) + ' |')

    @staticmethod
    def printBoardNum():
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + ' |' .join(row) + ' |')

    def availalbeMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == '*']
        """
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == '*':
                moves.append(i)
        return moves
        """
    def emptySquares(self):
        return '*' in self.board

    def numEmptySquares(self):
        return self.board.count('*')

    def makeMove(self, square, letter):
        # if valid move, then make the move(assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == '*':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False

    def winner(self, square, letter):
        # win = 3 in a row

        # check row
        rowIndex = square // 3
        row = self.board[rowIndex*3 : (rowIndex+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check col
        colIndex = square % 3
        col = [self.board[colIndex+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        
        # check diagonals
        # only check for even numbers
        # even numbers = possible move to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, xPlayer, oPlayer, printGame = True):
    # returns the winner of the game(letter) or None for a tie
    if printGame:
        game.printBoardNum()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (Don't have to worry about winner because it can easily breaks
    # the loop by return)
    while game.emptySquares():
        # get the move from the appropriate player
        if letter == 'O':
            square = oPlayer.getMove(game)
        else:
            square = xPlayer.getMove(game)

        # make a move 
        if game.makeMove(square, letter):
            if printGame:
                print(letter + f' makes a move to square {square}')
                game.printBoard()
                print('')

            if game.currentWinner:
                if printGame:
                    print(letter + 'wins!')
                return letter

            #after made the move, we need to alternate letters
            #letter = 'O' if letter == 'X' else 'X' #switches player
            if letter == 'O':
                letter = 'X'
            else:
                letter = 'O'
            
            # win condition
            
    if printGame:
        print('It\'s a tie!')

if __name__ == '__main__':
    xPlayer = HumanPlayer('X')
    oPlayer = RandomComPlayer('O')
    t = TicTacToe()
    play(t, xPlayer, oPlayer, printGame=True)

