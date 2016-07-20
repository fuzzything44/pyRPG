import display
import world

def attk_update(this, delta_time):
    this.attributes["to_move"] += delta_time
    if this.attributes["to_move"] >= this.attributes["speed"]:
        this.attributes["to_move"] = 0
        this.X += this.attributes["movex"]
        this.Y += this.attributes["movey"]
        this.attributes["range"] -= 1
        try:
            if (this.attributes["range"] < 0) or (not world.map[this.getCoords()[0]][this.getCoords()[1]][2]):
                # Hit something or out of range.
                world.to_del.append(this)
        except:
            pass # Out of map, will be automatically deleted

def attk_coll(this, oth):
    if not (this.attributes["owner"] is oth):
        try: # Deal damage
            oth.attributes["HP"] -= this.attributes["damage"]
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
        except: # Or not...
            pass
    
def attk_char(this):
    return '!'

def attk_color(this):
    return display.MAGENTA

attk_type = "damage"

attk_attributes = {     \
    "movex" : 0,        \
    "movey" : 0,        \
    "damage" : 1,       \
    "range" : 1,        \
    "speed" : 1,        \
    "to_move": 0,       \
    "owner" : 0         \
  }