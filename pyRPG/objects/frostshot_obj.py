from effects import frozen
from objects import attack
from objects import world_object
update = attack.attk_update

def collide(this, other):
     if this.attributes["owner"].type != other:
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
            other.attributes["effects"]["frozen"] = [frozen.frozen, frozen.unfreeze, 1000]
            other.attributes["stuckX"] = other.X
            other.attributes["stuckY"] = other.Y

        except: # Or not...
            pass
def color(this):
    return display.CYAN

def char(this):
    return 'o'

type = 'damage'