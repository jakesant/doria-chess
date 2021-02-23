class Pawn:
    """On first move, a pawn can move 2 spaces forward.
    
    On subsequent moves, a pawn can move only 1 space forward."""

    first_move = True
    can_move_back = False #Pawn can only move forward

    def __init__(self):
        self.first_move = True
        self.hor_range = 0
        self.vert_range = 2
    
    def move(self):
        if(self.first_move is True):
            self.first_move = False
        

class Rook:
    def __init__(self):
        self.hor_range = 8
        self.vert_range = 8
        
class Knight:
    """Moves in an 'L'-shaped formation"""

    def __init__(self):

class Bishop:
    def __init__(self):
        
class Queen:
    def __init__(self):
        
class King:
    def __init__(self):
        self.is_checked = False