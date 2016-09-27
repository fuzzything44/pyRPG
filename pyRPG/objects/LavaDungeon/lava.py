import world
import display

from effects import fire
from objects import world_object
def update(this, delta_time):
    to_del = []
    this.attributes["delay_lava"] -= delta_time
    this.attributes["delay_coals"] -= delta_time

    # Check if the player is on a lava tile. Lava character is a #
    if (world.map[world.player.X][world.player.Y][2] == '#') and (this.attributes["delay_lava"] <= 0):
        world.player.attributes["HP"] -= world.player.attributes["maxHP"]*.1              # Hurt it
        this.attributes["delay_lava"] = 100    # Give invincibility
        world.player.attributes["effects"]["fire"] = [fire.fire, lambda x: 0, 1000] # Start fire damage

    if (world.map[world.player.X][world.player.Y] == [display.RED, display.BLACK, '.', True]) and (this.attributes["delay_coals"] <= 0):
        world.player.attributes["HP"] -= 1  # Hurt it
        this.attributes["delay_coals"] = 1000    # Give invincibility

      
collide = world_object.no_func

def char(this):
    return '\0' # Invisible!

def color(this):
    return 0    # Invisible!

type = "damage"

attributes = { "delay_lava" : 0, "delay_coals" : 0}