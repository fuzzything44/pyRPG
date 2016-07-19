name ="Wizard's hat"
type = "hat"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"] +=2
def on_unequip (this, player):
    player.attributes["maxMP"] -= 2
