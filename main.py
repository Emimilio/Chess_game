

from graphical_interface import Plateau
from players import Player, Bot

player1 = Player(1)
player2 = Player(2)
game_board = Plateau()
players = [player1, player2]
    
print(game_board)
game_board.Game_GUI(players)
print(game_board)
