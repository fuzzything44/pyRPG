import world

from effects import effect

from objects import General

class war_enemy(General.enemy_base.enemy_base):
    """Walks around maybe?"""

    def __init__(this, posX, posY, spawner = None):
        super().__init__(posX, posY, 10, 10, 1, 3, [], spawner)
        this.attributes["speed"] = 700

    def update(this, delta_time):
        if "mov_del" not in this.attributes["effects"]:
            # Find nearest player
            locX = this.X # For quicker checking
            locY = this.Y
            
            closest_plr = None
            dist = 101 # Only players close enough
            for plr in world.players:
                if (locX - plr.X) ** 2 + (locY - plr.Y) ** 2 < dist:
                    closest_plr = plr
                    dist = ((locX - plr.X)**2 + (locY - plr.Y)**2) ** .5

            # Now that we have the closest enemy, damage it.
            if closest_plr is not None:
                dist_x = closest_plr.X - locX
                dist_y = closest_plr.Y - locY

                move_x = 0 if dist_x == 0 else dist_x // abs(dist_x)
                move_y = 0 if dist_y == 0 else dist_y // abs(dist_y)

                this.X += move_x
                this.Y += move_y
            this.attributes["effects"]["mov_del"] = effect.effect(this, this.attributes["speed"])

        super().update(delta_time)

    def collide(this, obj):
        if (not this.team & obj.team) and ("HP" in obj.attributes):
            obj.attributes["HP"] -= this.attributes["damage"]
            if this.attributes["spawner"] is not None:
                this.attributes["spawner"].attributes["current_enemy"] = None
            world.to_del.append(this)
    
    def char(this):
        return "%"


