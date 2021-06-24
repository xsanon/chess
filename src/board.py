import piece

class Board():
    def __init__(self):
        self.board = []
        self.turn = True

        self.white_ghost_piece = None
        self.black_ghost_piece = None

        for i in range(8):
            self.board.append([None] * 8)
        # White
        self.board[7][0] = piece.Rook(True)
        self.board[7][1] = piece.Knight(True)
        self.board[7][2] = piece.Bishop(True)
        self.board[7][3] = piece.Queen(True)
        self.board[7][4] = piece.King(True)
        self.board[7][5] = piece.Bishop(True)
        self.board[7][6] = piece.Knight(True)
        self.board[7][7] = piece.Rook(True)

        for i in range(8):
            self.board[6][i] = piece.Pawn(True)

        # Black
        self.board[0][0] = piece.Rook(False)
        self.board[0][1] = piece.Knight(False)
        self.board[0][2] = piece.Bishop(False)
        self.board[0][3] = piece.Queen(False)
        self.board[0][4] = piece.King(False)
        self.board[0][5] = piece.Bishop(False)
        self.board[0][6] = piece.Knight(False)
        self.board[0][7] = piece.Rook(False)

        for i in range(8):
            self.board[1][i] = piece.Pawn(False)

    def print_board(self):
        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)
        for i in range(len(self.board)):
            tmp_str = "|"
            for j in self.board[i]:
                if j == None:
                    tmp_str += "   |"
                elif len(j.name) == 2:
                    tmp_str += (" " + str(j) + "|")
                else:
                    tmp_str += (" " + str(j) + " |")
            print(tmp_str)
        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)

    def move(self, start, to):
        if self.board[start[0]][start[1]] == None:
            print("There is no piece to move at the start place")
            return
        target_piece = self.board[start[0]][start[1]]
        if self.turn != target_piece.color:
            print("That's not your piece to move")
            return
        if target_piece.is_valid_move(self, start, to):
            if self.board[to[0]][to[1]]:
                print(str(self.board[to[0]][to[1]]) + " taken.")
                if self.board[to[0]][to[1]].name == "GP":
                    if self.turn:
                        self.board[
                            self.black_ghost_piece[0] + 1
                        ][
                            self.black_ghost_piece[1]
                        ] = None
                        self.black_ghost_piece = None
                    else:
                        self.board[self.white_ghost_piece[0] - 1][self.black_ghost_piece[1]] = None
                        self.white_ghost_piece = None
            self.board[to[0]][to[1]] = target_piece
            self.board[start[0]][start[1]] = None
            print(str(target_piece) + " moved.")
            if self.turn and self.black_ghost_piece:
                self.board[self.black_ghost_piece[0]][self.black_ghost_piece[1]] = None
            elif not self.turn and self.white_ghost_piece:
                self.board[self.white_ghost_piece[0]][self.white_ghost_piece[1]] = None
            self.turn = not self.turn
