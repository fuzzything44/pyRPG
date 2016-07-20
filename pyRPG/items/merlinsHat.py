name ="Merlin's hat"
type = "hat"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"] += 30
    player.attributes["maxHP"] +=20
    player.attributes["magic"] += 20
def on_unequip (this, player):
    player.attributes["maxMP"] -= 30
    player.attributes["maxHP"] -= 20
    player.attributes["magic"] -= 20
