import display
import world

from effects import fire

from objects import world_object
from objects.Player import attack

class fireball_atk(attack.attack):
    def collide(this, other):
         if this.attributes["owner"].type != other.type:
            if "HP" in other.attributes: # Deal damage
                other.attributes["HP"] -= this.attributes["damage"]
                world.to_del.append(this)
                if "effects" in other.attributes:
                    other.attributes["effects"]["fire"] = [fire.fire, world_object.no_func, 1000]
    
    def color(this):
        return display.RED
    
    def char(this):
        return 'o'