import display
from objects import world_object

type = "consumable"
equip = world_object.no_func
unequip = world_object.no_func

def use(own):
    try:
        own.attributes["MP"] += 100
        if own.attributes["MP"] > own.attributes["maxMP"]:
            own.attributes["MP"] = own.attributes["maxMP"]
    except:
        pass
name = "Large Mana Potion"
attributes = {"icon" : ["   ", "69", "   "], "color": display.BLUE, "use" : use}



