import display
import world
from objects.General import portal

class level_portal(portal.portal):
    """Portal only usable if they're a high enough level."""
    def __init__(this, posX, posY, newmap, locx, locy, level_req):
        super().__init__(posX, posY, newmap, locx, locy)
        this.attributes["level"] = level_req

    def collide(this, other):
        "Possibly changes current map if collides with player."
        if other.type == "player":
            if other.attributes["level"] >= this.attributes["level"]:
                return super().collide(other)
            else:
                other.attributes["sidebar"] += "Portal requires level " + str(this.attributes["level"]) + '\n'
 
