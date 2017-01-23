import display
import world

from objects import world_object

class lever(world_object.world_object):
    """ Pullable lever. Does things when pulled"""

    def __init__(this, posX, posY, on_left, on_right, start_left = True):
        """Parameters:
            posX: The X position of the lever.
            posY: The Y position of the lever.
            on_left: The function called when lever is moved to the left position.
            on_right: The function called when the lever is moved to the right position.
            start_mode: The position the lever starts as.
"""
        super().__init__(posX, posY, "interactable")
        # on_left, on_right, and on_mid are functions it runs when it is moved to that position
        this.attributes.update({    \
            "is_left" : start_left, \
            "on_left" : on_left,    \
            "on_right" : on_right   \
          })

    def update(this, delta_time):
        "Checks if player is pulling it and if they're at the correct side of it."
        for plr in world.players:
            if plr.keys[display.KEY_E]: # If they pulled the lever...
                if (plr.X == this.X - 1) and (plr.Y == this.Y) and (not this.attributes["is_left"]): # They're to the left, not already max left
                    this.attributes["is_left"] = True
                    this.attributes["on_left"](this) # Call on_left with this as a parameter.
                if (plr.X == this.X + 1) and (plr.Y == this.Y) and (this.attributes["is_left"]): # They're to the right, not already max right.
                    this.attributes["is_left"] = False
                    this.attributes["on_right"](this) # It was pulled to the right
            else:
                if (plr.X == this.X - 1 or plr.X == this.X + 1) and plr.Y == this.Y and plr.attributes["sidebar"].count('\n') < 29:
                    plr.attributes["sidebar"] += "Press E to pull the lever"
    def color(this):
        "Returns green"
        return display.GREEN
    
    def char(this):
        "Returns a character corresponding to the position the lever is in."
        if this.attributes["is_left"]:
            return "\\\\"
        return "/"
    
