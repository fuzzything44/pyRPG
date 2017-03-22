from items import item

class t1_health(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Red Potion", "consumable", 5, "A small bottle with a red\n fluid inside.", quantity, {"icon" : "\\fy ^ \n\\fw|\\fr~\\fw|\n\\\\\\fr#\\fw/"})

    def use(this, owner):
        owner.attributes["HP"] = min(owner.attributes["HP"] + 10, owner.attributes["maxHP"])

class t1_mana(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Blue Potion", "consumable", 5, "A small bottle with a blue\n fluid inside.", quantity, {"icon" : "\\fy ^ \n\\fw|\\fb~\\fw|\n\\\\\\fb#\\fw/"})

    def use(this, owner):
        owner.attributes["MP"] = min(owner.attributes["MP"] + 10, owner.attributes["maxMP"])
