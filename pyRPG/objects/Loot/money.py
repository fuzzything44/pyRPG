import display
import world

from objects import world_object

class money(world_object.world_object):
    def __init__(this, posX, posY, value):
        super().__init__(posX, posY, "money")
        this.attributes.update({
            "value" : value,
            "taken" : False
          })

    def collide(this, obj):
        if ("money" in obj.attributes) and (not this.attributes["taken"]):
            obj.attributes["money"] += this.attributes["value"]
            this.attributes["taken"] = True
            world.to_del.append(this)
    
    def color(this):
        return display.YELLOW
    
    def char(this):
        return '$'

