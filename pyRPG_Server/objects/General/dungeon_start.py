import multiprocessing

import world

from objects import world_object

from objects.General import dungeon_updater

class dungeon_start(world_object.world_object):
    """Coordinates maps in a dungeon. When spawned, creates rest of dungeon maps and updates dungeon state."""

    def __init__(this, map_names, state):
        """Arguments:
  map_names: list of strings, names of the rest of the maps in the dungeon.
  state: dictionary to set world.dungeon_state to upon map load.
"""
        super().__init__(0, 0, "special")
        this.blocks_map_exit = True
        for name in map_names:   # Have tracking for if each map has players.
            state[name + "_has_players"] = False
        state["_exit"] = False
        this.attributes.update({"maps" : map_names, "state" : state, "setup_done" : False, "get_queues" : {}, "send_queues" : {}, "timeout" : 0})

    def update(this, delta_time):
        if not this.attributes["setup_done"]: # Map is newly created!
            # TODO: spawn rest of maps with dungeon_updaters
            for name in this.attributes["maps"]:
                mger = multiprocessing.Manager()
                get_q  = mger.Queue()
                send_q = mger.Queue()
                this.attributes["get_queues"][name] = get_q
                this.attributes["send_queues"][name] = send_q
                send_q.put(this.attributes["state"])
                linked_updater = dungeon_updater.dungeon_updater(get_q, send_q)
                # Send it to map;extra_stuff_on_this_world
                # So if this map is named dungeon_start;player_name;other_player,
                # It creates a map named map_name;player_name;other_player, not just named map_name
                extra_data = world.world_name.split(';', 1)
                if len(extra_data) > 1:
                    world.move_requests.append((name + extra_data[1], linked_updater))
                else:
                    world.move_requests.append((name, linked_updater))
            world.dungeon_state = this.attributes["state"]
            this.attributes["setup_done"] = True

        # Check for updates.
        diff = {}
        for map_name in this.attributes["get_queues"]: # For each map in dungeon...
            if not this.attributes["get_queues"][map_name].empty(): # See if it changed global stuff.
                state_upd = this.attributes["get_queues"][map_name].get() 
                for change in state_upd:
                    diff[change] = state_upd[change]                   # If so, add that to list of changes.

        diff.update(world.dungeon_state_diff)
        world.dungeon_state_diff = {}

        if len(diff) > 0: # If we had changes...
            for map_name in this.attributes["send_queues"]: # Send those changes to each map.
                this.attributes["send_queues"][map_name].put(diff)

        for change in diff: # And update starting map's world with the difference.
            world.dungeon_state[change] = diff[change]

        has_players = False
        for name in this.attributes["maps"]:
            if world.dungeon_state[name + "_has_players"]:
                has_players = True
        if world.players:
            has_players = True
        if has_players:
            this.attributes["timeout"] = 0
        else:
            this.attributes["timeout"] += delta_time
            if this.attributes["timeout"] > 1000: # Timed out. No players left in dungeon.
                for map_name in this.attributes["send_queues"]: # Tell all maps to exit.
                    print("sending exit signal")
                    this.attributes["send_queues"][map_name].put({"_exit" : True})
                this.blocks_map_exit = False # Stop blocking exit.



