import effects.fire as fire

def invis_dmg_update(this, delta_time):
    try:
        for index in this.attributes["timers"]:
            this.attributes["timers"][index] -= delta_time
            if this.attributes["timers"][index] <= 0:
                del this.attributes["timers"][index]
    except:
        this.attributes["timers"] = {}   # Give it timers

# Since various sources of damage may do different effects, we need a new collide for each effect       
def invis_fire_dmg_collide(this, oth):
    if not (oth in this.attributes["timers"]):
        try:
            oth.attributes["HP"] -= 10              # Hurt it
            this.attributes["timers"][oth] = 100    # Give invincibility
            oth.attributes["effects"]["fire"] = [fire.fire, 1000] # Start fire damage
        except:
            pass # Object did not have HP

def invis_dmg_char(this):
    return '\0' # Invisible!

def invis_dmg_color(this):
    return 0    # Invisible!