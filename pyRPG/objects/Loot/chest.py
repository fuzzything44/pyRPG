import world
import display
from items import item
from objects import world_object

def _chest_remove(chest):
    item_list = [["Exit", lambda: 0]]
    param_list = [[]]
    # Get items in proper format
    for itm in chest.attributes["contents"]:
        # Get item. item[0] is item name.
        item_list.append([itm.name, lambda: 0])
        # Add paramaters to function corresponding to choice.
        param_list.append([])

    # Menu
    opt = display.menu("A Chest!", param_list, *item_list)
    # As long as they say not to finish.
    while opt:
        # Remove items

        #  So add to their stock or create new one.
        if item_list[opt][0] in world.player.attributes["items"]:
            # Get their item location
            world.player.attributes["items"][world.player.attributes["items"].index(item_list[opt][0])].amount \
                     += chest.attributes["contents"][opt - 1].amount # And add how many were in the chest.
        else: # Give them the item
            world.player.attributes["items"].append(chest.attributes["contents"][opt - 1]) # Giving the player the chest's items.
        # Remove from chest
        chest.attributes["contents"].remove(item_list[opt][0])
        # Remove from list.
        item_list.remove(item_list[opt])
        param_list.pop()
        opt = display.menu("Item Removed", param_list, *item_list)
        
        

def update(this, delta_time):
    pass

def collide(this, oth):
    if (oth.type == "player") and display.keyDown(ord('E')):
        _chest_remove(this)

def char(this):
    return '\0'

def color(this):
    return display.WHITE

type = "container"

attributes = {\
    "contents" : [item.item("Bugged Sword", "weapon", 100, world_object.no_func, world_object.no_func, 1, { "damage" : 1, "range": 10, "disp_data" : "Please contact fuzzything44 on how you got this."})],        \
  }