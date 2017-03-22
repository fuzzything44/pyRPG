import world

from items import item

from objects import General
from objects.tutorial import mage_tut

class mage_quest_item(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Broken Rune", "consumable", 0, "A broken rune.", quantity, {"icon" : "\\fx\\bm\\\\|/\n-#-\n/|\\\\"})

    def use(this, owner):
        if this.amount >= 4 and world.world_name == "mage_tut_2": # They have enough
            world.objects.append(General.timed_portal.timed_portal(25, 10, "mage_tut_boss", 10, 10, 3000))
            world.objects.append(General.timed_portal.timed_portal(25, 9, "mage_tut_boss", 10, 10, 3000))
            world.objects.append(General.timed_portal.timed_portal(26, 10, "mage_tut_boss", 10, 10, 3000))
            world.objects.append(General.timed_portal.timed_portal(26, 9, "mage_tut_boss", 10, 10, 3000))

            this.amount -= 3