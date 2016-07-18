name ="Tennis shoes"
type = "shoes"
attributes = {}
def on_equip (this,player):
    player.attributes["maxHP"+2]
def on_unequip (this, player):
    player.attributes["maxHP"-2]
