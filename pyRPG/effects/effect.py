

class effect():
    """Base class of effects."""
    def __init__(this, owner, duration):
        this.time = duration
        this.owner = owner

    def tick(this, delta_time):
        this.time -= delta_time

    def uneffect(this, owner):
        pass

