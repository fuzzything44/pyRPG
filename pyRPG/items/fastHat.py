name ="fast hat"
type = "hat"
attributes = {}
def on_equip (this,player):
    player.attributes["mov_spd"] -= 2
def on_unequip (this, player):
    player.attributes["mov_spd"] += 2
