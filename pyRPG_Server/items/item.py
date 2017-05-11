import display
# Item class. Note that for all equipment, certain attribute modifiers will be displayed in the menu:
# maxHP = red
# maxMP = blue
# mov_spd = green
# atk_spd = white
# magic = cyan
# str = magenta
# luck = yellow
# To override this, add the attribute "disp_data".
class item:
    """Item class, all items in the game are part of this."""
    def __init__(this, item_name, type, sell_value, description, quantity = 1, attr = {}):
        """Parameters:
            item_name: The name of the item.
            type: What type it is. hat, pants, consumable...
            sell_value: How much it sells for. 0 if it is unsellable
            quantity: How many there are.
"""
        this.name = item_name
        this.amount = quantity
        this.value = sell_value
        this.description = description
        this.attributes = attr
        this.type = type
        if "disp_data" not in this.attributes: # They gave no default display data. Make it.
            disp_str = ""   # Go through all default modifiers and add them to the string.

            if this.type == "weapon":
                # It's a weapon, so we need to show range and damage
                disp_str += " Range " + str(this.attributes["range"]) + " " # Add range
                disp_str += "Damage " + str(this.attributes["damage"]) + " " # Add damage
            mod_types = ["maxHP_mod", "maxMP_mod", "mov_spd_mod", "atk_spd_mod", "magic_mod", "str_mod", "luck_mod"]
            mod_colors = 'rbgwcmy'

            for mod in mod_types:
                if mod in this.attributes:
                    disp_str += "\\f" + mod_colors[mod_types.index(mod)]
                    mod_str = '('
                    if this.attributes[mod] >= 0:
                        mod_str += '+'
                    mod_str += str(this.attributes[mod]) + ')'
                    disp_str += mod_str
            this.attributes["disp_data"] = disp_str + '\\fw'
    def __lt__(self, other):
        return self.name < other

    def ___le__(self, other):
        return self.name <= other

    def __eq__(self, other):
        "For objects to be equal, they need same name, attributes, type, and value."
        return (self.name == other.name) and (self.attributes == other.attributes) and (self.type == other.type) and (self.value == other.value)

    def __ne__(self, other):
        return self.name != other

    def __gt__(self, other):
        return self.name > other

    def __ge__(self, other):
        return self.name >= other

    # Default equip and unequip functions. Use these when having normal enchantments.
    def equip(this, player):
        if "maxHP_mod" in this.attributes:
            player.attributes["maxHP"] += this.attributes["maxHP_mod"]
            player.attributes["HP"] += this.attributes["maxHP_mod"]
        if "maxMP_mod" in this.attributes:
            player.attributes["maxMP"] += this.attributes["maxMP_mod"]
            player.attributes["MP"] += this.attributes["maxMP_mod"]
        if "mov_spd_mod" in this.attributes:
            player.attributes["mov_spd"] += this.attributes["mov_spd_mod"]
        if "atk_spd_mod" in this.attributes:
            player.attributes["atk_spd"] += this.attributes["atk_spd_mod"]
        if "magic_mod" in this.attributes:
            player.attributes["magic"] += this.attributes["magic_mod"]
        if "str_mod" in this.attributes:
            player.attributes["strength"] += this.attributes["str_mod"]
        if "luck_mod" in this.attributes:
            player.attributes["luck"] += this.attributes["luck_mod"]
    def unequip(this, player):
        if "maxHP_mod" in this.attributes:
            player.attributes["maxHP"] -= this.attributes["maxHP_mod"]
            player.attributes["HP"] -= this.attributes["maxHP_mod"]
        if "maxMP_mod" in this.attributes:
            player.attributes["maxMP"] -= this.attributes["maxMP_mod"]
            player.attributes["MP"] -= this.attributes["maxMP_mod"]
        if "mov_spd_mod" in this.attributes:
            player.attributes["mov_spd"] -= this.attributes["mov_spd_mod"]
        if "atk_spd_mod" in this.attributes:
            player.attributes["atk_spd"] -= this.attributes["atk_spd_mod"]
        if "magic_mod" in this.attributes:
            player.attributes["magic"] -= this.attributes["magic_mod"]
        if "str_mod" in this.attributes:
            player.attributes["strength"] -= this.attributes["str_mod"]
        if "luck_mod" in this.attributes:
            player.attributes["luck"] -= this.attributes["luck_mod"]
