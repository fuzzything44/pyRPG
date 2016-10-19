import world
import display
from items import item
from objects import world_object

class chest(world_object.world_object):
    def __init__(this, posX, posY, contents = []):
        super().__init__(posX, posY, "container")
        this.attributes.update({    \
            "contents" : contents   \
          })

    def remove_items(chest):
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
            

    def collide(this, oth):
        if (oth.type == "player") and display.keyDown(ord('E')):
            this.remove_items()
    

