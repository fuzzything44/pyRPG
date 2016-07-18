import display
from effects import flame

def fireblade(player):
    player.attributes["effects"]["fireblade"]=[flame.flame, lambda x: 0, 10000]