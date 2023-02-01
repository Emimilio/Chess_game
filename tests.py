

from plateau import Plateau
from pieces import Pawn
from players import Player

#x = Plateau()
#x.Game_GUI()
#y = Player(1)
#y.get_move(x)
x = {'hello': 2, 'bye': 3}
def dico_merge(x, y):
    res = x | y
    return res
y = {'lol': 0}
z = dico_merge(x, y)
print(z)

w = dico_merge(z, y)
print(w)

