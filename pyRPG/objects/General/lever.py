import display
import world

from objects import world_object

class lever(world_object.world_object):
    MODE_LEFT = 0
    MODE_MID = 1
    MODE_RIGHT = 2

    def __init__(this, posX, posY, on_left, on_right, on_mid = None, start_mode = 0):
        super().__init__(posX, posY, "interactable")
        # on_left, on_right, and on_mid are functions it runs when it is moved to that position
        this.attributes.update({    \
            "mode" : 0,             \
            "on_left" : on_left,    \
            "on_right" : on_right,  \
            "on_mid" : on_mid,      \
            "can_pull" : True       \
          })

    def update(this, delta_time):
        if display.keyDown(ord('E')) and (this.attributes["can_pull"]): # If they pulled the lever...
            if (world.player.X == this.X - 1) and (this.attributes["mode"] != this.MODE_LEFT): # They're to the left, not already max left
                this.attributes["can_pull"] = False
                this.attributes["mode"] -= 1
                if this.attributes["mode"] == 0: # It was pulled to the left
                    this.attributes["on_left"](this) # Call on_left with this as a parameter.
                else: # It was pulled to the mid
                    if this.attributes["on_mid"] is None:
                        this.attributes["mode"] -= 1
                        this.attributes["on_left"](this)
                    else:
                        this.attributes["on_mid"](this)
            if (world.player.X == this.X + 1) and (this.attributes["mode"] != this.MODE_RIGHT): # They're to the right, not already max right.
                this.attributes["can_pull"] = False
                this.attributes["mode"] += 1
                if this.attributes["mode"] == 2:
                    this.attributes["on_right"](this) # It was pulled to the right
                else:
                    if this.attributes["on_mid"] is None:
                        this.attributes["mode"] += 1
                        this.attributes["on_right"](this)
                    else:
                        this.attributes["on_mid"](this) # It was pulled to the mid.
        if not display.keyDown(ord('E')):
            this.attributes["can_pull"] = True
       
    def color(this):
        return display.YELLOW
    
    def char(this):
        if this.attributes["mode"] == lever.MODE_LEFT:
            return "\\"
        if this.attributes["mode"] == lever.MODE_MID:
            return "|"
        if this.attributes["mode"] == lever.MODE_RIGHT:
            return "/"
        return "\0"
    
