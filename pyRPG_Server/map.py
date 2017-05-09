import time
import traceback

import world
import setuptools

import json as JSON


def handle_messages(map_name, pipe):
    # Check queue for new messages.
    if pipe.poll():
        message = pipe.recv()
        if message[0] == "add": # We're adding a player
            if message[1].type == "player":
                message[1].attributes["sidebar"] = ""
                message[1].attributes["current_menu"] = None # Clear menu if it somehow kept through this...
                message[1].attributes["pipe"].send(world.send_data)
                world.players.append(message[1])
                print("[" + map_name + "] Player", message[1].attributes["name"], "added to map")
            else:
                world.objects.append(message[1])
        if message[0] == "end": # Forcibly end map
            print("[" + map_name + "] Map forcibly ended.")
            return True
    return False

# Runs the map with the given name and given queues
def run_map(map_name, pipe):
    try:
        world.load(map_name.split(';')[0]) # Only load everything before first ;

        print("[" + map_name + "] Map started")
        start_time = time.clock()
        since_start = 0

        time_until_messages = 0 # How many ms before we send out messages again. Let's not overload the client
        # We handle messages before entering the loop to avoid a race condition as
        #  the map is started before any message is sent (as not to overflow pipe's buffer)
        handle_messages(map_name, pipe)
        while True:
            # Calculate delta time
            delta_time = int((time.clock() - start_time) * 1000) - since_start
            if delta_time > 100:
                print("Capped tick at", delta_time, "ms.", len(world.objects) + len(world.players), "objects total")
                delta_time = 100
            delta_time = max(0, delta_time) # Don't have ticks with negative time!
            since_start += delta_time
            time_until_messages -= delta_time
            print(delta_time, " ", end="\r")

            if handle_messages(map_name, pipe):
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

            if time_until_messages <= 0:
                # Send data to players.
                send_data = {"type" : "update", "tiles" : []}

                for obj in world.objects + world.players:
                    send_data["tiles"].append({"color" : obj.color(), "chr" : obj.char(), "x": obj.X, "y": obj.Y})

                # Send update to all players
                for plr in world.players:
                    if plr.attributes["using_inv"]:
                        pass # TODO: what now?
                    else:
                        plr.attributes["pipe"].send(JSON.dumps(send_data))
                    plr.send_extra_data()
                time_until_messages = 16 # Reset time

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
