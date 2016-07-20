import display
import world

from effects import fire

from objects import attack
from objects import world_object
update = attack.attk_update

def collide(this, other):
     if not (this.attributes["owner"] is other):
        try: # Deal damage
            other.attributes["HP"] -= this.attributes["damage"]
            world.to_del.append(this)
            if oth.attributes["HP"] <= 0:
                this.attributes["owner"].attributes["EXP"] += other.attributes["EXP"]
                while this.attributes["owner"].attributes["EXP"] >= this.attributes["owner"].attributes["level"]**2:
                    this.attributes["owner"].attributes["EXP"] -= this.attributes["owner"].attributes["level"]**2
                    this.attributes["owner"].attributes["level"] += 1
                    this.attributes["owner"].attributes["maxHP"] += 10
                    this.attributes["owner"].attributes["maxMP"] += 5
                    this.attributes["owner"].attributes["mov_spd"] -= 2
                    this.attributes["owner"].attributes["attk_spd"] -= 3
                    this.attributes["owner"].attributes["magic"] += 2
                    this.attributes["owner"].attributes["strength"] += 2
            other.attributes["effects"]["fire"] = [fire.fire, world_object.no_func, 1000]

        except: # Or not...
            pass
def color(this):
    return display.RED

def char(this):
    return 'o'

type = 'damage'