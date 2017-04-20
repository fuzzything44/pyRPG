from objects import world_object

from objects.tutorial.mage_tut import mage_boss

import display
import world

class mage_boss_spawner(world_object.world_object):

    def __init__(this, posX, posY):
        super().__init__(posX, posY, "spawner")
        this.attributes["current_enemy"] = None
        this.attributes["since_death"] = 30000

    def update(this, delta_time):
        if this.attributes["current_enemy"] is None:
            this.attributes["since_death"] += delta_time
            if this.attributes["since_death"] > 30000: # 30s respawn
                s_enemy = mage_boss.mage_boss(this.X, this.Y, this)
                world.objects.append(s_enemy)
                this.attributes["current_enemy"] = s_enemy
                this.attributes["since_death"] = 0

    



