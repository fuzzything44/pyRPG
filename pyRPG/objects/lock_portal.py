import display
import world
from objects import portal
from objects import world_object

update = world_object.no_func

def collide(this, other):
    for obj in world.objects: # Check if there are any enemies left in the map
        if obj.type == "enemy":
            return # An enemy was found. ABORT!
    portal.collide(this, other)

char = portal.char

def color(this):
    for obj in world.objects:
        if obj.type == "enemy":
            return display.RED
    return display.CYAN
type = portal.type
attributes = portal.attributes