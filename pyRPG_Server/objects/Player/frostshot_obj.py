import display
import world
from effects import frozen
from objects.Player import attack
from objects import world_object

class frostshot_atk(attack.attack):
    def collide(this, other):
         if this.attributes["owner"].type != other.type:
            if "HP" in other.attributes: # Deal damage
                other.attributes["HP"] -= min(50, this.attributes["damage"])
                world.to_del.append(this)
                if "effects" in other.attributes:
                    other.attributes["effects"]["frozen"] = frozen.frozen(other, 2500, "Frozen")
                    other.attributes["stuckX"] = other.X
                    other.attributes["stuckY"] = other.Y
    
    def color(this):
        return display.BLUE
    
    def char(this):
        return 'o'