import display
import world

from effects import dot
from effects import effect

from items import item

from objects import General
from objects.tutorial import mage_tut
from objects.Player import player_flags

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
        else:
            this.amount += 1

class warrior_quest_item(item.item):
    def __init__(this, quantity = 1):
        super().__init__("NAME", "consumable", 0, "???", quantity, {"icon" : "   \n   \n   "})

    def use(this, owner):
        pass

class thief_quest_item(item.item):
    def __init__(this, quantity = 1):
        super().__init__("NAME", "consumable", 0, "???", quantity, {"icon" : "   \n   \n   "})

    def use(this, owner):
        pass



class mage_rare_reward(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Slime tea", "consumable", 10, display.add_newlines("A tea made of gross slime. Why would you drink this?"), quantity, {"icon" : "|\\fg~\\fw|\n|\\fx\\bg#\\fw\\bx|\n\\\\_/"})

    def use(this, owner):
        owner.attributes["HP"] -= 5
        owner.attributes["effects"]["poison"] = dot.dot(owner, 5000, 5, "Poisoned")

class warrior_rare_reward(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Oops", "consumable", 10, display.add_newlines("Huh? You shouldn't have this."), quantity, {"icon" : "   \n   \n   "})

    def use(this, owner):
        pass

class thief_rare_reward(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Oops", "consumable", 10, display.add_newlines("Huh? You shouldn't have this."), quantity, {"icon" : "   \n   \n   "})

    def use(this, owner):
        pass

class any_rare_reward(item.item):
    def __init__(this, quantity = 1):
        super().__init__("Gross Souvenier", "consumable", 25, display.add_newlines("You're still hanging onto that bit of the boss you killed? Just get rid of it."), quantity, {"icon" : " \\bg\\fr~*\n\\bx\\fw \\bg\\fr@\\bx\\fw \n\\bg\\fr/|\\\\"})

    def use(this, owner):
        owner.attributes["effects"]["tutbosseff"] = effect.effect(owner, 10000, "Ugh")
        this.amount += 1

class rare_reward_skillbook(item.item):
    def __init__(this, quantity = 1):
        super().__init__("What not to collect", "consumable", 25, display.add_newlines("This book explains what you should and should not take from a monster.\n (Permanent +5 luck)"), quantity, {"icon" : "\\fy|==\n|==\n|==\\fw"})

    def use(this, owner):
        if player_flags.get_flag(owner, player_flags.SKILL_TUTORIAL): # They already have the skill
            this.amount += 1
        else:
            owner.attributes["luck"] += 5 # Give 5 luck!
            player_flags.set_flag(owner, player_flags.SKILL_TUTORIAL, 1)
   