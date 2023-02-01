

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
        self.blank = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\blank.png')

        b_pawn = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\Chess_pieces\Chess_pdt60.png')
        w_pawn = tk.PhotoImage(file=r'C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_plt60.png')
        b_knight = tk.PhotoImage(file=r'"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_ndt60.png"')
        w_knight = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_nlt60.png")
        b_bish = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_BB.png")
        w_bish = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_BW.png")
        b_rook = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_rdt60.png")
        w_rook = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_rlt60.png")
        b_queen = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_qdt60.png")
        w_queen = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_qlt60.png")
        b_king = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_kdt60.png")
        w_king = tk.PhotoImage(file=r"C:\Users\FamilleLemus\Desktop\vscode\Chess_pieces\Chess_klt60.png")

        self.white_list = [w_pawn, w_knight, w_bish, w_rook, w_queen, w_king]
        self.black_list = [b_pawn, b_knight, b_bish, b_rook, b_queen, b_king]
        self.widgets = {}

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
        print(f"This is the var {self.var}")
        text = event.cget('text')
        move = (int(text[1]), int(text[4]))

        if self.turn:#to chose origine

            if self.plateau[7-move[1]][move[0]] is None:
                print('the origine is invalid')
            else:
                if self.plateau[7-move[1]][move[0]].color == player.player_color:
                    print(f'the origine is valid and is{self.plateau[7-move[1]][move[0]]}')
                    print('now click where you want to place the piece')
                    self.origin = move
                    self.turn = False

        
        else:#to chose destination
            if self.plateau[7-move[1]][move[0]] is None:
                print('the destination is valid')
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
                if self.plateau[7-move[1]][move[0]].color == player.player_color:
                    self.origin = move #change the origin
                    print('origin changed')
                else:
                    self.piece = self.remove_piece(self.origin[0], self.origin[1])
                    self.place_piece(move[0], move[1], self.piece)
                    print('the destination is valid')
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

