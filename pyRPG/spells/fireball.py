import display
from effects import flame

def fireball(player):
    player.attributes["effects"]["fireball"] = [flame.flame, lambda x: 0, 3000]