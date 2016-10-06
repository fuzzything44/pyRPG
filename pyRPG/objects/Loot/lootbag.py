import display
import world

from objects.Loot import chest

def update(this, delta_time):
    if len(this.attributes["contents"]) == 0:
        world.to_del.append(this)

def collide(this, oth):
    if (oth.type == "player") and display.keyDown(ord('E')):
        chest._chest_remove(this)

def char(this):
    return 'L'

def color(this):
    return display.YELLOW

type = "container"

attributes = { "contents" : [] }