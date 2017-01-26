from objects import world_object
import display
import world
import copy

from items import no_item

class merchant(world_object.world_object):
    def __init__(this, posX, posY, inventory = [], overpricing = 2):
        super().__init__(posX, posY, 'interactable')
        this.attributes.update({"items" : inventory, "players_start" : {}, "players_buying" : {}, "players_selling" : {}, "cost_mult" : overpricing})

    def update(this, delta_time):
        for plr in world.players:
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                if plr.attributes["current_menu"] is None: # Start talking to new players
                    this.attributes["players_start"][plr] = 0
                    plr.attributes["current_menu"] = display.menu("Buy or sell?", plr, "Buy", "Sell")

        left_players = []
        for plr in this.attributes["players_start"]:
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                upd = plr.attributes["current_menu"].update()
                if upd is not None:
                    if upd: # They chose sell
                        can_sell = [] # What items they can sell
                        options  = [] # Text for menu
                        for itm in plr.attributes["items"]:
                            if itm.value > 0:
                                can_sell.append(itm)
                                options.append(itm.name + '(' + str(itm.amount) + ')(\\fy' + str(itm.value) + '\\fw)')
                        plr.attributes["current_menu"] = display.menu("Sell what?", plr, "Nothing", *options)
                        this.attributes["players_selling"][plr] = can_sell
                    else:   # They chose buy
                        can_buy = [] # What items they can buy
                        options = [] # Text for menu
                        for itm in this.attributes["items"]:
                            if itm.value * this.attributes["cost_mult"] * itm.amount <= plr.attributes["money"]: # If they can buy it, add it.
                                can_buy.append(itm)
                                options.append(itm.name + '(' + str(itm.amount) + ')(\\fy' + str(itm.value * this.attributes["cost_mult"] * itm.amount) + '\\fw)')
                        plr.attributes["current_menu"] = display.menu("Buy what?", plr, "Nothing", *options)
                        this.attributes["players_buying"][plr] = can_buy

                    left_players.append(plr)
            else:
                plr.attributes["current_menu"] = None
                left_players.append(plr)
            if plr not in world.players:
                left_players.append(plr)

        for left in left_players:
            left.attributes["current_menu"] = None

            del this.attributes["players_start"][left]

        left_players.clear()
        for plr in this.attributes["players_buying"]:
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                upd = plr.attributes["current_menu"].update()
                if upd is not None:
                    if upd != 0:
                        item_bought = this.attributes["players_buying"][plr][upd - 1] # Find chosen item
                        if item_bought.value * this.attributes["cost_mult"] * item_bought.amount <= plr.attributes["money"]: # Give them item if true
                            if item_bought in plr.attributes["items"]:
                                # Get their item location
                                plr.attributes["items"][plr.attributes["items"].index(item_bought)].amount \
                                         += item_bought.amount # And add how many they bought
                            else: # Give them the item
                                plr.attributes["items"].append(copy.deepcopy(item_bought))
                            plr.attributes["money"] -= item_bought.value * this.attributes["cost_mult"] * item_bought.amount

                    this.attributes["players_start"][plr] = 0
                    plr.attributes["current_menu"] = display.menu("Buy or sell?", plr, "Buy", "Sell")
                    left_players.append(plr)
            else:
                plr.attributes["current_menu"] = None
                left_players.append(plr)
            if plr not in world.players:
                left_players.append(plr)

        for left in left_players:
            del this.attributes["players_buying"][left]

        left_players.clear()
        for plr in this.attributes["players_selling"]:
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                upd = plr.attributes["current_menu"].update()
                if upd is not None:
                    if upd != 0:
                        item_sold = this.attributes["players_selling"][plr][upd - 1]  # Find chosen item
                        if item_sold in plr.attributes["items"]:  # If they still have it
                            plr.attributes["money"] += item_sold.value # Give gold
                            item_sold.amount -= 1                 # Remove one of it
                            if item_sold.amount <= 0:             # No items left
                                del plr.attributes["items"][plr.attributes["items"].index(item_sold)]  # Remove item from inventory
                                if plr.attributes[item_sold.type] == item_sold: # If equipped
                                    plr.attributes[item_sold.type].unequip(plr)
                                    plr.attributes[item_sold.type] = no_item.make_noitem(item_sold.type)

                    this.attributes["players_start"][plr] = 0
                    plr.attributes["current_menu"] = display.menu("Buy or sell?", plr, "Buy", "Sell")
                    left_players.append(plr)
            else:
                plr.attributes["current_menu"] = None
                left_players.append(plr)
            if plr not in world.players:
                left_players.append(plr)

        for left in left_players:
            del this.attributes["players_selling"][left]

    def char(this):
        return 'M'
    
    def color(this):
        return display.YELLOW


