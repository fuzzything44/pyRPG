from objects import world_object
import display
import world
import copy

class merchant(world_object.world_object):
    def __init__(this, posX, posY, inventory = []):
        super().__init__(posX, posY, 'interactable')
        this.attributes.update({"items" : inventory, "players_start" : {}, "players_buying" : {}, "players_selling" : {}})

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
                        pass #TODO: make sell menu
                    else:   # They chose buy
                        can_buy = [] # What items they can buy
                        options = [] # Text for menu
                        for itm in this.attributes["items"]:
                            if itm.value() <= plr.attributes["money"]: # If they can buy it, add it.
                                can_buy.append(itm)
                                options.append(itm.name + '(' + str(itm.value) + ')')
                        plr.attributes["current_menu"] = display.menu("Buy what?", plr, "Nothing", *options)
                        this.attributes["players_buying"][plr] = can_buy

                    left_players.append(plr)
            else:
                left_players.append(plr)
            if plr not in world.players:
                left_players.append(plr)

        for left in left_players:
            del this.attributes["players_start"][left]

        left_players.clear()
        for plr in this.attributes["players_buying"]:
            if plr.X + 1 >= this.X and plr.X - 1 <= this.X and plr.Y + 1 >= this.Y and plr.Y -1 <= this.Y:
                upd = plr.attributes["current_menu"].update()
                if upd is not None:
                    if upd != 0:
                        item_bought = this.attributes["players_buying"][plr][upd - 1] # Find chosen item
                        if item_bought.value <= plr.attributes["money"]: # Give them item if true
                            if item_bought in plr.attributes["items"]:
                                # Get their item location
                                plr.attributes["items"][plr.attributes["items"].index(item_bought)].amount \
                                         += item_bought.amount # And add how many they bought
                            else: # Give them the item
                                plr.attributes["items"].append(copy.deepcopy(item_bought))

                    
                    this.attributes["players_start"][plr] = 0
                    plr.attributes["current_menu"] = display.menu("Buy what?", plr, "Nothing", *options)
                    left_players.append(plr)
            else:
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
                    #TODO: have them sell that item.
                    left_players.append(plr)
            else:
                left_players.append(plr)
            if plr not in world.players:
                left_players.append(plr)

        for left in left_players:
            del this.attributes["players_selling"][left]

    def char(this):
        return 'M'
    
    def color(this):
        return display.YELLOW


