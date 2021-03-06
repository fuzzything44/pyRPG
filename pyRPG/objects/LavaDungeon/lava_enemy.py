from random import randrange

import display
import world

from items import item
from items import bread

from objects.Loot import money
from objects.Loot import lootbag
from objects import world_object
from spells import spell

from objects.LavaDungeon import attack
from objects.General import enemy_base

from effects import effect

class lava_enemy(enemy_base.enemy_base):
    def __init__(this, posX, posY):
        super().__init__(posX, posY, 150.0, 25, 17, 0, [[bread.bread(3), 100]]) # TODO: Add actual drop
        this.attributes.update({\
              "effects" : {},   \
              "mov_spd" : 800,  \
              "atk_spd" : 300,  \
              "aggro_range" : 100\
          })

    def update(this, delta_time):
        # If within 5 tiles of player...
        if ((this.X - world.player.X) ** 2 + (this.Y - world.player.Y) ** 2) <= this.attributes["aggro_range"]:
            if not ("mov_del" in this.attributes["effects"]): # Possibly move to player.
                diffX = this.X - world.player.X # How much it needs to move left to hit player
                diffY = this.Y - world.player.Y # How much it needs to move down to hit player
                if diffX < 0 and (world.map[this.X + 1][this.Y][3]): # Make sure you don't move onto a wall
                    this.X += 1
                if diffX > 0 and (world.map[this.X - 1][this.Y][3]):
                    this.X -= 1
                if diffY < 0 and world.map[this.X][this.Y + 1][3]:
                    this.Y += 1
                if diffY > 0 and world.map[this.X][this.Y - 1][3]:
                    this.Y -= 1
                # Add boundary checking
                if this.X == 0: # Left side
                    this.X += 1
                if this.X == world.WORLD_X - 1: # Right side
                    this.X -= 1
                if this.Y == 0: # Top
                    this.Y += 1
                if this.Y == world.WORLD_Y - 1: # Bottom
                    this.Y -= 1
                this.attributes["effects"]["mov_del"] = effect.effect(this, this.attributes["mov_spd"])
   
        super().update(delta_time)

    def collide(this, obj):
        if obj.type == "player" and ("del_atk" not in this.attributes["effects"]):
            obj.attributes["HP"] -= this.attributes["damage"]
            this.attributes["effects"]["del_atk"] = effect.effect(this, this.attributes["mov_spd"])
    
    def char(this):
      return 'S'


