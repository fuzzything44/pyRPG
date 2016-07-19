
name ="fast shirt"
type = "shirt"
attributes = {}
def on_equip (this,player):
    player.attributes["move_spd"] += 4
    player.attributes["maxHP"] += 5
def on_unequip (this, player):
    player.attributes["move_spd"] -= 4
    player.attributes["maxHP"] -= 5