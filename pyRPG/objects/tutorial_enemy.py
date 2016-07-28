import display
import world

from objects import world_object

def update(this, delta_time):
    if this.attributes["HP"] <= 0:
        world.to_del.append(this) # Delete
        world.player.attributes["gainexp"](world.player, this.attributes["EXP"]) # Give exp
        # Tell them they get a new spell
        display.printc(5, 5, "^")
        display.printc(0, 6, "Experience and level")
        display.printc(display.SPELL_BOX_START + 2, 5, "^")
        display.printc(display.SPELL_BOX_START - 2, 6, "Current spell")
        display.printc(0, 9, "You leveled up and got a new spell!")
        display.printc(0, 10, "Press ESC to open the menu and set your spell!")
        display.printc(0, 11, "Once set, you can cast your spell with SPACE")
        display.refresh()
        


# Deals some damage...
def collide(this, oth):
    if "HP" in oth.attributes:
        oth.attributes["HP"] -= this.attributes["damage"]
        oth.X -= 3 # Bounce back other a bit

def char(this):
    return 'Q'

def color(this):
    return display.CYAN

type = "enemy"
attributes = {      \
    "HP" : 1,       \
    "damage" : 1,   \
    "EXP" : 1       \
  }