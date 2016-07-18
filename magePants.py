name ="Mage pants"
type = "pants"
attributes = {}
def on_equip (this,player):
    player.attributes["maxMP"+8, "maxHP"+3]
def on_unequip (this, player):
    player.attributes["maxMP"-8, "maxHP"-3]
