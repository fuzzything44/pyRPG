import display
import world

def update(this, delta_time):
    pass

def collide(this, other):
    if other.type == "player":
        world.load(this.attributes["newmap"])
        world.objects = [world.player] + world.objects

        world.player.X = this.attributes["locx"]
        world.player.Y = this.attributes["locy"]
        this.attributes["used"] = True
        # Print world out
        for x in range(world.WORLD_X):
            for y in range(world.WORLD_Y):
                display.printc(x, y + 5, world.map[x][y][1], world.map[x][y][0])
    return True

def char(this):
    if not this.attributes["used"]:
        return 'O'
    return '\0'

def color(this):
    return display.CYAN
type = "portal"

# \ contiunes the line
attributes = {      \
    "newmap" : "",  \
    "locx" : 0,     \
    "locy" : 10,    \
    "used" : False  \
}   


