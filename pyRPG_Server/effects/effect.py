import display

class effect():
    """Base class of effects."""
    def __init__(this, owner, duration, name = None, stat_mods = {}):
        this.time = duration
        this.owner = owner
        this.name = name
        this.stat_change = stat_mods
        for mod in stat_mods:
            owner.attributes[mod] += stat_mods[mod]

    def tick(this, delta_time):
        this.time -= delta_time
        if this.owner.type == "player" and this.name is not None and this.owner.attributes["sidebar"].count('\n') <= 7: # Only show the first few effects.
            time_left = "Inf"
            if this.time < float("inf"):
                time_left = str(int(this.time/1000))
            this.owner.attributes["sidebar"] += " " + this.name + '(' + time_left + ")\n"

    def uneffect(this, owner):
        for mod in this.stat_change:
            owner.attributes[mod] -= this.stat_change[mod]

