#TODO make fireball object
from objects import attack
from effects import fire
import display
import world

update = attack.attk_update

def collide(this, other):
     if not (this.attributes["owner"] is other):
        try: # Deal damage
            other.attributes["HP"] -= this.attributes["damage"]
            world.to_del.append(this)
            if oth.attributes["HP"] <= 0:
                this.attributes["owner"].attributes["EXP"] += 1
                if this.attributes["owner"].attributes["EXP"] <= this.attributes["owner"].attributes["level"]**2:
                    this.attributes["owner"].attributes["EXP"] -= this.attributes["owner"].attributes["level"]**2
                    this.attributes["owner"].attributes["level"] += 1
                    this.attributes["owner"].attributes["maxHP"] += 10
                    this.attributes["owner"].attributes["maxMP"] += 5
                    this.attributes["owner"].attributes["mov_spd"] -= 2
                    this.attributes["owner"].attributes["attk_spd"] -= 3
                    this.attributes["owner"].attributes["magic"] += 2
                    this.attributes["owner"].attributes["strength"] += 2
            other.attributes["effects"]["fire"] = [fire.fire, lambda x: 0, 1000]
        except: # Or not...
            pass
def color(this):
    return display.RED

def char(this):
    return 'o'

type = 'damage'