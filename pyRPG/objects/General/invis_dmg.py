from effects import fire

def update(this, delta_time):
    to_del = []
    for index in this.attributes["timers"]:
        this.attributes["timers"][index] -= delta_time
        if this.attributes["timers"][index] <= 0:
            to_del.append(index)
    for index in to_del:
        del this.attributes["timers"][index]

# Since various sources of damage may do different effects, we need a new collide for each effect       
def fire_collide(this, oth):
    if not (oth in this.attributes["timers"]):
        if "HP" in oth.attributes:
            oth.attributes["HP"] -= 10              # Hurt it
            this.attributes["timers"][oth] = 100    # Give invincibility
            if "effects" in oth.attributes:
                oth.attributes["effects"]["fire"] = [fire.fire, lambda x: 0, 1000] # Start fire damage


def char(this):
    return '\0' # Invisible!

def color(this):
    return 0    # Invisible!

type = "damage"

attributes = { "timers" : {}}