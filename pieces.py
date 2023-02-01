





chess_piece_values = {1: ["♟", "♞", "♝", "♜", "♛", "♚"],
                      2: ["♙", "♘", "♗", "♖", "♕", "♔"],
                      }


class ChessError(Exception):

    def __str__(self):
        return F"ChessError: {self.args[0]}"
        

class Pawn:

    def __init__(self, color):
        self.value = 1
        self.color = color
        self.indice = 0
        
    
    def __str__(self):
        if self.color == 2:
            return ' ♙ '
        if self.color == 1:
            return ' ♟ '
    
    def check_moves(self, plateau, move):
        if self.color == 1:
            futur_posi = [(move[0], move[1]+1)]
            eat_other = [(move[0]+1, move[1]+1), (move[0]-1, move[1]+1)]
            if move[1] == 1:
                futur_posi.append((move[0], move[1]+2))
        else:
            futur_posi = [(move[0], move[1]-1)]
            eat_other = [(move[0]-1, move[1]-1), (move[0]+1, move[1]-1)]
            if move[1] == 6:
                futur_posi.append((move[0], move[1]-2))

        positions = []
        for posi in futur_posi:
            if posi[1] not in [0, 1, 2, 3, 4, 5, 6, 7]:
                continue
            if plateau[7-posi[1]][posi[0]] is None:
                positions.append(posi)
                continue
            if plateau[7-posi[1]][posi[0]].color == self.color:
                continue

        for posi in eat_other:
            if posi[1] not in range(8) or posi[0] not in range(8):
                continue
            if plateau[7-posi[1]][posi[0]] is None:
                continue
            if plateau[7-posi[1]][posi[0]].color == self.color:
                continue
            positions.append(posi)

        return positions


class Knight:

    def __init__(self, color):
        self.value = 3
        self.color = color
        self.indice = 1

    def __str__(self):
        if self.color == 2:
            return ' ♘ '
        if self.color == 1:
            return ' ♞ '

    def check_moves(self, plateau, move):
        """
        move = piece_position
        (x, y)
        8 valid moves
        1: y+2, x+1
        2: y+2, x-1
        3: y-2, x+1
        4: (y-2, x-1)
        5: (y+1, x+2)
        6: (y-1, x+2)
        7: (y+1, x-2)
        8: (y-1, x-2)

        as long as y+2 or x+2 are in [0, 1, 2, 3, 4, 5, 6, 7]
        """
        futur_posi = [(move[0]+2, move[1]+1),
                       (move[0]+2, move[1]-1),
                       (move[0]-2, move[1]+1),
                       (move[0]-2, move[1]-1),
                       (move[0]+1, move[1]+2),
                       (move[0]-1, move[1]+2),
                       (move[0]+1, move[1]-2),
                       (move[0]-1, move[1]-2)
                       ]
        positions = []
        for posi in futur_posi:
            if posi[0] not in range(8) or posi[1] not in range(8):
                continue
            if plateau[7-posi[1]][posi[0]] is None:
                positions.append(posi)
                continue
            if plateau[7-posi[1]][posi[0]].color == self.color:
                continue
            positions.append(posi)

        return positions

class Bishop:

    def __init__(self, color):
        self.value = 3
        self.color = color
        self.indice = 2

    def __str__(self):
        if self.color == 2:
            return ' ♗ '
        if self.color == 1:
            return ' ♝ '

    def check_moves(self, plateau, move):
        """
        find number of case available
        on the right on the left on top and under

        then fin list for the 4 diagonals
        """
        top_R = [(move[0]+1, move[1]+1),
                 (move[0]+2, move[1]+2),
                 (move[0]+3, move[1]+3),
                 (move[0]+4, move[1]+4),
                 (move[0]+5, move[1]+5),
                 (move[0]+6, move[1]+6),
                 (move[0]+7, move[1]+7)
                 ]
        top_L = [(move[0]-1, move[1]+1),
                 (move[0]-2, move[1]+2),
                 (move[0]-3, move[1]+3),
                 (move[0]-4, move[1]+4),
                 (move[0]-5, move[1]+5),
                 (move[0]-6, move[1]+6),
                 (move[0]-7, move[1]+7)
                 ]
        bot_L = [(move[0]-1, move[1]-1),
                 (move[0]-2, move[1]-2),
                 (move[0]-3, move[1]-3),
                 (move[0]-4, move[1]-4),
                 (move[0]-5, move[1]-5),
                 (move[0]-6, move[1]-6),
                 (move[0]-7, move[1]-7)
                 ]
        bot_R = [(move[0]+1, move[1]-1),
                 (move[0]+2, move[1]-2),
                 (move[0]+3, move[1]-3),
                 (move[0]+4, move[1]-4),
                 (move[0]+5, move[1]-5),
                 (move[0]+6, move[1]-6),
                 (move[0]+7, move[1]-7)
                 ]

        futur_posi = []
        for liste in [top_R, top_L, bot_L, bot_R]:
            for moves in liste:
                if moves[0] not in range(8) or moves[1] not in range(8):
                    break
                if plateau[7-moves[1]][moves[0]] is None:
                    futur_posi.append(moves)
                    continue
                if plateau[7-moves[1]][moves[0]].color == self.color:
                    break
                if plateau[7-moves[1]][moves[0]].color != self.color:
                    futur_posi.append(moves)
                    break
                else:
                    futur_posi.append(moves)
                    break

        return futur_posi


