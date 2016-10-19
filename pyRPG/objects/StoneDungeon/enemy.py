from random import randrange

import display
import world

from objects.Player import attack
from objects.Loot import money
from objects import world_object
from objects.General import enemy_base
from spells import spell

class stone_enemy(enemy_base.enemy_base):
    def __init__(this, posX, posY):
        super().__init__(posX, posY, 10.0, 5, 1, 3)
        this.mov_spd = 350
        this.attributes["effects"] = {}

    def update(this, delta_time):
        if randrange(0, this.mov_spd) < delta_time:  
            newX = this.X + randrange(-1, 2)
            newY = this.Y + randrange(-1, 2)
            # If the new tile is walkable on and not out of bounds
            if (newX >= 0) and (newX < world.WORLD_X) and (newY >= 0) and (newY < world.WORLD_Y) and (world.map[newX][newY][3]):
                this.X = newX
                this.Y = newY
        eff_del_list = []
        for eff in this.attributes["effects"]:
            this.attributes["effects"][eff][0](this, delta_time)       # Tick code
            this.attributes["effects"][eff][2] -= delta_time           # Lower time
            if this.attributes["effects"][eff][2] <= 0:                # Remove effect
                eff_del_list.append(eff)
        for to_del in eff_del_list:
            this.attributes["effects"][to_del][1](this)
            del this.attributes["effects"][to_del]
        del eff_del_list
        super().update(delta_time)
    
    def collide(this, obj):
        if obj.type == "player":
            obj.attributes["HP"] -= this.attributes["damage"]
            this.X += 1

    def char(this):
      return 'Q'

