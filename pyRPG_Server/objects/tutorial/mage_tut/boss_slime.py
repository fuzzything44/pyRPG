import display
from objects import world_object
import world

class boss_slime(world_object.world_object):
    def __init__(this, posX, posY, boss, health = 30):
        super().__init__(posX, posY, "obstacle", world_object.TEAM_ENEMY)
        this.attributes["HP"] = health
        this.attributes["boss"] = boss

    def update(this, delta_time):
        super().update(delta_time)
        world.map[this.X][this.Y][3] = False # Block movement

        if this.attributes["HP"] <= 0:
            world.map[this.X][this.Y][3] = True # Allow movement again.
            world.to_del.append(this)

    def char(this):
        if (this.X, this.Y) == (this.attributes["boss"].X, this.attributes["boss"].Y):
            return this.attributes["boss"].char()
        return '#'

    def color(this):
        if (this.X, this.Y) == (this.attributes["boss"].X, this.attributes["boss"].Y):
            return this.attributes["boss"].color()
        return display.GREEN


