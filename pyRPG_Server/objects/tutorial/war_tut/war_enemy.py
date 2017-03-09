import world

from effects import effect

from objects import General

class war_enemy(General.enemy_base.enemy_base):
    """Walks around maybe?"""

    def __init__(this, posX, posY):
        super().__init__(posX, posY, 10, 10, 1, 3)
        this.attributes["speed"] = 1000

    def update(this, delta_time):
        if "mov_del" not in this.attributes["effects"]:
            pass # TODO: move.
            this.attributes["effects"]["mov_del"] = effect.effect(this, this.attributes["speed"])

        super().update(delta_time)

    def collide(this, obj):
        if (not this.team & obj.team) and ("HP" in obj.attributes):
            obj.attributes["HP"] -= this.attributes["damage"]
            world.to_del.append(this)
    
    def char(this):
        return "%"


