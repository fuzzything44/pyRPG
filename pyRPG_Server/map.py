import time
import traceback

import world
import setuptools

# Runs the map with the given name and given queues
def run_map(map_name, get, send):
    try:
        world.load(map_name.split(';')[0]) # Only load everything before first ;
    
        print("[" + map_name + "] Map started")
        start_time = time.clock()
        since_start = 0
    
        loop_count = 0
        while True:
            loop_count += 1
            # Calculate delta time
            delta_time = int((time.clock() - start_time) * 1000) - since_start
            if delta_time > 100:
                print("Capped tick at", delta_time, "ms.", len(world.objects) + len(world.players), "objects total")
                delta_time = 100
            delta_time = max(0, delta_time) # Don't have ticks with negative time!
            since_start += delta_time

            print(delta_time, " ", end="\r")

            # Check queue for new messages.
            if not get.empty():
                message = get.get()

                if message[0] == "add": # We're adding a player
                    if message[1].type == "player":
                        message[1].attributes["pipe"].send("help me why is this failing".encode("utf-8"))#bytearray([1]) + world.send_data) # Send map data
                        message[1].attributes["sidebar"] = ""
                        message[1].attributes["current_menu"] = None # Clear menu if it somehow kept through this...
                        world.players.append(message[1])
                        print("[" + map_name + "] Player added to map", message[1].attributes["name"])
                    else:
                        world.objects.append(message[1])
                if message[0] == "end": # Forcibly end map
                    print("[" + map_name + "] Map forcibly ended.")
                    for plr in world.players:
                        plr.attributes["socket"].close()
                    return
    
            world.to_del.clear()
            world.to_del_plr.clear()
    
            continue_loop = False
            # Update objects
            obj_update_list = world.players + world.objects

            
            for index in range(len(obj_update_list)):
                obj = obj_update_list[index]
    
                # Update it
                obj.update(delta_time)

                if obj.type != "player": # Don't check player collisions as they can only collide with other players.
                    for coll in obj_update_list[:index]:    # Check for collision
                        if coll.X == obj.X and coll.Y == obj.Y:
                            obj.collide(coll) # Call collisions
                            coll.collide(obj)
    
                #Check if out of bounds
                if world.out_of_bounds(obj.X, obj.Y):
                    world.to_del.append(obj)

                if obj.blocks_map_exit:
                    continue_loop = True

            # Delete objects that need to be deleted.
            for obj in set(world.to_del): # Set to remove duplicates
                world.objects.remove(obj)

    
            # Remove players that left
            for plr in set(world.to_del_plr):
                world.save_player(plr)
                world.players.remove(plr)
    
            # Handle move requests.
            for req in world.move_requests:
                send.put(("mov", req)) # Send request
            world.move_requests.clear()

            # Send data to players.
            # Start with map data - either a 0 byte or a 1 byte with map len and map after.
            # We need (#objects + # players) things to send.
            # Each thing needs an X coord, Y coord, char, and color
            # We devote 1 byte to each, meaning each is 4 bytes
            send_data = bytearray(1)

            if len(world.objects) > 200:
                send_data[0] = 200 + len(world.players)
                for index in range(201):
                    obj = world.objects[index]
                    send_data += bytearray([obj.X, obj.Y])
                    send_data += bytearray(obj.char(), 'utf-8')
                    send_data += bytearray([obj.color()])
            else:
                send_data[0] = len(world.objects) + len(world.players)
                for obj in world.objects + world.players: # Loop through objects, get data.
                    send_data += bytearray([obj.X, obj.Y])
                    send_data += bytearray(obj.char(), 'utf-8')
                    send_data += bytearray([obj.color()])
    
            # Send update to all players
            for plr in world.players:
                if plr.attributes["using_inv"]:
                    pass # TODO: what now?
                else:
                    plr.attributes["pipe"].send(bytes(send_data + plr.extra_data()))
                
            if not continue_loop: # Nothing blocking.
                send.put(("end", ))
                print("[" + map_name + "] Ending map")
                while get.get() != ("end",): # Wait for acknowledge of end.
                    pass
                return


    except Exception as ex:
        send.put(("end", ))
        print("[" + map_name + "] Ending map due to error!")
        print("[" + map_name + "]", traceback.format_exc())
        while get.get() != ("end",): # Wait for acknowledge of end.
            pass
        return


    
