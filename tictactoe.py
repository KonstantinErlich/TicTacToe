class TicTacToe:
    def __init__(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]

        self.player = 0
        self.mark = "X"
        self.won = 0

        print(
            "to make a move type in the row and column where a mark should be placed. e.g: \'0,2\' will place a mark in the upper right corner ")
        self.print_board()
        while self.won == 0:
            if self.won == 2:
                break
            if self.player == 0:
                self.player_move()
            else:
                self.comp_move()
                self.print_board()
            self.check_winner()
            self.check_tie()
        self.announce_winner()

    def print_board(self):
        for row in self.board:
            print("|".join(row))

    def announce_winner(self):
        if self.won == 2:
            print("Tie")
        else:
            if self.player == 0:
                print("Player 2 wins!")
            if self.player == 1:
                print("Player 1 wins!")

    def current_player(self):
        # player toggles between 0 and 1
        self.player = 1 if self.player == 0 else 0
        self.mark = "X" if self.player == 0 else "O"

    def check_winner(self):
        # check if any row is filled with same mark
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

        # check if either diagonals are filled with same mark
        first_mark = self.board[0][0]
        if first_mark != "-" and all(self.board[i][i] == first_mark for i in range(3)):
            self.won = 1

        first_mark = self.board[0][2]
        if first_mark != "-" and all(self.board[i][2 - i] == first_mark for i in range(3)):
            self.won = 1

    def check_tie(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    count += 1
        if count == 0 and self.won == 0:
            self.won = 2

    def player_move(self):
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

    def is_moves_left(self):
        for row in self.board:
            if "-" in row:
                return True
        return False

    def evaluate(self):
        # Check rows for victory
        for row in self.board:
            if row[0] == row[1] == row[2] != "-":
                return 10 if row[0] == 'O' else -10

        # Check columns for victory
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "-":
                return 10 if self.board[0][col] == 'O' else -10

        # Check diagonals for victory
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "-":
            return 10 if self.board[0][0] == 'O' else -10
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "-":
            return 10 if self.board[0][2] == 'O' else -10

        # If no one has won
        return 0

    def minimax(self, depth, is_maximizing):
        score = self.evaluate()

        # If the computer has won
        if score == 10:
            return score - depth

        # If the opponent has won
        if score == -10:
            return score + depth

        # If there are no more moves and no winner
        if not self.is_moves_left():
            return 0

        # If it's the computer's move (maximizing player)
        if is_maximizing:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "-":
                        self.board[i][j] = 'O'
                        best = max(best, self.minimax(depth + 1, not is_maximizing))
                        self.board[i][j] = "-"
            return best

        # If it's the opponent's move (minimizing player)
        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "-":
                        self.board[i][j] = 'X'
                        best = min(best, self.minimax(depth + 1, not is_maximizing))
                        self.board[i][j] = "-"
            return best

    def comp_move(self):
        best_val = -1000
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    self.board[i][j] = 'O'
                    move_val = self.minimax(0, False)
                    self.board[i][j] = "-"

                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val

        while True:
            input_str = f"{best_move[0]},{best_move[1]}"
            i, j = map(int, input_str.split(','))
            self.board[i][j] = self.mark
            self.current_player()
            break


t1 = TicTacToe()
