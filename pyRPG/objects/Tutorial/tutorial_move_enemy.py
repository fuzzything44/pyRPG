import display
import world

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
        world.to_del.append(this) # Delete
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give exp

# Deals some damage...
def collide(this, oth):
    if "HP" in oth.attributes:
        oth.attributes["HP"] -= this.attributes["damage"]
        # Bounce other back opposite of pattern.
        oth.X -= this.attributes["pattern"][this.attributes["pattern_loc"]][0]
        oth.Y -= this.attributes["pattern"][this.attributes["pattern_loc"]][1]

def char(this):
    return 'Q'

def color(this):
    return display.CYAN

type = "enemy"
attributes = {      \
    "HP" : 5,       \
    "damage" : 1,   \
    "EXP" : 1,      \
    "del_mov" : 200,\
    "pattern_loc" : 0,\
    # Pattern is ^^^^^>>>>>VVVVV<<<<<
    "pattern": [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0]]\
  }