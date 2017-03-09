import math

import world

from effects import effect

from objects import world_object
from objects import General

from objects.tutorial.mage_tut import directed_attack

class mage_enemy(General.enemy_base.enemy_base):
    """Stays still, shoots up/down/left/right at even intervals"""
    def __init__(this, posX, posY):
        super().__init__(posX, posY, 16, 15, 1, 3, [])
        

    def update(this, delta_time):
        super().update(delta_time)
        if "atk_del" not in this.attributes["effects"]:
            closest_player = None
            dist = float("Inf")
            for plr in world.players: # Find closest player
                if (this.X - plr.X) ** 2 + (this.Y - plr.Y) ** 2 < dist:
                    closest_player = plr
                    dist = (this.X - plr.X) ** 2 + (this.Y - plr.Y) ** 2
            if closest_player is not None:
                x_dist = this.X - closest_player.X 
                y_dist = this.Y - closest_player.Y 
                x_mov = 0
                y_mov = 0
                if abs(x_dist) > abs(y_dist):
                    x_mov =  -1 if x_dist > 0 else 1
                else:
                    y_mov =  -1 if y_dist > 0 else 1

                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, x_mov, y_mov, 150))
            this.attributes["effects"]["atk_del"] = effect.effect(this, 1000)
            

    def collide(this, obj):
        if (not this.team & obj.team) and ("HP" in obj.attributes) and (obj.attributes["name"] + "-attack-del" not in this.attributes["effects"]): 
            # If collides with something, damage it. Wait to damage again for 500ms
            obj.attributes["HP"] -= this.attributes["damage"]
            this.attributes["effects"][obj.attributes["name"] + "-attack-del"] = effect.effect(this, 500)

    def char(this):
        return '+'




