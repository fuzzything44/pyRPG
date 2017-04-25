import display
from objects import world_object
from items import item

class bread(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Bread", "consumable", 0, "Restores 5 HP", quantity, {"icon" : "\\fy   \n(#)\n   "})

    def use(this, owner):
        owner.attributes["HP"] += 5




