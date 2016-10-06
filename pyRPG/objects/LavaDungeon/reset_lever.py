import world
import display
from objects import world_object

def update(this, delta_time):
    this.attributes["to_reset"] -= delta_time
    if this.attributes["to_reset"] <= 0:
        world.to_del.append(this)
        if this.attributes["lever"] is None:
            return
        # Reset lever
        this.attributes["lever"].attributes["mode"] = this.attributes["pos"]
        if this.attributes["pos"] == 0:
            this.attributes["lever"].attributes["on_left"](this.attributes["lever"])
        elif this.attributes["pos"] == 1:
            this.attributes["lever"].attributes["on_right"](this.attributes["lever"])
        else:
            this.attributes["lever"].attributes["on_mid"](this.attributes["lever"])

collide = world_object.no_func

def char(this):
    return '\0' # Invisible

def color(this):
    return 0

type = "timer"

attributes = { "to_reset" : 1000, "lever" : None, "pos" : 0}