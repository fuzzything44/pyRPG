import world
import display
import item
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
    opt = display.menu("Remove Items", param_list, *item_list)
    # As long as they say not to finish.
    while opt:
        # Remove items

        # Give player item. TODO: Actually give it instead of set to 1.
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
        
        

def chest_update(this, input, delta_time):
    if (input == ord('e')) & (this.attributes["canopen"]):
        _chest_remove(this)
    this.attributes["canopen"] = False

def chest_collide(this, oth):
    if oth.attributes["type"] == "player":
        this.attributes["canopen"] = True

def chest_char(this):
    if this.attributes["canopen"]:
        return 'E'
    return '\0'

def chest_col(this):
    return display.WHITE

chest_attributes = {\
    "type" : "container",   \
    "money" : 0,            \
    "contents" : [item.item("Useless Sword", 1), item.item("Useless Sword", 1)],        \
    "canopen" : False       \
    }