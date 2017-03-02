import display
import world

from objects import world_object

TEAM_NONE   = 0
TEAM_PLAYER = 1 # Same as 1 << 0
TEAM_ENEMY  = 2 # Same as 1 << 1

def get_team(obj):
    if "team" in obj.attributes:
        return obj.attributes["team"]
    elif obj.type == "player":
        return TEAM_PLAYER
    elif obj.type == "enemy":
        return TEAM_ENEMY
    else:
        return TEAM_NONE

class base_attack(world_object.world_object):
    """ Basic attack. Just can collide to do damage, has a display color."""
    def __init__(this, posX, posY, damage, owner, team = None):
        """Parameters:
            posX: The X position of the attack.
            posY: The Y position of the attack.
            damage: How much damage the attack does.
            owner: The object that spawned the attack.
"""
        super().__init__(posX, posY, "damage")
        if team is None:
            team = get_team(owner)
        this.attributes.update({    \
            "damage" : damage,      \
            "owner" : owner,        \
            "team" : team           \
          })
    
    def collide(this, oth):
        "Checks if collided object is of a different team than it. If so, does damage and gets destroyed."

        # Using bitwise and here. So if no teams match then it damages.
        if not (this.attributes["team"] & get_team(oth)) and ("HP" in oth.attributes):
            oth.attributes["HP"] -= this.attributes["damage"]
            if "dmg_dist" in oth.attributes: # Add damage to damage distribution
                if this.attributes["owner"] in oth.attributes["dmg_dist"]:
                    oth.attributes["dmg_dist"][this.attributes["owner"]] += this.attributes["damage"]
                else:
                    oth.attributes["dmg_dist"][this.attributes["owner"]]  = this.attributes["damage"]

            world.to_del.append(this)

    def char(this):
        "Always a '!'"
        return '!'
    
    def color(this):
        "Returns magenta"
        return display.MAGENTA
    