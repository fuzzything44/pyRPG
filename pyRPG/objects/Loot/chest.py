import world
import display
from items import item
from objects import world_object

class chest(world_object.world_object):
    def __init__(this, posX, posY, contents = []):
        super().__init__(posX, posY, "container")
        this.attributes.update({    \
            "contents" : contents,  \
            "open"     : False      \
          })

    def update(this, delta_time):
        if world.player.X == this.X and world.player.Y == this.Y: # Colliding with player.
            # Update menu
            if this.attributes["open"]:
                if display.current_menu.update() is not None: # They chose something
                    if this.attributes["contents"] == []:     # Nothing in chest
                        return
                    #  So add to their stock or create new one.
                    if this.attributes["contents"][display.current_menu.update()] in world.player.attributes["items"]:
                        # Get their item location
                        world.player.attributes["items"][world.player.attributes["items"].index(this.attributes["contents"][display.current_menu.update()])].amount \
                                 += this.attributes["contents"][display.current_menu.update()].amount # And add how many were in the chest.
                    else: # Give them the item
                        world.player.attributes["items"].append(this.attributes["contents"][display.current_menu.update()]) # Giving the player the chest's items.
                    # Remove from chest
                    this.attributes["contents"].remove(this.attributes["contents"][display.current_menu.update()])

                    this.attributes["open"] = False # Close chest
                    display.current_menu = None
                    for i in range(5, 25): # Clear right pane
                        display.printc(50, i, ' ' * 29) 
            else:
                if display.current_menu is None: # We can actually make it
                    option_list = []
                    for item in this.attributes["contents"]:
                        option_list.append(item.name)
                    if option_list != []:
                        display.current_menu = display.menu("A Chest!", *option_list)
                    else:
                        display.current_menu = display.menu("An empty chest.", "No items to remove")
                    this.attributes["open"] = True

        elif this.attributes["open"]:           # Not colliding but opened.
            display.current_menu.clear()        # Clear right pane
            display.current_menu = None         # Remove menu
            this.attributes["open"] = False
            

