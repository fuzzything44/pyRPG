from items import item

class t1_warrior_hat(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Helmet", "hat", 5, "How boring.", quantity, {"maxHP_mod" : 10})

class t1_warrior_pants(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Leggings", "pants", 5, "Pretty much what you'd expect.", quantity, {"maxHP_mod" : 15})

class t1_warrior_ring(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Ring", "ring", 5, "An iron ring. It has a few runes.", quantity, {"maxHP_mod" : 5, "str_mod" : 5})

class t1_warrior_shirt(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Breastplate", "shirt", 5, "Platemail normally weighs 35 to 55 pounds.", quantity, {"maxHP_mod" : 25})

class t1_warrior_weapon(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Iron Longsword", "weapon", 5, "Long, sharp, and hard. What else do you need?", quantity, {"range" : 2, "damage" : 5})

