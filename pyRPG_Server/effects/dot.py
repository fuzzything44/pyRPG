from effects import effect

class dot(effect.effect):
    def __init__(this, owner, duration, dps = 15.0, name = None):
        super().__init__(owner, duration, name)
        this.damage = dps

    def tick(this, delta_time):
        super().tick(delta_time)
        if "HP" in this.owner.attributes:
            this.owner.attributes["HP"] -= this.damage * delta_time / 1000.0