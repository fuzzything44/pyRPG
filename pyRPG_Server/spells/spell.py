import display

class spell:
    """Class to hold spell data.
Constructor: spell(manaCost, effect, icon): manaCost is how much mana it will cast the player to cast. Effect is the function taking a single paramater of the character casting it to actually cast the spell. Icon is the 3x3 ASCII icon to display when set.
cast(player): Casts the set spell. player is the one casting it
draw(): Draws the spell image in the top pane"""
    def __init__(this, manaCost, effect, name, icon):
        this.amount = manaCost
        this.on_cast = effect
        this.image = icon
        this.type = "spell"
        this.name = name
    def cast(this, player):
        if player.attributes["MP"] >= this.amount:
            this.on_cast(player)
            player.attributes["MP"] -= this.amount
