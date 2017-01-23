from items import item
from objects import world_object

class no_hat(item.item):
    def __init__(this):
        super().__init__("No hat", "hat", 0, 0, {})

class no_pants(item.item):
    def __init__(this):
        super().__init__("No pants", "pants", 0, 0, {})

class no_ring(item.item):
    def __init__(this):
        super().__init__("No ring", "ring", 0, 0, {})

class no_shirt(item.item):
    def __init__(this):
        super().__init__("No shirt", "shirt", 0, 0, {})

class no_weapon(item.item):
    def __init__(this):
        super().__init__("Fists", "weapon", 0, 0, {"range" : 1, "damage" : 1})

class no_consumable(item.item):
    def __init__(this):
        super().__init__("Nothing", "consumable", 0, 0, {"icon" : "   \n   \n   ", "color" : 0, "use" : world_object.no_func})

