import display
from objects import world_object
from items import item

class bread(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Bread", "consumable", 0, quantity, {"icon" : ["   ", "(#)", "   "], "color": display.YELLOW})

    def use(this, owner):
        owner.attributes["HP"] += 5




