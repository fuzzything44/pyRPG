import time

import display
import main_menu
import world
from objects import chest
from objects import enemy
from objects import invis_dmg
from objects import player
from objects import portal
from objects import world_object

# Temporary imports to refresh maps each time we run it.
import start 
import tut1
import tutboss
import town
import end
import stonstart
import credits

# World generation
try:
    start.generate()
    world.objects = [world.player] + world.objects
    world.save("start")
except Exception as ex:
    pass
try:
    tut1.generate()
    world.objects = [world.player] + world.objects
    world.save("tut1")
except Exception as ex:
    pass
try:
    tutboss.generate()
    world.objects = [world.player] + world.objects
    world.save("tutboss")
except Exception as ex:
    pass
try:
    town.generate()
    world.objects = [world.player] + world.objects
    world.save("town")
except Exception as ex:
    pass
try:
    end.generate()
    world.objects = [world.player] + world.objects
    world.save("end")
except Exception as ex:
    pass
try:
    stonstart.generate()
    world.objects = [world.player] + world.objects
    world.save("stonstart")
except Exception as ex:
    pass
try:
    credits.generate()
    world.objects = [world.player] + world.objects
    world.save("credits")
except Exception as ex:
    pass


display.start()
main_menu.start()
# Title menu!
# Needs world selection menu. Probably try for a scrolling menu with basic graphics if possible.


world.objects = [world.player] + world.objects

# Print world out
for x in range(world.WORLD_X):
    for y in range(world.WORLD_Y):
        display.printc(x, y + 5, world.map[x][y][1], world.map[x][y][0])

# Print top pane
display.printc(5, 0, "HP:")
display.printc(5, 1, "MP:")
display.printc(5, 2, "Gold:")
display.printc(5, 3, "Level")

# Current spell and item border
display.printc(display.SPELL_BOX_START, 0, "+++++ +++++   Weapon:")
display.printc(display.SPELL_BOX_START, 1, "+   + +   +   Hat:")
display.printc(display.SPELL_BOX_START, 2, "+   + +   +   Shirt:")
display.printc(display.SPELL_BOX_START, 3, "+   + +   +   Pants:")
display.printc(display.SPELL_BOX_START, 4, "+++++ +++++   Ring:")


start_time = time.time()
since_start = 0
while True: # Main game loop
    # Refresh screen
    display.refresh()

    delta_time = int((time.time() - start_time) * 1000) - since_start
    since_start += delta_time
    if delta_time > 100:
        delta_time = 100
        # TODO: Give a speed warning if this happens too often...
    display.printc(0,0, str(delta_time) + ' ')
    # Loop through all objects. Update and redraw all of them.
    for index in range(len(world.objects)):
        try:
            obj = world.objects[index]
        except: # List size decreased because of a world load.
            break
        # Redraw world tile, unless the object is invisible
        if obj.getChar() != '\0':
            display.printc(obj.getCoords()[0], obj.getCoords()[1] + 5, world.map[obj.getCoords()[0]][obj.getCoords()[1]][1], world.map[obj.getCoords()[0]][obj.getCoords()[1]][0])
        # Update it
        obj.update(delta_time)
        for coll in world.objects:    # Check for collision
            if (coll.getCoords() == obj.getCoords()) and (not coll is obj) :
                obj.collide(coll)

        #Check if out of bounds
        if (obj.getCoords()[0] >= world.WORLD_X) or (obj.getCoords()[0] < 0) or (obj.getCoords()[1] >= world.WORLD_Y) or (obj.getCoords()[1] < 0):
            world.to_del.append(obj)
        else:
            # And now redraw it
            display.printc(obj.getCoords()[0], obj.getCoords()[1] + 5, obj.getChar(), obj.getColor())
    # Delete objects that need to be deleted.
    for obj in world.to_del:
        try:
            # Don't print too high!
            if (obj.Y < 0):
                obj.Y = 0
            display.printc(obj.X, obj.Y + 5, world.map[obj.X][obj.Y][1], world.map[obj.X][obj.Y][0])
        except: # Deleted for being out of bounds.
            pass
        try:
            world.objects.remove(obj)
        except ValueError:
            pass # Been put in list multiple times.
    world.to_del.clear()
    if display.keyDown(display.CONST.VK_ESCAPE):
        while display.menu("Options:", [[], [], ["spell"], [], []], ["Resume", lambda: 0], ["Inventory", player.inventory_menu], ["Spells", player.set_active], ["Save", world.save_player], ["Exit", display.end]):
            world.player.attributes["spell"].draw()
            try:
                world.player.attributes["consumable"].draw()
            except:
                pass
            display.refresh()
        