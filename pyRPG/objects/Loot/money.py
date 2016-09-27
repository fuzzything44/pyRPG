import display
import world

def money_update(this, delta_time):
    pass

def money_collide(this, obj):
    if ("money" in obj.attributes) and (not this.attributes["taken"]):
        obj.attributes["money"] += this.attributes["value"]
        this.attributes["taken"] = True
        world.to_del.append(this)

def money_color(this):
    return display.YELLOW

def money_char(this):
    return '$'


money_type = "money"

money_attributes = {
    "value": 5,
    "taken" : False,
}