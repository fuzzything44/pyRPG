name ="Fast pants"
type = "pants"
attributes = {}
def on_equip (this,player):
    player.attributes["mov_spd"] -= 5
    player.attributes["atk_spd"] -= 2
    player.attributes["maxHP"] += 4
def on_unequip (this, player):
    player.attributes["mov_spd"] += 5
    player.attributes["atk_spd"] += 2
    player.attributes["maxHP"] -= 4
