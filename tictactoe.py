class TicTacToe:
    def __init__(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]

        self.player = 0
        self.mark = "X"
        self.won = 0

        print("to make a move type in the row and column where a mark should be placed. e.g: \'0,2\' will place a mark in the upper right corner ")
        self.print_board()
        while self.won == 0:
            self.move()
            self.print_board()
            self.check_winner()
        self.announce_winner()



    def print_board(self):
        for row in self.board:
            print("|".join(row))
    def announce_winner(self):
        if self.player == 0:
            print("Player 2 wins!")
        if self.player == 1:
            print("Player 1 wins!")

    def current_player(self):
        # player toggles between 0 and 1
        self.player = 1 if self.player == 0 else 0
        self.mark = "X" if self.player == 0 else "O"

    def check_winner(self):
        #check if any row is filled with same mark
        for i in range(3):
            row = self.board[i]
            first_mark = row[i]
            if first_mark != "-" and all(mark == first_mark for mark in row):
                self.won = 1
        # check if any row is filled with same mark
        for i in range(3):
            column = [self.board[row][i] for row in range(3)]
            first_mark = column[0]
            if first_mark != "-" and all(mark == first_mark for mark in column):
                self.won = 1

        #check if either diagonals are filled with same mark
        first_mark = self.board[0][0]
        if first_mark != "-" and all(self.board[i][i] == first_mark for i in range(3)):
            self.won = 1

        first_mark = self.board[0][2]
        if first_mark != "-" and all(self.board[i][2-i] == first_mark for i in range(3)):
            self.won = 1

    def move(self):
        while True:
         input_str = input(f"where to place \'{self.mark}\'? \n")
         try:
             # Split the input string by comma and convert to integers
             i, j = map(int, input_str.split(','))

             # Check if the indices are within the valid range (0 to 2)
             if 0 <= i <= 2 and 0 <= j <= 2:
                 if self.board[i][j] != "-":
                     print("invalid input, there is already a mark there.")
                 else:
                    self.board[i][j] = self.mark  
                    self.current_player()
                    break
             else:
                 print("Invalid input: Indices must be between 0 and 2.")
         except (ValueError, IndexError):
             print("Invalid input: Please enter the input in 'i,j' format with i, j between 0 and 2.")

t1 = TicTacToe()
