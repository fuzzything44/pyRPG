import display
from effects import tough

def toughen(player):
    if "tough" not in player.attributes["effects"]:
        player.attributes["effects"]["tough"] = tough.tough(player, 15000, "Tough")
    else:
        player.attributes["effects"]["tough"].time += 15000

manaCost = 20
icon = "XXX\nXOX\nXXX"
name = "Toughen"
