from effects import effect

class slow(effect.effect):
    def __init__(this, owner, duration, intensity = 25, name = "Slow"):
        super().__init__(owner, duration, name)
        this.intensity = intensity
        owner.attributes["mov_spd"] -= this.intensity


    def uneffect(this, owner):
        owner.attributes["mov_spd"] += this.intensity
