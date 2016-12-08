import display
import world

from objects import world_object

class base_attack(world_object.world_object):
    """ Basic attack. Just can collide to do damage, has a display color."""
    def __init__(this, posX, posY, damage, owner):
        """Parameters:
            posX: The X position of the attack.
            posY: The Y position of the attack.
            damage: How much damage the attack does.
            owner: The object that spawned the attack.
"""
        super().__init__(posX, posY, "damage")
        this.attributes = {     \
            "damage" : damage,  \
            "owner" : owner     \
          }
    
    def collide(this, oth):
        "Checks if collided object is of a different type than spawner. If so, does damage and gets destroyed."
        if (this.attributes["owner"].type != oth.type) and ("HP" in oth.attributes):
            oth.attributes["HP"] -= this.attributes["damage"]
            if "dmg_dist" in oth.attributes: # Add damage to damage distribution
                oth.attributes["dmg_dist"][this.attributes["owner"]] += this.attributes["damage"]

            world.to_del.append(this)
    def char(this):
        "Always a '!'"
        return '!'
    
    def color(this):
        "Returns magenta"
        return display.MAGENTA
    