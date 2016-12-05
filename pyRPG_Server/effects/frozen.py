from effects import effect

class frozen(effect.effect):
    def tick(owner, delta_time):
        if "stuckX" in obj.attributes:
            obj.X = obj.attributes["stuckX"]
        else:
            obj.attributes["stuckX"] = obj.X
        if "stuckY" in obj.attributes:
            obj.Y = obj.attributes["stuckY"]
        else:
            obj.attributes["stuckY"] = obj.Y

    def uneffect(this, owner):
        del owner.attributes["stuckX"]
        del owner.attributes["stuckY"]
