import display
import world

from objects import world_object

class attack(world_object.world_object):
    def __init__(this, posX, posY, movex, movey, damage, range, speed, owner):
        super().__init__(posX, posY, "damage")
        this.attributes = {     \
            "movex" : movex,    \
            "movey" : movey,    \
            "damage" : damage,  \
            "range" : range,    \
            "speed" : speed,    \
            "to_move": 0,       \
            "owner" : owner     \
          }
    def update(this, delta_time):
        this.attributes["to_move"] += delta_time
        if this.attributes["to_move"] >= this.attributes["speed"]:
            this.attributes["to_move"] = 0
            this.X += this.attributes["movex"]
            this.Y += this.attributes["movey"]
            this.attributes["range"] -= 1
            if (this.attributes["range"] <= 0) or world.out_of_bounds(this.X, this.Y) or (not world.map[this.X][this.Y][3]):
                    # Hit something, outside map, or out of range.
                    world.to_del.append(this)
    
    def collide(this, oth):
        if (this.attributes["owner"].type != oth.type) and ("HP" in oth.attributes):
            oth.attributes["HP"] -= this.attributes["damage"]
            world.to_del.append(this)
    
    def char(this):
        return '!'
    
    def color(this):
        return display.BLUE
    
