import display
import world

from effects import fire

from objects import attack
from objects import world_object
update = attack.attk_update

def collide(this, other):
     if this.attributes["owner"].type != other.type:
        try: # Deal damage
            other.attributes["HP"] -= this.attributes["damage"]
            world.to_del.append(this)
            other.attributes["effects"]["fire"] = [fire.fire, world_object.no_func, 1000]
            if this.attributes["owner"].attributes["magic"] >= 25:
                other.attributes["effects"]["fire"] = [fire.bigfire, world_object.no_func, 1500]
        except: # Or not...
            pass
def color(this):
    return display.RED

def char(this):
    return 'o'

type = 'damage'