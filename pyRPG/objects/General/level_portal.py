import display
import world
from objects.General import portal

class level_portal(portal.portal):
    def __init__(this, posX, posY, newmap, locx, locy, level_req):
        super().__init__(posX, posY, newmap, locx, locy)
        this.attributes["level"] = level_req

    def collide(this, other):
        if world.player.attributes["level"] < this.attributes["level"]:
            return # Too low of level.
        return super().collide(other)
 
    def color(this):
        if world.player.attributes["level"] >= this.attributes["level"]:
            return super().color()
        return display.RED
