name ="running shoes"
type = "shoes"
attributes = {}
def on_equip (this,player):
    player.attributes["move_spd"] += 5
def on_unequip (this, player):
    player.attributes["move_spd"] -= 5
