class item:
    """Item class, all items in the game are part of this.
item(name, quanitity, attributes = default)"""
    def __init__(this, item_name, quantity = 1, attr = {"type" : "weapon", "damage" : 1, "range": 0, "effects" : []}):
        this.name = item_name
        this.amount = quantity
        this.attributes = attr

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
