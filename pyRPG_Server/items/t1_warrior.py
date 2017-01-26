from items import item

class t1_warrior_hat(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Helmet", "hat", 5, quantity, {"maxHP_mod" : 10})

class t1_warrior_pants(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Leggings", "pants", 5, quantity, {"maxHP_mod" : 15})

class t1_warrior_ring(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Ring", "ring", 5, quantity, {"maxHP_mod" : 5, "str_mod" : 5})

class t1_warrior_shirt(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Breastplate", "shirt", 5, quantity, {"maxHP_mod" : 25})

class t1_warrior_weapon(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Longsword", "weapon", 5, quantity, {"range" : 3, "damage" : 5})

