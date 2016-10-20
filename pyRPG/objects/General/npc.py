import display
import world
from objects import world_object

class npc(world_object.world_object):
    """Talks to the player.""" #TODO: add a good interface for complex dialog trees.
    def __init__(this, posX, posY, text = "Hello", options = [["Bye", world_object.no_func]], opt_params = [[]]):
        super().__init__(posX, posY, "interactable")
        this.attributes.update({        \
            "text" : text,              \
            "options" : options,        \
            "opt_params" : opt_params,  \
            "can_talk" : True           \
          })

    def update(this, delta_time):
        "Talks to player if they're standing next to it and pressed 'E'."
        if display.keyDown(ord('E')) and (this.attributes["can_talk"]):
            this.attributes["can_talk"] = False
            # If they're right next to this.
            if (((world.player.X == this.X -1) or (world.player.X == this.X + 1)) and (world.player.Y == this.Y)) or (((world.player.Y == this.Y - 1) or (world.player.Y == this.Y + 1)) and (world.player.X == this.X)):
                # Now we say hi!
                display.menu(this.attributes["text"], this.attributes["opt_params"], *this.attributes["options"])
    
        if not display.keyDown(ord('E')):
            this.attributes["can_talk"] = True
    
        if ("HP" in this.attributes) and (this.attributes["HP"] <= 0):
            world.to_del.append(this)
    
    def color(this):
        "Returns green"
        return display.GREEN
    
    def char(this):
        return 'T'
    

