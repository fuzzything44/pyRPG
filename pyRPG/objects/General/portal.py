import display
import world
from objects import world_object

class portal(world_object.world_object):
    def __init__(this, posX, posY, newmap, locx, locy):
        super().__init__(posX, posY, "portal")
        this.attributes.update({      \
            "newmap" : newmap,  \
            "locx" : locx,      \
            "locy" : locy,      \
            "used" : False      \
        })

    def collide(this, other):
        if other.type == "player":
            world.load(this.attributes["newmap"])
            world.objects = [world.player] + world.objects
    
            world.player.X = this.attributes["locx"]
            world.player.Y = this.attributes["locy"]
            this.attributes["used"] = True
            # Print world out
            world.dispworld()
            return True

    def char(this):
        if not this.attributes["used"]:
            return 'O'
        return '\0'

    def color(this):
        return display.BLUE

 


