from items import item

class start_hat(item.item):
    def __init__(this, quantity = 1):
        super().__init__("No0b hat", "hat", 1, quantity, {"maxHP_mod" : 1})

class start_pants(item.item):
    def __init__(this, quantity = 1):
        super().__init__("No0b pants", "pants", 1, quantity, {"luck_mod" : 1})

class start_ring(item.item):
    def __init__(this, quantity = 1):
        super().__init__("No0b ring", "ring", 1, quantity, {"maxMP_mod" : 1})

class start_shirt(item.item):
    def __init__(this,  quantity = 1):
        super().__init__("No0b shirt", "shirt", 1, quantity, {"maxHP_mod" : 3})

class start_weapon(item.item):
    def __init__(this, quantity = 1):
        super().__init__("No0b sword", "weapon", 1, quantity, {"range" : 2, "damage" : 1})

