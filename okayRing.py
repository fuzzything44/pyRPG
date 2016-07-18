name ="okay ring"
type = "ring"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"+8]
def on_unequip (this, player):
    player.attributes["maxHP"-8]
