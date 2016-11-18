import display

class effect():
    """Base class of effects."""
    def __init__(this, owner, duration, name = None):
        this.time = duration
        this.owner = owner
        this.name = name

    def tick(this, delta_time):
        this.time -= delta_time
        if this.name is not None and display.sidebar_line < 15: # Only show the first few effects.
            display.printc(51, display.sidebar_line, this.name)
            display.sidebar_line += 1

    def uneffect(this, owner):
        pass

