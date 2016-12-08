import display
from effects import regen
from objects import world_object
def FirstAid(player):
    player.attributes["effects"]["firstaid"] = regen.regen(player, 10000, "Regeneration")

manaCost = 10
icon = "\\rcX+X\n+X+\nX+X"
name = "First Aid"