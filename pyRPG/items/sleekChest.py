name ="Sleek chest piece"
type = "shirt"
attributes = {}
def on_equip (this,player):
    player.attributes["move_spd"] -=30
    player.attributes["maxHP"] += 30
def on_unequip (this, player):
    player.attributes["move_spd"] += 30
    player.attributes["maxHP"] -= 30
