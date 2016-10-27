from effects import effect

class regen(effect.effect):
    def tick(this, delta_time):
        super().tick(delta_time)
        if ("HP" in this.owner.attributes) and ("maxHP" in this.owner.attributes):
            this.owner.attributes["HP"] += 1.0 * this.owner.attributes["magic"] * delta_time / 1000
            if this.owner.attributes["HP"] > this.owner.attributes["maxHP"]:
                this.owner.attributes["HP"] = this.owner.attributes["maxHP"]
    