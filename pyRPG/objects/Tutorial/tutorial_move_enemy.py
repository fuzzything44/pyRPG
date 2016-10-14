import display
import world

from objects.General import enemy_base

class move_enemy(enemy_base.enemy_base):
    # Pattern is ^^^^^>>>>>VVVVV<<<<<
    def __init__(this, posX, posY, health = 5, damage = 3, exp = 1, pattern_loc = 0):
        super().__init__(posX, posY, health, damage, exp)
        this.attributes["del_mov"] = 200
        this.attributes["pattern_loc"] = pattern_loc
        this.pattern = [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0]]

    def update(this, delta_time):
        this.attributes["del_mov"] -= delta_time
        if this.attributes["del_mov"] <= 0: # If they can move
            this.attributes["del_mov"] = 250 # Wait to move again
    
            # Move depending on where we are in the pattern.
            this.X += this.pattern[this.attributes["pattern_loc"]][0]
            this.Y += this.pattern[this.attributes["pattern_loc"]][1]
            # Go to the next step of the pattern
            this.attributes["pattern_loc"] += 1
            # Restart pattern if needed.
            if this.attributes["pattern_loc"] >= len(this.pattern):
                this.attributes["pattern_loc"] = 0
        super().update(delta_time)
    
    # Deals some damage...
    def collide(this, oth):
        if "HP" in oth.attributes:
            oth.attributes["HP"] -= this.attributes["damage"]
            # Bounce other back opposite of pattern.
            oth.X -= this.pattern[this.attributes["pattern_loc"]][0]
            oth.Y -= this.pattern[this.attributes["pattern_loc"]][1]

