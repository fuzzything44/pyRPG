import display
import world

def update(this, delta_time):
    pass

def collide(this, obj):
    if ("money" in obj.attributes) and (not this.attributes["taken"]):
        obj.attributes["money"] += this.attributes["value"]
        this.attributes["taken"] = True
        world.to_del.append(this)

def color(this):
    return display.YELLOW

def char(this):
    return '$'


type = "money"

attributes = {
    "value": 5,
    "taken" : False,
}