class TicTacToe:
    def __init__(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]
        print("to make a move type in the row and column where a mark should be placed. e.g: \'0,0\' will place a mark in the upper left corner ")
        self.print_board()

    def print_board(self):
        for row in self.board:
            print("|".join(row))



t1 = TicTacToe()
