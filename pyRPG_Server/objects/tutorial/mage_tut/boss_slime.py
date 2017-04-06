import random

import display
from objects import world_object
import world

class boss_slime(world_object.world_object):
    def __init__(this, posX, posY, boss):
        super().__init__(posX, posY, "obstacle", world_object.TEAM_ENEMY)
        this.attributes["HP"] = 10
        this.attributes["boss"] = boss
        this.attributes["lifetime"] = random.randrange(10000, 40000) # Countdown to self destroy.

    def update(this, delta_time):
        super().update(delta_time)
        world.map[this.X][this.Y][3] = False # Block movement

        this.attributes["lifetime"] -= delta_time

        if this.attributes["lifetime"] <= 0:
            this.attributes["HP"] = 0

        if this.attributes["HP"] <= 0:
            world.map[this.X][this.Y][3] = True # Allow movement again.
            world.to_del.append(this)

    def collide(this, oth):
        if oth.type == "obstacle" and "HP" in oth.attributes and oth.attributes["HP"] > 0:
            this.attributes["HP"] = 0

    def char(this):
        if (this.X, this.Y) == (this.attributes["boss"].X, this.attributes["boss"].Y):
            return this.attributes["boss"].char()
        return '#'

    def color(this):
        if (this.X, this.Y) == (this.attributes["boss"].X, this.attributes["boss"].Y):
            return this.attributes["boss"].color()
        return display.GREEN


