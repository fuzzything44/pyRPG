import display
import world
from objects.General import portal

class lock_portal(portal.portal):
    """Portal only usable if no enemies are in the map"""
    def collide(this, other):
        "Brings player to new map if no enemies in map and collided with player."
        for obj in world.objects: # Check if there are any enemies left in the map
            if obj.type == "enemy":
                return # An enemy was found. ABORT!
        return super().collide(other)
    
    def color(this):
        "Normal if usable, red if enemies in map."
        for obj in world.objects:
            if obj.type == "enemy":
                return display.RED
        return super().color()
