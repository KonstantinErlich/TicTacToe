class TicTacToe:
    def __init__(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]

        self.player = 0
        self.mark = "X"

        print("to make a move type in the row and column where a mark should be placed. e.g: \'0,2\' will place a mark in the upper right corner ")
        self.print_board()
        self.move()
        self.print_board()



    def print_board(self):
        for row in self.board:
            print("|".join(row))

    def current_player(self):
        # player toggles between 0 and 1
        self.player = 1 if self.player == 0 else 0
        self.mark = "X" if self.player == 0 else "O"

    def move(self):
        while True:
         input_str = input(f"where to place \'{self.mark}\'? \n")
         try:
             # Split the input string by comma and convert to integers
             i, j = map(int, input_str.split(','))

             # Check if the indices are within the valid range (0 to 2)
             if 0 <= i <= 2 and 0 <= j <= 2:
                 self.board[i][j] = self.mark  # Or any other value you want to use
                 self.current_player()
                 break
             else:
                 print("Invalid input: Indices must be between 0 and 2.")
         except (ValueError, IndexError):
             print("Invalid input: Please enter the input in 'i,j' format with i, j between 0 and 2.")



t1 = TicTacToe()
