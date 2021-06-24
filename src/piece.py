blocked_path = "There's a piece in the path."
incorrect_path = "This piece does not move in this pattern."

class Piece():
    def __init__(self, color):
        self.name = ""
        self.color = color

    def is_valid_move(self, board, start, to):
        """
        Determines if moving this piece start [start] to [to] is a valid move.

        Precondition: [start] and [to] are valid coordinates on the board.board
        """
        return False

    def is_white(self):
        return self.color

    def __str__(self):
        if self.color:
            return self.name
        else:
            return '\033[94m' + self.name + '\033[0m'

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "R"

    def is_valid_move(self, board, start, to):
        if start[0] == to[0]:
            smaller_y = start[1] if start[1] < to[1] else to[1]
            bigger_y = start[1] if start[1] > to[1] else to[1]

            for i in range(smaller_y + 1, bigger_y):
                if board.board[start[0]][i] != None:
                    print(blocked_path)
                    return False
            return True
        if start[1] == to[1]:
            smaller_x = start[0] if start[0] < to[0] else to[0]
            bigger_x = start[0] if start[0] > to[0] else to[0]

            for i in range(smaller_x + 1, bigger_x):
                if board.board[i][start[1]] != None:
                    print(blocked_path)
                    return False
            return True
        print(incorrect_path)
        return False

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"

    def is_valid_move(self, board, start, to):
        if abs(start[0] - to[0]) == 2 and abs(start[1] - to[1]) == 1:
            return True
        if abs(start[0] - to[0]) == 1 and abs(start[1] - to[1]) == 2:
            return True
        print(incorrect_path)
        return False

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"

    def is_valid_move(self, board, start, to):
        if abs(start[0] - to[0]) != abs(start[1] - to[1]):
            print(incorrect_path)
            return False

        x_pos =  1 if to[0] - start[0] > 0 else -1
        y_pos = 1 if to[1] - start[1] > 0 else -1

        i = start[0] + x_pos
        j = start[1] + y_pos
        while i <= to[0]:
            if board.board[i][j] != None:
                print(blocked_path)
                print("At: " + str((i, j)))
                return False
            i += x_pos
            j += y_pos
        return True

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"

    def is_valid_move(self, board, start, to):
        # diagonal
        if abs(start[0] - to[0]) == abs(start[1] - to[1]):
            x_pos =  1 if to[0] - start[0] > 0 else -1
            y_pos = 1 if to[1] - start[1] > 0 else -1

            i = start[0] + x_pos
            j = start[1] + y_pos
            while i <= to[0]:
                if board.board[i][j] != None:
                    print(blocked_path)
                    print("At: " + str((i, j)))
                    return False
                i += x_pos
                j += y_pos
            return True

        # up/down
        elif start[0] == to[0] or start[1] == to[1]:
            if start[0] == to[0]:
                smaller_y = start[1] if start[1] < to[1] else to[1]
                bigger_y = start[1] if start[1] > to[1] else to[1]

                for i in range(smaller_y + 1, bigger_y):
                    if board.board[start[0]][i] != None:
                        print(blocked_path)
                        return False
                return True
            else:
                smaller_x = start[0] if start[0] < to[0] else to[0]
                bigger_x = start[0] if start[0] > to[0] else to[0]

                for i in range(smaller_x + 1, bigger_x):
                    if board.board[i][start[1]] != None:
                        print(blocked_path)
                        return False
                return True
        print(incorrect_path)
        return False

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "K"

    def is_valid_move(self, board, start, to):
        if abs(start[0] - to[0]) == 1 or start[0] - to[0] == 0:
            if start[1] - to[1] == 0 or abs(start[1] - to[1]) == 1:
                return True
        print(incorrect_path)
        return False

class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "GP"

    def is_valid_move(self, board, start, to):
        return False

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"
        self.first_move = True

    def is_valid_move(self, board, start, to):
        if self.color:
            if start[0] == to[0] + 1 and (start[1] == to[1] + 1 or start[1] == to[1] - 1):
                if board.board[to[0]][to[1]] != None:
                    self.first_move = False
                    return True
                print("Cannot move diagonally unless taking.")
                return False
            if start[1] == to[1]:
                if (start[0] - to[0] == 2 and self.first_move) or (start[0] - to[0] == 1):
                    for i in range(start[0] - 1, to[0] - 1, -1):
                        if board.board[i][start[1]] != None:
                            print(blocked_path)
                            return False
                    # insert a GhostPawn
                    if start[0] - to[0] == 2:
                        board.board[start[0] - 1][start[1]] = GhostPawn(self.color)
                        board.white_ghost_piece = (start[0] - 1, start[1])
                    self.first_move = False
                    return True
                print(blocked_path + " or " + "Cannot move forward twice if not first move.")
                return False
            print(incorrect_path)
            return False
        else:
            if start[0] == to[0] - 1 and (start[1] == to[1] - 1 or start[1] == to[1] + 1):
                if board.board[to[0]][to[1]] != None:
                    self.first_move = False
                    return True
                print(blocked_path)
                return False
            if start[1] == to[1]:
                if (to[0] - start[0] == 2 and self.first_move) or (to[0] - start[0] == 1):
                    for i in range(start[0] + 1, to[0] + 1):
                        if board.board[i][start[1]] != None:
                            print(blocked_path)
                            return False
                    # insert a GhostPawn
                    if to[0] - start[0] == 2:
                        board.board[start[0] + 1][start[1]] = GhostPawn(self.color)
                        board.black_ghost_piece = (start[0] + 1, start[1])
                    self.first_move = False
                    return True
                print(blocked_path + " or " + "Cannot move forward twice if not first move.")
                return False
            print(incorrect_path)
            return False
