import display
from effects import regen

def FirstAid(player):
    if "firstaid" in player.attributes["effects"]:
        player.attributes["effects"]["firstaid"].time += 10000
    else:
        player.attributes["effects"]["firstaid"] = regen.regen(player, 10000, "Regeneration")

manaCost = 10
icon = "\\fcX+X\n+X+\nX+X"
name = "First Aid"