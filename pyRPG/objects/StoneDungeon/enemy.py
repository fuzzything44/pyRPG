from random import randrange

import display
import world

from objects.Player import attack
from objects.Loot import money
from objects import world_object
from objects.General import enemy_base

from items import bread

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
        super().update(delta_time)
    
    def collide(this, obj):
        if obj.type == "player":
            obj.attributes["HP"] -= this.attributes["damage"]
            this.X += 1

    def char(this):
      return 'Q'

