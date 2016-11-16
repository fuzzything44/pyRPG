import display
import world
from objects import world_object


class npc(world_object.world_object):
    """Talks to the player.""" #TODO: add a good interface for complex dialog trees.
    def __init__(this, posX, posY, text = "Hello", *options):
        super().__init__(posX, posY, "interactable")
        this.attributes.update({        \
            "text" : text,              \
            "options" : options,        \
            "can_talk" : True           \
          })

    def update(this, delta_time):
        "Talks to player if they're standing next to it."
        if ("HP" in this.attributes) and (this.attributes["HP"] <= 0):
            world.to_del.append(this)
    
    def color(this):
        "Returns green"
        return display.GREEN
    
    def char(this):
        return 'T'
    

