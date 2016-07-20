import display
from effects import flame
from objects import world_object

def fireball(player):
    player.attributes["effects"]["fireball"] = [flame.flame, world_object.no_func, 1000000]
manaCost = 25
icon = ["\\|/", "-0-", "/|\\"]
color = display.RED
