
from pieces import Pawn, Knight, Bishop, Rook, Queen, King, ChessError
import tkinter as tk


class Plateau:
    def __init__(self):
        self.plateau = [[Rook(2), Knight(2), Bishop(2), Queen(2), King(2), Bishop(2), Knight(2), Rook(2)],
                        [Pawn(2), Pawn(2), Pawn(2), Pawn(2), Pawn(2), Pawn(2), Pawn(2), Pawn(2)],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
                        [Rook(1), Knight(1), Bishop(1), Queen(1), King(1), Bishop(1), Knight(1), Rook(1)]
                        ]

        self.root = tk.Tk()
        self.blank = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\blank.png')

        b_pawn = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_pdt60.png')
        w_pawn = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_plt60.png')
        b_knight = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_ndt60.png')
        w_knight = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_nlt60.png')
        b_bish = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_BB.png')
        w_bish = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_BW.png')
        b_rook = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_rdt60.png')
        w_rook = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_rlt60.png')
        b_queen = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_qdt60.png')
        w_queen = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_qlt60.png')
        b_king = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_kdt60.png')
        w_king = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_klt60.png')

        self.white_list = [w_pawn, w_knight, w_bish, w_rook, w_queen, w_king]
        self.black_list = [b_pawn, b_knight, b_bish, b_rook, b_queen, b_king]
        self.widgets = {}
        self.posi = []
        self.turn = True
        self.piece = None
        self.var = 0
        self.origin = []

    def __str__(self):
        print('')
        plato = ''
        indice = 8
        for line in self.plateau:
            indice -= 1
            sortie = f"{indice} |"
            for case in line:
                if case is None:
                    sortie += '   '
                else:
                    sortie += case.__str__()
                sortie += '|'

            plato += f" {sortie}\n   ---------------------------------\n"
        plato += '     a   b   c   d   e   f   g   h\n'
        return plato

    def remove_piece(self, x, y):
        
        piece = self.plateau[7-y][x]
        self.plateau[7-y][x] = None
        return piece
    
    def place_piece(self,x ,y , piece):
        if self.plateau[7-y][x] == None:
            self.plateau[7-y][x] = piece
        else:
            if self.plateau[7-y][x].color == piece.color:
                raise ChessError('You are trying to eat one of your own pieces')
            self.plateau[7-y][x] = piece
    
    def Game_GUI(self, players):
    
        
        self.root.title('grid()')
        self.root.geometry('570x570')
        self.root.config(bg='black')

        cadre = tk.Frame(self.root)
        cadre.grid(padx=20, pady=20)

        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    color = 'white'
                else:
                    color = 'brown'
                if self.plateau[7-i][j] is None:
                    bt = tk.Button(cadre, bg=color, text=f'{j,7-i}', image=self.blank)
                    bt.config(command=lambda bt=bt: self.showGrid(bt, players))
                    bt.grid(row=i, column=j)
                    self.widgets[(j, 7-i)] = bt

                else:
                    if self.plateau[7-i][j].color == 1:
                        bt = tk.Button(cadre, bg=color, text=f'{j,7-i}', image=self.black_list[self.plateau[7-i][j].indice])
                        bt.config(command=lambda bt=bt: self.showGrid(bt, players))
                        bt.grid(row=i, column=j)
                        self.widgets[(j, 7-i)] = bt
                    else:
                        bt = tk.Button(cadre, bg=color, text=f'{j,7-i}', image=self.white_list[self.plateau[7-i][j].indice])
                        bt.config(command=lambda bt=bt: self.showGrid(bt, players))
                        bt.grid(row=i, column=j)
                        self.widgets[(j, 7-i)] = bt
                        
        self.root.mainloop()

    def showGrid(self, event, players):
        player = players[self.var]

        print(f"its player {player.player_color}'s turn")
        text = event.cget('text')
        move = (int(text[1]), int(text[4]))
        win_check = player.chicken_win(self.plateau)
        print(win_check)
        if win_check[0] is False:
            self.posi = win_check[2]
        
        elif win_check[0] is True:
            raise ChessError(f"****PLAYER {player.player_color} WIN'S******")

        if self.turn:#to chose origine

            if self.plateau[7-move[1]][move[0]] is None:
                print('the origine is invalid')
            
            elif win_check[0] is False:
                if move in win_check[1]:
                    self.origin = move
                    self.turn = False
                    i = 0
                    for j, key in enumerate(self.widgets.keys()):
                        if j%8 == 0 and j != 0:
                            i += 1
                        if key in self.posi:
                            self.widgets[key].config(bg='green')
                        elif (j+i)%2 == 0:
                            self.widgets[key].config(bg='white')
                        else:
                            self.widgets[key].config(bg='brown')
                elif move == win_check[3][0] and len(win_check[3][2]) != 0:
                    self.origin = move
                    self.turn = False
                    self.posi = win_check[3][1]
                    i = 0
                    for j, key in enumerate(self.widgets.keys()):
                        if j%8 == 0 and j != 0:
                            i += 1
                        if key in self.posi:
                            self.widgets[key].config(bg='green')
                        elif (j+i)%2 == 0:
                            self.widgets[key].config(bg='white')
                        else:
                            self.widgets[key].config(bg='brown')
                else:
                    print('invalide origine the king will die')

            else:
                if self.plateau[7-move[1]][move[0]].color == player.player_color:
                    print(f'the origine is valid and is{self.plateau[7-move[1]][move[0]]}')
                    self.posi = self.plateau[7-move[1]][move[0]].check_moves(self.plateau, move)
                    if len(self.posi) == 0:
                        print('no futur possible moves')
                    else:
                        print(f'u can move at {self.posi}')
                    self.origin = move
                    self.turn = False
                    i = 0
                    for j, key in enumerate(self.widgets.keys()):
                        if j%8 == 0 and j != 0:
                            i += 1
                        if key in self.posi:
                            self.widgets[key].config(bg='green')
                        elif (j+i)%2 == 0:
                            self.widgets[key].config(bg='white')
                        else:
                            self.widgets[key].config(bg='brown')
        
        else:#to chose destination
            if self.plateau[7-move[1]][move[0]] is None:
                if move in self.posi:
                    self.piece = self.remove_piece(self.origin[0], self.origin[1])
                    self.place_piece(move[0], move[1], self.piece)
                    self.widgets[self.origin].config(image=self.blank)
                    if self.piece.color == 2:
                        event.config(image=self.black_list[self.piece.indice])
                    else:
                        event.config(image=self.white_list[self.piece.indice])
                    
                    self.piece = None
                    self.turn = True
                    if self.var == 0:
                        self.var = 1
                    else:
                        self.var = 0
                else:
                    print('destination not valid')

            else:
                if self.plateau[7-move[1]][move[0]].color == player.player_color and win_check[0] is None:
                    self.origin = move #change the origin
                    self.posi = self.plateau[7-move[1]][move[0]].check_moves(self.plateau, move)
                    if len(self.posi) == 0:
                        print('no futur possible moves')
                    else:
                        print(f'u can move at {self.posi}')
                    i = 0
                    for j, key in enumerate(self.widgets.keys()):
                        if j%8 == 0 and j != 0:
                            i += 1
                        if key in self.posi:
                            self.widgets[key].config(bg='green')
                        elif (j+i)%2 == 0:
                            self.widgets[key].config(bg='white')
                        else:
                            self.widgets[key].config(bg='brown')

                elif self.plateau[7-move[1]][move[0]].color == player.player_color and move in win_check[1]:
                    self.origin = move
                    i = 0
                    for j, key in enumerate(self.widgets.keys()):
                        if j%8 == 0 and j != 0:
                            i += 1
                        if key in self.posi:
                            self.widgets[key].config(bg='green')
                        elif (j+i)%2 == 0:
                            self.widgets[key].config(bg='white')
                        else:
                            self.widgets[key].config(bg='brown')

                else:
                    if move in self.posi:
                        self.piece = self.remove_piece(self.origin[0], self.origin[1])
                        self.place_piece(move[0], move[1], self.piece)
                        self.widgets[self.origin].config(image=self.blank)
                        if self.piece.color == 2:
                            event.config(image=self.black_list[self.piece.indice])
                        else:
                            event.config(image=self.white_list[self.piece.indice])
                        self.turn = True
                        self.piece = None
                        if self.var == 0:
                            self.var = 1
                        else:
                            self.var = 0
                    else:
                        print('destination not valid')
        '''if self.turn is False:
            org = players[1].chose_origine(self.plateau)
            print(f'this is org {org}')
            dest = players[1].chose_destination(self.plateau, org)
            self.piece = self.remove_piece(org[0], org[1])
            self.place_piece(dest[0], dest[1], self.piece)'''
        
