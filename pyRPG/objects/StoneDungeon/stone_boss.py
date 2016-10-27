from random import randrange

import display
import world

from items import item
from objects.StoneDungeon import attack
from objects.Loot import chest
from objects import world_object
from objects.General import enemy_base

class stone_boss(enemy_base.enemy_base):
    def __init__(this, posX, posY):
        super().__init__(posX, posY, 1000.0, 30, 50, 20, [])
        this.attributes.update({\
             "lastHP" : 1000.0, \
             "effects": {}, \
             "mov_spd": 400, \
             "atk_spd": 1000, \
             "range": 10, \
        })

    def update(this, delta_time):
        # Movement code
        if not ("mov_del" in this.attributes["effects"]):
            diffX = this.X - world.player.X # How much it needs to move left to hit player
            diffY = this.Y - world.player.Y # How much it needs to move down to hit player
            if diffX < 0:
                this.X += 1
            else:
                this.X -= (not not diffX) # Should give either 1 or 0.
            if diffY < 0:
                this.Y += 1
            else:
                this.Y -= (not not diffY)
            # Add boundary checking
            if this.X == 0: # Left side
                this.X += 1
            if this.X == world.WORLD_X - 1: # Right side
                this.X -= 1
            if this.Y == 0: # Top
                this.Y += 1
            if this.Y == world.WORLD_Y - 1: # Bottom
                this.Y -= 1
            this.attributes["effects"]["mov_del"] = [world_object.no_func, world_object.no_func, this.attributes["mov_spd"]]
        if not ("atk_del" in this.attributes["effects"]):
            # Attack!
            world.objects.append(attack.shoot_attack(this.X + 1, this.Y - 1, 1 , -1, this.attributes["damage"], this.attributes["range"], 300, this))
            world.objects.append(attack.shoot_attack(this.X + 1, this.Y    , 1 , 0 , this.attributes["damage"], this.attributes["range"], 300, this))
            world.objects.append(attack.shoot_attack(this.X + 1, this.Y + 1, 1 , 1 , this.attributes["damage"], this.attributes["range"], 300, this))
            world.objects.append(attack.shoot_attack(this.X    , this.Y - 1, 0 , -1, this.attributes["damage"], this.attributes["range"], 300, this))
            world.objects.append(attack.shoot_attack(this.X    , this.Y + 1, 0 , 1 , this.attributes["damage"], this.attributes["range"], 300, this))
            world.objects.append(attack.shoot_attack(this.X - 1, this.Y - 1, -1, -1, this.attributes["damage"], this.attributes["range"], 300, this))
            world.objects.append(attack.shoot_attack(this.X - 1, this.Y    , -1, 0 , this.attributes["damage"], this.attributes["range"], 300, this))
            world.objects.append(attack.shoot_attack(this.X - 1, this.Y + 1, -1, 1 , this.attributes["damage"], this.attributes["range"], 300, this))
            this.attributes["effects"]["atk_del"] = [world_object.no_func, world_object.no_func, this.attributes["atk_spd"]]

        if this.attributes["HP"] < this.attributes["lastHP"]:
            diff = this.attributes["lastHP"] - this.attributes["HP"] # Difference in HP between this frame and last frame
            if diff > 10: # Soft damage cap
                diff = 10 + ((diff - 10) ** .75)
            if diff > 50: # Hard damage cap
                diff = 50
            this.attributes["lastHP"] -= diff
            this.attributes["HP"] = this.attributes["lastHP"]
        super().update(delta_time)
    
    def char(this):
        return 'P'
    

