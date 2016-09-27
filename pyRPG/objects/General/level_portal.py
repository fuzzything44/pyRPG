import display
import world
from objects.General import portal
from objects import world_object

update = world_object.no_func

def collide(this, other):
    if world.player.attributes["level"] < this.attributes["level"]:
        return # Too low of level.
    return portal.collide(this, other)

char = portal.char

def color(this):
    if world.player.attributes["level"] >= this.attributes["level"]:
        return display.BLUE
    return display.RED

type = portal.type

attributes = {\
    "newmap" : "",\
    "locx" : 0,\
    "locy" : 10,\
    "used" : False,\
    "level" : 0
  }