import time

import display
import main_menu
import makemaps
import world
from objects import Player

#makemaps.make_from_file('maps/Tutorial/tut1.txt', 'maps/Tutorial/tut1.py')

makemaps.make("all")

display.start()
main_menu.start()
# Title menu!
# Needs world selection menu. Probably try for a scrolling menu with basic graphics if possible.


world.objects = [world.player] + world.objects

# Print world out
world.dispworld()

# Print top pane
display.printc(5, 0, "HP:")
display.printc(5, 1, "MP:")
display.printc(5, 2, "Gold:")
display.printc(5, 3, "Level")

# Current spell and item border
display.printc(display.SPELL_BOX_START, 0, "+++++ +++++   Weapon:" + world.player.attributes["weapon"].name)
display.printc(display.SPELL_BOX_START, 1, "+   + +   +   Hat:" + world.player.attributes["hat"].name)
display.printc(display.SPELL_BOX_START, 2, "+   + +   +   Shirt:" + world.player.attributes["shirt"].name)
display.printc(display.SPELL_BOX_START, 3, "+   + +   +   Pants:" + world.player.attributes["pants"].name)
display.printc(display.SPELL_BOX_START, 4, "+++++ +++++   Ring:" + world.player.attributes["ring"].name)

world.player.attributes["spell"].draw()
world.player.attributes["consumable"].draw()
start_time = time.time()
since_start = 0
while True: # Main game loop
    try:
        new_map_loaded = False
        # Refresh screen

        display.refresh()
    
        delta_time = int((time.time() - start_time) * 1000) - since_start
        since_start += delta_time
        if delta_time > 100:
            delta_time = 100
            # TODO: Give a speed warning if this happens too often...
        display.printc(0, 0, str(delta_time) + ' ')
        display.printc(0, 1, str(len(world.objects)) + ' ')

        # Clear out deletion list for next update
        world.to_del.clear()

        # Loop through all objects. Update and redraw all of them.
        for index in range(len(world.objects)):
            obj = world.objects[index]

            # Redraw world tile, unless the object is invisible
            if obj.getChar() != '\0':
                display.printc(obj.X, obj.Y + 5, world.map[obj.X][obj.Y][2], world.map[obj.X][obj.Y][0])
            # Update it
            obj.update(delta_time)
            for coll in world.objects:    # Check for collision
                if (coll.getCoords() == obj.getCoords()) and (not coll is obj) :
                    if obj.collide(coll) is not None:
                        new_map_loaded = True
                        break # Stop collide check, new map was loaded
            if new_map_loaded:
                break
            #Check if out of bounds
            if world.out_of_bounds(obj.X, obj.Y):
                world.to_del.append(obj)
            else:
                # And now redraw it
                display.printc(obj.X, obj.Y + 5, obj.getChar(), obj.getColor(), world.map[obj.X][obj.Y][1])
        if new_map_loaded:
            continue
        # Delete objects that need to be deleted.
        for obj in set(world.to_del): # Set to remove duplicates
            # Only print if in bounds
            if not world.out_of_bounds(obj.X, obj.Y):
                display.printc(obj.X, obj.Y + 5, world.map[obj.X][obj.Y][2], world.map[obj.X][obj.Y][0])
            world.objects.remove(obj)
        if display.keyDown(display.CONST.VK_ESCAPE):
            while display.menu("Options:", [[], [], ["spell"], [], []], ["Resume", lambda: 0], ["Inventory", Player.player.inventory_menu], ["Spells", Player.player.set_active], ["Save", world.save_player], ["Exit", display.end]):
                world.player.attributes["spell"].draw()
                world.player.attributes["consumable"].draw()
                display.refresh()
    except Exception as ex:
        pass