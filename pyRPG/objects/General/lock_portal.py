import display
import world
from objects.General import portal
from objects import world_object

update = world_object.no_func

def collide(this, other):
    for obj in world.objects: # Check if there are any enemies left in the map
        if obj.type == "enemy":
            return # An enemy was found. ABORT!
    return portal.collide(this, other)

char = portal.char

def color(this):
    for obj in world.objects:
        if obj.type == "enemy":
            return display.RED
    return display.BLUE
type = portal.type
attributes = portal.attributes