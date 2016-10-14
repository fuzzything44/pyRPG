#This is the enemy they kill to level up and gives a message upon levelling.
import display
import world

from objects.Tutorial import tutorial_move_enemy

class level_up_enemy(tutorial_move_enemy.move_enemy):
    # Pattern is ^<>^^>>V<VV<
    def __init__(this, posX, posY, health = 5, damage = 3, exp = 1, pattern_loc = 0):
        super().__init__(posX, posY, health, damage, exp, pattern_loc)
        this.pattern = [0, -1],[-1, 0],[1, 0],[0, -1],[0, -1], [1, 0], [1, 0], [0, 1], [-1, 0], [0, 1], [0, 1], [-1, 0]

    def update(this, delta_time):
        if this.attributes["HP"] <= 0:
            die()
            if world.player.attributes["level"] >= 2: # If they're level 2, they leveled up and need to be notified.
                world.load("tutorial.2-killed")
                world.objects = [world.player] + world.objects
                if world.player.X == world.WORLD_X - 1: # If they're on the portal
                    world.player.X -= 1 # Push them back a bit
                world.dispworld()
                return True
            return
        super().update(delta_time)

   