class Piece:
    """Superclass of piece. Other pieces are subclasses
    
    inheriting this"""

    def __init__(self, can_move_back=True, movement_range):
        self.first_move = True
        self.can_move_back = can_move_back
        self.movement_range = movement_range

class Pawn(Piece):
    """On first move, a pawn can move 2 spaces forward.
    
    On subsequent moves, a pawn can move only 1 space forward."""

    first_move = True
    can_move_back = False #Pawn can only move forward

    def __init__(self):
        super().__init__()
        self.first_move = True
        self.hor_range = 0
        self.vert_range = 2
    
    def move(self):
        if(self.first_move is True):
            self.first_move = False
        

class Rook(Piece):
    """Moves any space directly horizontally or vertically"""

    def __init__(self):
        super().__init__(can_move_back = False, movement_range = [][])
        self.hor_range = 8
        self.vert_range = 8
        
class Knight(Piece):
    """Moves in an 'L'-shaped formation"""

    def __init__(self):
        super().__init__()

class Bishop(Piece):
    """Moves diagonally"""

    def __init__(self):
        super().__init__()

class Queen(Piece):
    def __init__(self):
        super().__init__()

class King(Piece):
    def __init__(self):
        super().__init__()
        self.is_checked = False