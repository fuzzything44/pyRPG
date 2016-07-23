import display
from effects import regen
from objects import world_object
def FirstAid(player):
    player.attributes["effects"]["FirstAid"] = [regen.regen2, world_object.no_func, 15000]

manaCost = 10
icon = ["X+X", "+X+", "X+X"]
color = display.CYAN
name = "First Aid"