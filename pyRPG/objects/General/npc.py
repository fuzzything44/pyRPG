import display
import world
from objects import world_object

def update(this, delta_time):
    if display.keyDown(ord('E')) and (this.attributes["can_talk"]):
        this.attributes["can_talk"] = False
        # If they're right next to this.
        if (((world.player.X == this.X -1) or (world.player.X == this.X + 1)) and (world.player.Y == this.Y)) or (((world.player.Y == this.Y - 1) or (world.player.Y == this.Y + 1)) and (world.player.X == this.X)):
            # Now we say hi!
            display.menu(this.attributes["text"], this.attributes["opt_params"], *this.attributes["options"])

    if not display.keyDown(ord('E')):
        this.attributes["can_talk"] = True

    if ("HP" in this.attributes) and (this.attributes["HP"] <= 0):
        world.to_del.append(this)

def collide(this, oth):
    pass

def color(this):
    return display.GREEN

def char(this):
    return 'T'

type = "interactable"

attributes = {\
    "text" : "Hello",                           \
    "options" : [["Bye", world_object.no_func]],  \
    "opt_params" : [[]],                        \
    "can_talk" : True                           \
  }