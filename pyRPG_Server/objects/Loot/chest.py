import world
import display
from items import item
from objects import world_object

class chest(world_object.world_object):
    def __init__(this, posX, posY, bound_player, contents = []):
        super().__init__(posX, posY, "container")
        this.attributes.update({    \
            "contents" : contents,  \
            "open"     : False,     \
            "player"   : bound_player\
          })

    def update(this, delta_time):
        plr = this.attributes["player"]
        menu = plr.attributes["current_menu"]

        if plr.X == this.X and plr.Y == this.Y: # Colliding with player.
            # Update menu
            if this.attributes["open"]:
                if menu.update() is not None: # They chose something
                    if this.attributes["contents"] == []:     # Nothing in chest
                        return
                    #  So add to their stock or create new one.
                    if this.attributes["contents"][menu.update()] in plr.attributes["items"]:
                        # Get their item location
                        plr.attributes["items"][plr.attributes["items"].index(this.attributes["contents"][menu.update()])].amount \
                                 += this.attributes["contents"][menu.update()].amount # And add how many were in the chest.
                    else: # Give them the item
                        plr.attributes["items"].append(this.attributes["contents"][menu.update()]) # Giving the player the chest's items.
                    # Remove from chest
                    this.attributes["contents"].remove(this.attributes["contents"][menu.update()])

                    this.attributes["open"] = False # Close chest
                    display.current_menu = None
            else:
                if menu is None: # We can actually make it
                    option_list = []
                    for item in this.attributes["contents"]:
                        option_list.append(item.name)
                    if option_list != []:
                        menu = display.menu("A Chest!", *option_list)
                        this.attributes["open"] = True

                    else:
                        plr.attributes["sidebar"] += "An empty chest."

        elif this.attributes["open"]:                                           # Not colliding but opened.
            this.attributes["player"].attributes["current_menu"] = None         # Remove menu
            this.attributes["open"] = False
            

