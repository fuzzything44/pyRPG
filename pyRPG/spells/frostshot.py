import display
from effects import freeze
from objects import world_object

def frostshot(player):
    player.attributes["effects"]["frostshot"] = freeze.freeze(player)
manaCost = 15
icon = ["\\|/", "-0-", "/|\\"]
color = display.BLUE
name = "Frostshot"