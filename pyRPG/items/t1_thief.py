from items import item

class t1_thief_hat(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Fedora", "hat", 0, quantity, {"maxHP_mod" : 5, "atk_spd_mod" : 5})

class t1_thief_pants(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Skinny Jeans", "pants", 0, quantity, {"maxHP_mod" : 10, "mov_spd_mod" : 10})

class t1_thief_ring(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Ring", "ring", 0, quantity, {"luck_mod" : 5, "str_mod" : 7})

class t1_thief_shirt(item.item):
    def __init__(this, quantity = 1):
        super().__init__("\"I'm with stupid\" shirt", "shirt", 0, quantity, {"maxHP_mod" : 10, "luck_mod" : 5})

class t1_thief_weapon(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Orange Mocha Frappuccino", "weapon", 0, quantity, {"range" : 2, "damage" : 7})

