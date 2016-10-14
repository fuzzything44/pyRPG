import display
import world

from objects import world_object

class bg_changer(world_object.world_object):
    def __init__(this, locX, locY, classes = "warrior mage thief", replace = world.WORLD_NOTHING):
        super().__init__(locX, locY, "special")
        this.attributes.update({\
            "class" : classes,  \
            "replace" : replace \
          })

    def update(this, delta_time):
        plr_class = world.player.attributes["class"]    # Get player class
        if plr_class in this.attributes["class"]:       # If they are an acceptable class...
            world.map[this.X][this.Y] = this.attributes["replace"] #... then change the world tile this is on to something else.
        world.to_del.append(this) # Delete this. It's job is done.
    
