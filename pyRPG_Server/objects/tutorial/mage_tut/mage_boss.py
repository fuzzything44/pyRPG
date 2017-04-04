
import math

import world

from effects import effect

from objects import world_object
from objects import General

from objects.tutorial.mage_tut import directed_attack

class mage_boss(General.enemy_base.enemy_base):
    def __init__(this, posX, posY, owner):
        super().__init__(posX, posY, 250, 25, 15, 10, [], owner)
        this.attributes["go_diag"] = False

    def update(this, delta_time):
        super().update(delta_time)

        # Attack
        if "atk_del" not in this.attributes["effects"]:
            if this.attributes["go_diag"]:
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 1 , 1 , 300))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 1 , -1, 300))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, -1, 1 , 300))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, -1, -1, 300))
            else:
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 1 , 0 , 150))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, -1, 0 , 150))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 0 , 1 , 150))
                world.objects.append(directed_attack.directed_attack(this.X, this.Y, this.attributes["damage"], this, 0 , -1, 150))
            this.attributes["go_diag"] = not this.attributes["go_diag"]
            this.attributes["effects"]["atk_del"] = effect.effect(this, 1000)

        # Move
            

    def collide(this, obj):
        if (not this.team & obj.team) and ("HP" in obj.attributes) and (obj.attributes["name"] + "-attack-del" not in this.attributes["effects"]): 
            # If collides with something, damage it. Wait to damage again for 500ms
            obj.attributes["HP"] -= this.attributes["damage"]
            this.attributes["effects"][obj.attributes["name"] + "-attack-del"] = effect.effect(this, 500)

    def char(this):
        return 'B'




