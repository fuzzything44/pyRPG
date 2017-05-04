import time
import traceback

import world
import setuptools

# Runs the map with the given name and given queues
def run_map(map_name, pipe):
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
            if pipe.poll():
                message = pipe.recv()

                if message[0] == "add": # We're adding a player
                    if message[1].type == "player":
                        message[1].attributes["sidebar"] = ""
                        message[1].attributes["current_menu"] = None # Clear menu if it somehow kept through this...
                        print(message[1].attributes["pipe"])
                        while message[1].attributes["pipe"].poll():
                            print(message[1].attributes["pipe"].recv())
                        message[1].attributes["pipe"].send(world.send_data)
                        print("Sent data")
                        world.players.append(message[1])
                        print("[" + map_name + "] Player added to map", message[1].attributes["name"])
                    else:
                        world.objects.append(message[1])
                if message[0] == "end": # Forcibly end map
                    print("[" + map_name + "] Map forcibly ended.")
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
                pipe.send(("mov", req)) # Send request
            world.move_requests.clear()

            # Send data to players.
            # Start with map data - either a 0 byte or a 1 byte with map len and map after.
            # We need (#objects + # players) things to send.
            # Each thing needs an X coord, Y coord, char, and color
            # We devote 1 byte to each, meaning each is 4 bytes

            # TODO: Pretty much all of this needs rewriting.
            send_data = {"type" : "update", "tiles" : []}

            for obj in world.objects + world.players:
                send_data["tiles"].append({"color" : obj.color(), "chr" : obj.char(), "x": obj.X, "y": obj.Y})

            # Send update to all players
            for plr in world.players:
                if plr.attributes["using_inv"]:
                    pass # TODO: what now?
                else:
                    plr.attributes["pipe"].send(JSON.dumps(send_data))

            if not continue_loop: # Nothing blocking.
                pipe.send(("end", ))
                print("[" + map_name + "] Ending map")
                while pipe.recv() != ("end",): # Wait for acknowledge of end.
                    pass
                return


    except Exception as ex:
        pipe.send(("end", ))
        print("[" + map_name + "] Ending map due to error!")
        print("[" + map_name + "]", traceback.format_exc())
        while pipe.recv() != ("end",): # Wait for acknowledge of end.
            pass
        return
