import world

from objects.General import base_attack

class shoot_attack(base_attack.base_attack):
    def __init__(this, posX, posY, movex, movey, damage, range, speed, owner):
        super().__init__(posX, posY, damage, owner)
        this.attributes.update({     \
            "movex" : movex,    \
            "movey" : movey,    \
            "range" : range,    \
            "speed" : speed,    \
            "to_move": 0,       \
          })

    def update(this, delta_time):
        this.attributes["to_move"] += delta_time
        if this.attributes["to_move"] >= this.attributes["speed"]:
            this.attributes["to_move"] = 0
            this.X += this.attributes["movex"]
            this.Y += this.attributes["movey"]
            this.attributes["range"] -= 1
            if (this.attributes["range"] <= 0) or world.out_of_bounds(this.X, this.Y) or (not world.map[this.X][this.Y][3]):
                    # Hit something or out of range.
                    world.to_del.append(this)
