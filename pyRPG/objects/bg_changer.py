import display
import world

def update(this, delta_time):
    plr_class = world.player.attributes["class"]    # Get player class
    if plr_class in this.attributes["class"]:       # If they are an acceptable class...
        world.map[this.X][this.Y] = this.attributes["replace"] #... then change the world tile this is on to something else.
    world.to_del.append(this) # Delete this. It's job is done.
def collide(this, oth):
    pass

def color(this):
    return display.WHITE

def char(this):
    return '\0'

type = "special"

attributes = {\
    "class" : "warrior mage thief", \
    "replace" : world.WORLD_NOTHING \
  }
