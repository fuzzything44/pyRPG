from effects import effect

class tough(effect.effect):
    def __init__(this, owner, duration, name = None):
        super().__init__(owner, duration, name, {})
        this._last_HP = owner.attributes["HP"] # Get owner HP


    def tick(this, delta_time):
        super().tick(delta_time)
        if this.owner.attributes["HP"] != this._last_HP:        # If HP changed since last update
            hurt = this._last_HP - this.owner.attributes["HP"]  # Find how much it changed.
            if hurt > 0:                                        # If they actually got hurt (so didn't heal)
                this.owner.attributes["HP"] += hurt / 2         # Heal them half of what they were hit for.
            this._last_HP = this.owner.attributes["HP"]
