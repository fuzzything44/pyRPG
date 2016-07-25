name = "Okay sword"
type = "weapon"
attributes = { "damage" : 3, "range": 2}
def on_equip (this,player):
    player.attributes["atk_spd"] += 5
def on_unequip (this, player):
    player.attributes["atk_spd"] -= 5


