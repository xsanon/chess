import board
import piece

class Chess():
    """
    A class to represent the game of chess.
    
    ...

    Attributes:
    -----------
    board : Board
        represents the chess board of the game
    """

    def __init__(self):
        self.board = board.Board()

def translate(s):
    """
    Translates traditional board coordinates of chess into list indices
    """
    try:
        row = int(s[0])
        col = s[1]
        if row < 1 or row > 8:
            print(s[0] + "is not in the range from 1 - 8")
            return None
        if col < 'a' or col > 'h':
            print(s[1] + "is not in the range from a - h")
            return None
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return (8 - row, dict[col])
    except:
        print(s + "is not in the format '[number][letter]'")
        return None


def promotion(board, pos):
    pawn = None
    while pawn == None:
        promote = input("Promote pawn to [Q, R, N, B, P(or nothing)]: ")
        if promote not in ['Q', 'R', 'N', 'B', 'P', '']:
            print("Not a valid promotion piece")
        else:
            if promote == 'Q':
                pawn = piece.Queen(True)
            elif promote == 'R':
                pawn = piece.Rook(True)
            elif promote == 'N':
                pawn = piece.Knight(True)
            elif promote == 'B':
                pawn = piece.Bishop(True)
            elif promote == 'P' or promote == '': 
                pawn = piece.Pawn(True)
    board[pos[0]][pos[1]] = pawn 


if __name__ == "__main__":
    chess = Chess()
    chess.board.print_board()

    while True:
        start = input("From: ")
        to = input("To: ")
        
        start = translate(start)
        to = translate(to)

        if start == None or to == None:
            continue

        chess.board.move(start, to)

        # check for promotion pawns
        i = 0
        while i < 8:
            if not chess.board.turn and chess.board.board[0][i] != None and \
                chess.board.board[0][i].name == 'P':
                promotion(chess.board.board, (0, i))
                break
            elif chess.board.turn and chess.board.board[7][i] != None and \
                chess.board.board[7][i].name == 'P':
                promotion(chess.board.board, (7, i))
                break
            i += 1

        chess.board.print_board()
