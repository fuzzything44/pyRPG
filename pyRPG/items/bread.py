import display
from objects import world_object

type = "consumable"
equip = world_object.no_func
unequip = world_object.no_func

def use(own):
    try:
        own.attributes["HP"] += 5
    except:
        pass
name = "Bread"
attributes = {"icon" : ["   ", "(#)", "   "], "color": display.YELLOW, "use" : use}



