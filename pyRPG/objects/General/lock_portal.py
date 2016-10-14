import display
import world
from objects.General import portal

class lock_portal(portal.portal):
    def collide(this, other):
        for obj in world.objects: # Check if there are any enemies left in the map
            if obj.type == "enemy":
                return # An enemy was found. ABORT!
        return super().collide(other)
    
    def color(this):
        for obj in world.objects:
            if obj.type == "enemy":
                return display.RED
        return super().color()
