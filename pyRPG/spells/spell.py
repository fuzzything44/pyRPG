class spell:
    """Class to hold spell data.
Constructor: spell(manaCost, effect, icon): manaCost is how much mana it will cast the player to cast. Effect is the function taking a single paramater of the character casting it to actually cast the spell. Icon is the 3x3 ASCII icon to display when set."""
    def __init__(this, manaCost, effect, icon):
        this.amount = manaCost
        this.cast = effect
        this.image = icon
    
        

