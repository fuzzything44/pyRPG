#This is the enemy they kill to level up and gives a message upon levelling.
import display
import world

from objects.Tutorial import tutorial_move_enemy

def update(this, delta_time):
    this.attributes["del_mov"] -= delta_time
    if this.attributes["del_mov"] <= 0: # If they can move
        this.attributes["del_mov"] = 250 # Wait to move again

        # Move depending on where we are in the pattern.
        this.X += this.attributes["pattern"][this.attributes["pattern_loc"]][0]
        this.Y += this.attributes["pattern"][this.attributes["pattern_loc"]][1]
        # Go to the next step of the pattern
        this.attributes["pattern_loc"] += 1
        # Restart pattern if needed.
        if this.attributes["pattern_loc"] >= len(this.attributes["pattern"]):
            this.attributes["pattern_loc"] = 0
    if this.attributes["HP"] <= 0:
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give exp
        if world.player.attributes["level"] == 2: # If they're level 2, they leveled up and need to be notified.
            world.load("tutorial.2-killed")
            world.objects = [world.player] + world.objects
            if world.player.X == world.WORLD_X - 1: # If they're on the portal
                world.player.X -= 1 # Push them back a bit
            world.dispworld()
            return True
        world.to_del.append(this) # Delete


            

collide = tutorial_move_enemy.collide
def char(this):
    return 'Q'

def color(this):
    return display.CYAN

type = "enemy"

attributes = {      \
    "HP" : 5,       \
    "damage" : 3,   \
    "EXP" : 1,      \
    "del_mov" : 250,\
    "pattern_loc" : 0,\
    # Pattern is ^<>^^>>V<VV<
    "pattern" : [\
        [0, -1],[-1, 0],[1, 0],[0, -1],[0, -1], [1, 0], [1, 0], [0, 1], [-1, 0], [0, 1], [0, 1], [-1, 0]
  ]}
