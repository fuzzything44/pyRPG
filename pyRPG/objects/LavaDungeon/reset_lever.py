import world
import display
from objects import world_object

class reset_lever(world_object.world_object):
    def __init__(this, time, lever, to_pos):
        super().__init__(0, 0, "timer-lever")
        this.attributes.update({ "to_reset" : time, "lever" : lever, "pos" : to_pos})

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
    


