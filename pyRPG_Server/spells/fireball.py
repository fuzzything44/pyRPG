import display
from effects import flame
from objects import world_object

def fireball(player):
    player.attributes["effects"]["fireball"] = flame.flame(player)
manaCost = 25
icon = "\\fr\\\\|/\n-0-\n/|\\\\"
name = "Fireball"
