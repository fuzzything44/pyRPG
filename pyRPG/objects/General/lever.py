import display
from objects import world_object

def update(this, delta_time):
    if display.keyDown(ord('E')) and (this.attributes["can_pull"]): # If they pulled the lever...
        this.attributes["can_pull"] = False
        if (player.X == this.X - 1) and (this.attributes["mode"] != 0): # They're to the left, not already max left
            this.attributes["mode"] -= 1
            if this.attributes["mode"] == 0: # It was pulled to the left
                this.attributes["on_left"](this) # Call on_left with this as a parameter.
            else: # It was pulled to the mid
                this.attributes["on_mid"](this)
        if (player.X == this.X + 1) and (this.attributes["mode"] != 2): # They're to the right, not already max right.
            this.attributes["mode"] += 1
            if this.attributes["mode"] == 2:
                this.attributes["on_right"](this) # It was pulled to the right
            else:
                this.attributes["on_mid"](this) # It was pulled to the mid.
    if not display.keyDown(ord('E')):
        this.attributes["can_pull"] = True

def collide(this, oth):
    pass

def color(this):
    return display.YELLOW

def char(this):
    if this.attributes["mode"] == 0:
        return "\\"
    if this.attributes["mode"] == 1:
        return "|"
    if this.attributes["mode"] == 2:
        return "/"
    return "\0"

type = "interactable"
# Modes: 0 = left, 1 = mid, 2 = right
# on_left, on_right, and on_mid are functions it runs when it is moved to that position
attributes = {\
    "mode" : 0,\
    "on_left" : world_object.no_func,   \
    "on_right" : world_object.no_func,  \
    "on_mid" : world_object.no_func,    \
    "can_pull" : True                   \
  }