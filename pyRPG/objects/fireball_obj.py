#TODO make fireball object
from objects import attack
from effects import fire
import display
   
update = attack.attk_update

def collide(this, other):
     if not (this.attributes["owner"] is other):
        try: # Deal damage
            other.attributes["HP"] -= this.attributes["damage"]
            world.to_del.append(this)
            other.attributes["effects"]["fire"] = [fire.fire, lambda x: 0, 1000]
        except: # Or not...
            pass

def color(this):
    return display.RED

def char(this):
    return 'o'

type = 'damage'