from objects import General

class directed_attack(General.base_attack.base_attack):
    def __init__(this, posX, posY, damage, owner, move_x, move_y, speed):
        super().__init__(posX, posY, damage, owner)
        this.attributes.update({"move_x" : move_x, "move_y" : move_y, "speed" : speed, "sincemove" : 0})

    def update(this, delta_time):
        this.attributes["sincemove"] += delta_time
        if this.attributes["sincemove"] > this.attributes["speed"]:
            this.attributes["sincemove"] = 0
            this.X += this.attributes["move_x"]
            this.Y += this.attributes["move_y"]


    



