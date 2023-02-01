

from types import NoneType
from pieces import ChessError, King



class Player:
    def __init__(self, player_color):
        self.player_color = player_color
    

    def get_move(self, plateau):
        print(f"Its player {self.player_color}'s turn")
        origin = input('what piece would you like to move (x, y) or (leter, number): ')
        destination = input('where would you like to put your piece: ')
        '''i = 0
        while True:
            print(i)
            i += 1
            if len(plateau.moves) != 0:
                origin = plateau.moves[-1]
                if plateau.plateau[7-int(origin[3])][int(origin[1])].color == self.color:
                    print("l'origine est valid" )
                    origin = [int(origin[1], int(origin[3]))]
                    plateau.moves = []
                    break
            plateau.Game_GUI()
            if i > 50:
                break

        while True:
            print(i)
            i += 1
            if len(plateau.moves) != 0:
                destination = plateau.moves[-1]
                if plateau.plateau[7-int(destination[3])][int(destination[1])] is None:
                    print("la des tination est valid" )
                    destination = [int(destination[1], int(destination[3]))]
                    plateau.moves = []
                    break

                if plateau.plateau[7-int(destination[3])][int(destination[1])].color != self.color:
                    print("la des tination est valid" )
                    destination = [int(destination[1], int(destination[3]))]
                    plateau.moves = []
                    break
            plateau.Game_GUI()
            if i > 50:
                break

            return (origin, destination)'''

        origin = [int(origin[0]), int(origin[2])]
        destination = [int(destination[0]), int(destination[2])]

        if origin[0] not in [0, 1, 2, 3, 4, 5, 6, 7] or origin[1] not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ChessError('invalid origine')
        if destination[0] not in [0, 1, 2, 3, 4, 5, 6, 7] or destination[1] not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ChessError('invalid destination')
        if plateau.plateau[7-origin[1]][origin[0]] == None:
            raise ChessError('There is no piece on that case')
        if plateau.plateau[7-origin[1]][origin[0]].color != self.player_color:
            raise ChessError('The pice you want to move is not yours')

        
        return (origin, destination)


    def chicken_win(self, plateau):
        '''
        return True if there is winner
        return False if the king is in check position
        return None if the king is just fine
        '''
        all_other_posi = []
        all_my_posi = []
        all_my_origin = []
        my_king = ()

        for i, line in enumerate(plateau):
            for j, case in enumerate(line):
                if case is None:
                    continue
                if isinstance(case, King) and case.color == self.player_color:
                    my_king = [(j, 7-i), case.check_moves(plateau, (j, 7-i)), case.positions]
                    continue
                if case.color != self.player_color:
                    all_other_posi += case.check_moves(plateau, (j, 7-i))
        
        for i, line in enumerate(plateau):
            for j, case in enumerate(line):
                if case is None:
                    continue
                if case.color != self.player_color or isinstance(case, King):
                    continue
                for moves in case.check_moves(plateau, (j, 7-i)):
                    if moves in all_other_posi and moves in my_king[2]:
                        all_my_posi.append(moves)
                        all_my_origin.append((j, 7-i))
        
        if my_king[0] in all_other_posi:
            if len(my_king[1]) == 0 and len(all_my_posi) == 0:
                return (True, None)
            return (False, all_my_origin, all_my_posi+my_king[1], my_king)

        return (None, None)


class Bot:
    def __init__(self, player_color):
        self.player_color = player_color
    
    def chose_origine(self, plateau):
        for i, line in enumerate(plateau):
            for j, case in enumerate(line):
                if isinstance(case, NoneType):
                    pass
                if case.color == self.player_color and len(case.check_moves(plateau, (j, i))) != 0:
                    return (j, i)
        print('no valit origine has been fond :(')

    def chose_destination(self, plateau, origine):
        moves =  plateau[7-origine[1]][origine[0]].check_moves(plateau, origine)
        print(f'these are the moves {moves}')

    def position_eval(self, plateau):
        pass