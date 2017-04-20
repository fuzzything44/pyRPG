import copy

import display
import world

from items import tutorial_quest_items
from items import no_item

from objects import General
from objects.Player import player_flags

def add_skillbook(plr):
    bit = tutorial_quest_items.any_rare_reward()
    index = plr.attributes["items"].index(bit)
    num_books = plr.attributes["items"][index].amount
    del plr.attributes["items"][index] # Remove gross bits

    if plr.attributes["consumable"] == bit:
        plr.attributes["consumable"] = no_item.no_consumable()

    book = tutorial_quest_items.rare_reward_skillbook(num_books)
    if book in plr.attributes["items"]:
        plr.attributes["items"][plr.attributes["items"].index(book)].amount += num_books
    else:
        plr.attributes["items"].append(book)


class quest_giver(General.npc.npc):
    """Talks to the player.""" #TODO: add a good interface for complex dialog trees.

    def __init__(this, posX, posY, dialogue, hard_portal = "lower"):
        super().__init__(posX, posY, dialogue)
        dialogue.add_exit("give_reward", 2, add_skillbook)
        this.attributes["next_portal"] = hard_portal

    def update(this, delta_time):
        "Talks to player if they're standing next to it."
        for plr in world.players:
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                if plr not in this.attributes["talking_players"]: # Not talking to them already
                    diag = copy.deepcopy(this.attributes["dialogue"])
                    diag.linked_player = plr
                    if not player_flags.get_flag(plr, player_flags.TUT_MONEY_GIVEN): # Don't have tut money, so give it
                        diag.nodes["start"].text += "\nYou're new. Take this money.\nUse it to buy some gear\n at the (\\fyM\\fw) Merchant"
                        diag.nodes["start"].options = [("Thanks!", "money")]
                    elif tutorial_quest_items.any_rare_reward() in plr.attributes["items"]:
                        diag.nodes["start"].text += "\n" + display.add_newlines("Hey, what's that gross monster bit you have? You really shouldn't hold on to that. \nLet me take it off your hands.")
                        diag.nodes["start"].options = [("Sure", "give_reward"), ("No thanks", "exit")]
                    elif plr.attributes["level"] < 5:
                        diag.nodes["start"].text += "\nGo to the (\\fb0\\fw) portal at\n the right.\nCome back when you're\n stronger."
                    else:
                        diag.nodes["start"].text += "\nNice job!\nGo to the " + this.attributes["next_portal"] + " portal\n for a bigger challenge."
                    this.attributes["talking_players"][plr] = diag

        left_players = []
        for plr, diag in this.attributes["talking_players"].items(): 
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y and plr in world.players:
                diag.run()
            else:
                left_players.append(plr)

        for gone in left_players:
            del this.attributes["talking_players"][gone]
            gone.attributes["current_menu"] = None

        if ("HP" in this.attributes) and (this.attributes["HP"] <= 0):
            world.to_del.append(this)
    
    

