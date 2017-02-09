import display
import world
from objects import world_object
import copy

class node:
    def __init__(this, text, *options):
        """Parameters:
  text: The menu intro text.
  options: A list of (choice_text, node)
"""
        this.text = text
        this.options = options
        this.ret_val = None

    def start_node(this, player):
        # Create options
        disp_opts = []
        for opt in this.options:
            disp_opts.append(opt[0])
        this.ret_val = None
        player.attributes["current_menu"] = display.menu(this.text, player, *disp_opts)

    # Calls menu, returns new node or None
    def run_node(this, player):
        if this.ret_val is not None:
            player.attributes["current_menu"] = None
            return this.options[this.ret_val][1]
        else:
            this.ret_val = player.attributes["current_menu"].update()

class exit_node:
    def __init__(this, val, func, *args):
        this.exit_number = val
        this._exit_func = func
        this._args = args

    def run_exit(this, plr):
        this._exit_func(plr, *this._args)

class dialogue_tree:

    def __init__(this):
        this.nodes = {}
        this.exit_nodes = {}
        this.current_node = "start"
        this.linked_player = None
        this.paused = True
        this.exit_taken = None

    def add_node(this, name, node):
        this.nodes[name] = node

    def add_exit(this, exit_name, exit_number, on_exit = world_object.no_func, *on_exit_args):
        this.exit_nodes[exit_name] = exit_node(exit_number, on_exit, *on_exit_args)

    def run(this):
        if this.exit_taken is not None:
            return this.exit_taken.exit_number
        if this.paused:
            this.paused = False                                             # Unpause
            this.nodes[this.current_node].start_node(this.linked_player)    # Redraw node
        else:
            new_node = this.nodes[this.current_node].run_node(this.linked_player)
            if new_node is not None:                            # Menu finished
                if new_node in this.exit_nodes:                 # Menu ended
                    this.exit_taken = this.exit_nodes[new_node] # Exit
                    this.exit_taken.run_exit(this.linked_player)
                    return this.exit_taken.exit_number
                else:
                    this.current_node = new_node                # Go to new node
                    this.nodes[this.current_node].start_node(this.linked_player)


class npc(world_object.world_object):
    """Talks to the player.""" #TODO: add a good interface for complex dialog trees.
    def __init__(this, posX, posY, dialogue):
        super().__init__(posX, posY, "interactable")
        this.attributes.update({        \
            "dialogue" : dialogue,      \
            "talking_players" : {}      \
          })

    def update(this, delta_time):
        "Talks to player if they're standing next to it."
        for plr in world.players:
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                if plr not in this.attributes["talking_players"]: # Not talking to them already
                    diag = copy.copy(this.attributes["dialogue"])
                    diag.linked_player = plr
                    this.attributes["talking_players"][plr] = diag

        left_players = []
        for plr, diag in this.attributes["talking_players"].items(): 
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y and plr in world.players:
                diag.run()
            else:
                left_players.append(plr)

        for gone in left_players:
            del this.attributes["talking_players"][gone]
            gone.attributes["current_menu"] = None

        if ("HP" in this.attributes) and (this.attributes["HP"] <= 0):
            world.to_del.append(this)
    
    def color(this):
        "Returns green"
        return display.GREEN
    
    def char(this):
        return 'T'
    

