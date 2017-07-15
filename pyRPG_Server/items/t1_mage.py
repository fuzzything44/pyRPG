from items import item

class t1_mage_hat(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Magical hat", "hat", 5, "Complete with pointy tip!", quantity, {"maxMP_mod" : 10})

class t1_mage_pants(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Pants of Power", "pants", 5, "These pants are only slightly sentient.", quantity, {"maxMP_mod" : 15})

class t1_mage_ring(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Cubic Zirconium Ring", "ring", 5, "Diamond was too expensive.", quantity, {"maxMP_mod" : 5, "magic_mod" : 5})

class t1_mage_shirt(item.item):
    def __init__(this, quantity = 1):
        super().__init__("White shirt", "shirt", 5, "No one knows what type of shirt this is.", quantity, {"maxMP_mod" : 25})

class t1_mage_weapon(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Aluminum wand", "weapon", 5, "A normal rod of aluminum about a foot long.", quantity, {"range" : 7, "damage" : 5})


