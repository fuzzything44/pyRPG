import display
import world
from objects import world_object

class timed_portal(world_object.world_object):
    """Brings player into a new map"""
    def __init__(this, posX, posY, newmap, locx, locy, time):
        """Parameters:
            posX: The X position of the portal.
            poxY: The Y position of the portal.
            newmap: The new map to bring the player to.
            locx: The x location to bring the player to.
            locy: The y location to bring the player to.
        """
        super().__init__(posX, posY, "portal")
        this.attributes.update({      \
            "newmap" : newmap,  \
            "locx" : locx,      \
            "locy" : locy,      \
            "time_left" : time  \
        })

    def update(this, delta_time):
        super().update(delta_time)
        this.attributes["time_left"] -= delta_time
        if this.attributes["time_left"] <= 0:
            world.to_del.append(this)

    def collide(this, other):
        "If collided with player, brings them to the new map."
        if other.type == "player":
            world.to_del_plr.append(other) # Move player out of map
            world.move_requests.append((this.attributes["newmap"], other)) # Put player in new map
            other.X = this.attributes["locx"] # Set player coords for new map
            other.Y = this.attributes["locy"]

    def char(this):
        return 'O'

    def color(this):
        return display.BLUE

 


