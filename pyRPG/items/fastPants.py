name ="Fast pants"
type = "pants"
attributes = {}
def on_equip (this,player):
    player.attributes["mov_spd"] -= 4
    player.attributes["maxHP"] += 5
def on_unequip (this, player):
    player.attributes["mov_spd"] += 4
    player.attributes["maxHP"] -= 5
