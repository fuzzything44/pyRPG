
name ="fast shirt"
type = "shirt"
attributes = {}
def on_equip (this,player):
    player.attributes["mov_spd"] -= 6
    player.attributes["atk_spd"] -= 3
    player.attributes["maxHP"] += 5
def on_unequip (this, player):
    player.attributes["mov_spd"] += 6
    player.attributes["atk_spd"] += 3
    player.attributes["maxHP"] -= 5