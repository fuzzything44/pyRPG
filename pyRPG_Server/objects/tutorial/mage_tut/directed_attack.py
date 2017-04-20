import world

from objects import General

class directed_attack(General.base_attack.base_attack):
    def __init__(this, posX, posY, damage, owner, move_x, move_y, speed, die_on_walls = True, range = 999):
        super().__init__(posX, posY, damage, owner)
        this.attributes.update({"move_x" : move_x, "move_y" : move_y, "speed" : speed, "sincemove" : 0, "die_on_walls" : die_on_walls, "range": range})

    def update(this, delta_time):
        this.attributes["sincemove"] += delta_time
        if this.attributes["sincemove"] > this.attributes["speed"]:
            this.attributes["sincemove"] = 0
            this.X += this.attributes["move_x"]
            this.Y += this.attributes["move_y"]
            this.attributes["range"] -= 1
            if this.attributes["range"] <= 0:
                world.to_del.append(this)
        if not world.out_of_bounds(this.X, this.Y) and not world.map[this.X][this.Y][3] and this.attributes["die_on_walls"]: # Hit a wall.
            world.to_del.append(this)





