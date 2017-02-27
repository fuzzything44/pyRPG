import display
from effects import freeze

def frostshot(player):
    player.attributes["effects"]["frostshot"] = freeze.freeze(player)
manaCost = 15
icon = "\\fb\\\\|/\n-0-\n/|\\\\"
name = "Frostshot"