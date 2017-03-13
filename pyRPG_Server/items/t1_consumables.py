from items import item

class t1_health(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Red Potion", "consumable", 5, "A small bottle with a red\n fluid inside.", quantity, {"maxMP_mod" : 10})



