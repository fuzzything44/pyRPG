import display
import world
from objects import world_object

class node:
    def __init__(this, text, *options):
        """Parameters:
  text: The menu intro text.
  options: A list of (choice_text, node)
"""
        this.text = text
        this.options = options
        this.ret_val = None

    def start_node(this):
        # Create options
        disp_opts = []
        for opt in this.options:
            disp_opts.append(opt[0])
        this.ret_val = None
        display.current_menu = display.menu(this.text, *disp_opts)

    # Calls menu, returns new node or None
    def run_node(this):
        if this.ret_val is not None:
            display.current_menu.clear()
            display.current_menu = None
            return this.options[this.ret_val][1]
        else:
            this.ret_val = display.current_menu.update()


class dialogue_tree:

    def __init__(this):
        this.nodes = {}
        this.exit_nodes = {}
        this.current_node = "start"
        this.paused = True
        this.exit_taken = None

    def add_node(this, name, node):
        this.nodes[name] = node

    def add_exit(this, exit_name, exit_number):
        this.exit_nodes[exit_name] = exit_number

    def run(this):
        if this.exit_taken is not None:
            return this.exit_taken
        if this.paused:
            this.paused = False                         # Unpause
            this.nodes[this.current_node].start_node()  # Redraw node
        else:
            new_node = this.nodes[this.current_node].run_node()
            if new_node is not None:                            # Menu finished
                if new_node in this.exit_nodes:                 # Menu ended
                    this.exit_taken = this.exit_nodes[new_node] # Exit
                    return this.exit_taken
                else:
                    this.current_node = new_node                # Go to new node
                    this.nodes[this.current_node].start_node()

    def pause(this):
        display.current_menu.clear()
        display.current_menu = None 
        this.paused = True
    
    def reset(this):
        this.current_node = "start"
        this.paused = True
        this.exit_taken = None


class npc(world_object.world_object):
    """Talks to the player.""" #TODO: add a good interface for complex dialog trees.
    def __init__(this, posX, posY, dialogue):
        super().__init__(posX, posY, "interactable")
        this.attributes.update({        \
            "dialogue" : dialogue,      \
            "talking" : False,          \
            "needs_reset" : False       \
          })

    def update(this, delta_time):
        "Talks to player if they're standing next to it."
        if world.player.X + 1 >= this.X and world.player.X - 1 <= this.X and world.player.Y + 1 >= this.Y and world.player.Y -1 <= this.Y:
            this.attributes["talking"] = True
            if this.attributes["dialogue"].run() is not None:
                this.attributes["needs_reset"] = True
        else:
            if this.attributes["needs_reset"]:
                this.attributes["needs_reset"] = False
                this.attributes["dialogue"].reset()
            if this.attributes["talking"]:
                this.attributes["talking"] = False
                this.attributes["dialogue"].pause()


        if ("HP" in this.attributes) and (this.attributes["HP"] <= 0):
            world.to_del.append(this)
    
    def color(this):
        "Returns green"
        return display.GREEN
    
    def char(this):
        return 'T'
    

