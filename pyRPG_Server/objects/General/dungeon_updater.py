import world

from objects import world_object

class dungeon_updater(world_object.world_object):
    """Object to manage coordination between dungeon instances. Spawned by dungeon_start. 
Does nothing but update world.dungeon_state and block map exit until told to stop."""

    def __init__(this, send, get):
        super().__init__(0, 0, "special")
        this.blocks_map_exit = True
        this.attributes.update({"send_queue" : send, "get_queue" : get, "has_players" : False})

    def update(this, delta_time):
        super().update(delta_time)

        if this.attributes["has_players"] != bool(world.players): # The state of players existing changed, so send that.
            world.dungeon_state_diff[world.world_name + "_has_players"] = bool(world.players)
            this.attributes["has_players"] = bool(world.players)

        # Check for updates
        if not this.attributes["get_queue"].empty():
            upd = this.attributes["get_queue"].get()
            world.dungeon_state.update(upd)

        # Needs to send updates.
        if len(world.dungeon_state_diff) > 0:
            this.attributes["send_queue"].put(world.dungeon_state_diff)
            world.dungeon_state_diff = {}

        if world.dungeon_state["_exit"]: # We should exit now.
            this.blocks_map_exit = False

