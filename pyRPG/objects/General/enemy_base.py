import display
import world

from objects import world_object

class enemy_base(world_object.world_object):
    def __init__(this, posX, posY, health = 1, damage = 1, exp = 1):
        super().__init__(posX, posY, "enemy")
        this.attributes.update({"HP" : health, "damage" : damage, "EXP" : exp})

    def update(this, delta_time):
        if this.attributes["HP"] <= 0:
            die()

    def color(this):
        return display.CYAN

    def die(this):
        world.to_del.append(this) # Delete
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give exp

