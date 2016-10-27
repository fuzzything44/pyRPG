from random import randrange

import display
import world

from effects import effect

from objects.Player import attack
from objects.Loot import chest
from objects.Loot import money
from objects.General import enemy_base
from objects import world_object
from objects.Tutorial import attack

class boss(enemy_base.enemy_base):
    def __init__(this, posX, posY):
        super().__init__(posX, posY, 150.0, 7, 10)
        this.attributes.update({ \
             "effects": {}, \
             "to_atk" : 500,\
             "mov_spd": 500,\
             "atk_spd": 900,\
             "range": 5,    \
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
            this.attributes["effects"]["mov_del"] = effect.effect(this, this.attributes["mov_spd"])
        # Attack code
        this.attributes["to_atk"] -= delta_time
        if this.attributes["to_atk"] <= 0:
            this.attributes["to_atk"] = this.attributes["atk_spd"] - 200 + this.attributes["HP"] # He attacks faster with less HP
            # Find which direction to shoot
            diffX = world.player.X - this.X # How much it needs to move left to hit player
            diffY = world.player.Y - this.Y # How much it needs to move down to hit player
            if diffX < 0:
                diffX = -1
            else:
                diffX = int(not not diffX)
            if diffY < 0:
                diffY = -1
            else:
                diffY = int(not not diffY)
            world.objects.append(attack.boss_attack(this.X + diffX, this.Y + diffY, diffX, diffY, this.attributes["damage"], this.attributes["range"], 250, this))
        
        # Update all effects.
        eff_del_list = []
        for eff_name in this.attributes["effects"]:
            eff = this.attributes["effects"][eff_name]
            eff.tick(delta_time)  # Tick effect
            if eff.time <= 0:           # Remove effect
                eff_del_list.append(eff_name)
        for eff_name in eff_del_list:
            this.attributes["effects"][eff_name].uneffect(this)
            del this.attributes["effects"][eff_name]
        del eff_del_list

        if this.attributes["HP"] <= 0:
            this.die()
            world.load("tutorial.boss-killed")
            world.objects = [world.player] + world.objects
            world.player.X = 10
            world.player.Y = 10
            world.dispworld()
            return True

    def collide(this, obj):
        if obj.type == "player":
            obj.attributes["HP"] -= this.attributes["damage"]
            this.X += 1
            if this.X == world.WORLD_X:
                this.X = 0
    
    def char(this):
        return 'B'
   