class Rook:
    def __init__(self, color):
        self.value = 5
        self.color = color
        self.indice = 3

    def __str__(self):
        if self.color == 2:
            return ' ♖ '
        if self.color == 1:
            return ' ♜ '

    def check_moves(self, plateau, move):

        top = [(move[0], move[1]+1),
               (move[0], move[1]+2),
               (move[0], move[1]+3),
               (move[0], move[1]+4),
               (move[0], move[1]+5),
               (move[0], move[1]+6),
               (move[0], move[1]+7)
               ]

        bot = [(move[0], move[1]-1),
               (move[0], move[1]-2),
               (move[0], move[1]-3),
               (move[0], move[1]-4),
               (move[0], move[1]-5),
               (move[0], move[1]-6),
               (move[0], move[1]-7)
               ]

        right = [(move[0]+1, move[1]),
                 (move[0]+2, move[1]),
                 (move[0]+3, move[1]),
                 (move[0]+4, move[1]),
                 (move[0]+5, move[1]),
                 (move[0]+6, move[1]),
                 (move[0]+7, move[1])
                 ]

        left = [(move[0]-1, move[1]),
                (move[0]-2, move[1]),
                (move[0]-3, move[1]),
                (move[0]-4, move[1]),
                (move[0]-5, move[1]),
                (move[0]-6, move[1]),
                (move[0]-7, move[1])
                ]

        positions = []
        for liste in [top, bot, right, left]:
            for posi in liste:
                if posi[0] == move[0] and posi[1] == move[1]:
                    continue
                if posi[0] not in range(8) or posi[1] not in range(8):
                    break
                if plateau[7-posi[1]][posi[0]] is None:
                    positions.append(posi)
                    continue
                if plateau[7-posi[1]][posi[0]].color == self.color:
                    break
                else:
                    positions.append(posi)
                    break

        return positions


class Queen:

    def __init__(self, color):
        self.value = 9
        self.color = color
        self.indice = 4

    def __str__(self):
        if self.color == 2:
            return ' ♕ '
        if self.color == 1:
            return ' ♛ '

    def check_moves(self, plateau, move):
        rook = Rook(self.color)
        bish = Bishop(self.color)
        futur_posi = rook.check_moves(plateau, move) + bish.check_moves(plateau, move)
        return futur_posi

class King:

    def __init__(self, color):
        self.value = 30
        self.color = color
        self.indice = 5

    def __str__(self):
        if self.color == 2:
            return ' ♔ '
        if self.color == 1:
            return ' ♚ '

    def check_moves(self, plateau, move):
        '''check for the casl
        (x, y)
        '''
        futur_posi = [(move[0]+1,move[1]+1),
                       (move[0],move[1]+1),
                       (move[0]-1,move[1]+1),
                       (move[0]-1,move[1]),
                       (move[0]-1,move[1]-1),
                       (move[0],move[1]-1),
                       (move[0]+1,move[1]-1),
                       (move[0]+1,move[1])
                       ]
        self.positions = []
        for posi in futur_posi:
            if posi[0] not in range(8) or posi[1] not in range(8):
                continue
            if plateau[7-posi[1]][posi[0]] is None:
                self.positions.append(posi)
                continue
            if plateau[7-posi[1]][posi[0]].color == self.color:
                continue
            self.positions.append(posi)

        all_other_posi = []
        for i, line in enumerate(plateau):
            for j, case in enumerate(line):
                if case is None:
                    continue
                if isinstance(case, King):
                    continue
                if case.color != self.color:
                    all_other_posi += case.check_moves(plateau, (j, 7-i))

        real_posi = []
        for posi in self.positions:
            if posi not in all_other_posi:
                real_posi.append(posi)
                continue
            if plateau[7-posi[1]][posi[0]] is None:
                continue
            if plateau[7-posi[1]][posi[0]].color != self.color:
                real_posi.append(posi)
                continue
        
        return real_posi
