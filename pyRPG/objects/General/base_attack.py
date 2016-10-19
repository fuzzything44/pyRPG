import display
import world

from objects import world_object

class base_attack(world_object.world_object):
    def __init__(this, posX, posY, damage, owner):
        super().__init__(posX, posY, "damage")
        this.attributes = {     \
            "damage" : damage,  \
            "owner" : owner     \
          }
    
    def collide(this, oth):
        if (this.attributes["owner"].type != oth.type) and ("HP" in oth.attributes):
            oth.attributes["HP"] -= this.attributes["damage"]
            world.to_del.append(this)
    
    def char(this):
        return '!'
    
    def color(this):
        return display.MAGENTA
    