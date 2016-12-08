import time

import display
import main_menu
import makemaps
import world
from objects import Player

#makemaps.make_from_file('maps/Multiplayer/start.txt', 'maps/Multiplayer/start.py')

display.start()
main_menu.start()
# Title menu!
# Needs world selection menu. Probably try for a scrolling menu with basic graphics if possible.


# Print world out
world.dispworld()

display.draw_topbar()

display.printc(display.WEAPON_X, display.WEAPON_Y, world.player.attributes["weapon"].name)
display.printc(display.HAT_X, display.HAT_Y, world.player.attributes["hat"].name)
display.printc(display.SHIRT_X, display.SHIRT_Y, world.player.attributes["shirt"].name)
display.printc(display.PANTS_X, display.PANTS_Y, world.player.attributes["pants"].name)
display.printc(display.RING_X, display.RING_Y, world.player.attributes["ring"].name)


world.player.attributes["spell"].draw()
world.player.attributes["consumable"].draw()
start_time = time.time()
since_start = 0
while True: # Main game loop
    try:
        new_map_loaded = False
        # Refresh screen. Draw player first.
        display.printc(world.player.X, world.player.Y + 5, world.player.char(), world.player.color(), world.map[world.player.X][world.player.Y][1])
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

        if display.current_menu is None:
            for i in range(5, display.sidebar_line):
                display.printc(50, i, ' ' * 29)
            display.sidebar_line = 5
        else:
            display.sidebar_line = 24

        # Loop through all objects. Update and redraw all of them.
        for index in range(len(world.objects)):
            obj = world.objects[index]

            # Redraw world tile, unless the object is invisible
            if obj.char() != '\0':
                display.printc(obj.X, obj.Y + 5, world.map[obj.X][obj.Y][2], world.map[obj.X][obj.Y][0])
            # Update it
            if obj.update(delta_time) is not None:
                new_map_loaded = True
            for coll in world.objects:    # Check for collision
                if ((coll.X, coll.Y) == (obj.X, obj.Y)) and (not coll is obj) :
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
                display.printc(obj.X, obj.Y + 5, obj.char(), obj.color(), world.map[obj.X][obj.Y][1])
        if new_map_loaded:
            if display.current_menu is not None:    # End menu on new map load, don't want extra stuff left over.
                display.current_menu.clear()
                display.current_menu = None
            continue
        # Delete objects that need to be deleted.
        for obj in set(world.to_del): # Set to remove duplicates
            # Only print if in bounds
            if not world.out_of_bounds(obj.X, obj.Y):
                display.printc(obj.X, obj.Y + 5, world.map[obj.X][obj.Y][2], world.map[obj.X][obj.Y][0])
            world.objects.remove(obj)
        if display.keyDown(display.CONST.VK_ESCAPE):
            menu = display.menu("Options:", "Resume", "Inventory", "Spells", "Save", "Exit")
            while menu.update() is None: # Blocking operation for main menu
                display.refresh()
            if menu.update() == 1: # Inventory
                Player.player.inventory_menu()
            elif menu.update() == 2: # Spells
                Player.player.set_active("spell")
            elif menu.update() == 3: # Save
                world.save_player()
            elif menu.update() == 4:
                exit(0)
            
            world.player.attributes["spell"].draw()
            world.player.attributes["consumable"].draw()
            if display.current_menu is not None: # Redraw old menu.
                display.current_menu.redraw()
            display.refresh()
    except Exception as ex:
        pass