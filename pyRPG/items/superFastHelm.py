name ="Super fast helmet"
type = "helmet"
attributes = {}
def on_equip (this,player):
    player.attributes["move_spd"] -= 20
    player.attributes["maxHP"] += 20
def on_unequip (this, player):
    player.attributes["move_spd"] += 20
    player.attributes["maxHP"] -= 20
