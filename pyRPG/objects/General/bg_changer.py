import display
import world

from objects import world_object

class bg_changer(world_object.world_object):
    # So apparently using replace = world.WORLD_NOTHING causes horrible recursive include issues.
    def __init__(this, locX, locY, classes = "warrior mage thief", replace = [display.BLACK, display.BLACK, ' ', True]):
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
    
