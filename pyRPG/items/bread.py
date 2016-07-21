import display
from objects import world_object

type = "consumable"
equip = world_object.no_func
unequip = world_object.no_func

def use(own):
    try:
        own.attributes["HP"] += 1
        if own.attributes["HP"] > own.attributes["maxHP"]:
            own.attributes["HP"] = own.attributes["maxHP"]
    except:
        pass
name = "Bread"
attributes = {"icon" : ["   ", "(#)", "   "], "color": display.YELLOW, "use" : use}



