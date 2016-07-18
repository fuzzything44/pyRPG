class item:
    """Item class, all items in the game are part of this.
item(name, quanitity, attributes = default)"""
    def __init__(this, item_name, type, on_equip, on_unequip, quantity = 1, attr = {"damage" : 1, "range": 0, "effects" : []}):
        this.name = item_name
        this.amount = quantity
        this.equip = on_equip
        this.unequip = on_unequip
        this.attributes = attr
        this.type = type
    def __lt__(self, other):
        return self.name < other
    
    def ___le__(self, other):
        return self.name <= other
    
    def __eq__(self, other):
        return self.name == other
    
    def __ne__(self, other):
        return self.name != other
    
    def __gt__(self, other):
        return self.name > other
    
    def __ge__(self, other):
        return self.name >= other
