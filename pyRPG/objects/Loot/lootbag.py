import display
import world

def update(this, delta_time):
    pass

def collide(this, obj):
    if obj == world.player:
        for item in this.attributes["items"]:
            # Give item. First check if they have one
            if item in world.player.attributes["items"]:
                # Get their item location
                world.player.attributes["items"][world.player.attributes["items"].index(item)].amount += 1 # Give them the item
            else: # Give them the item
                world.player.attributes["items"].append(item) # Giving the player the chest's items.

        world.to_del.append(this)

def color(this):
    return display.YELLOW

def char(this):
    return 'L'


type = "money"

attributes = {
    "items": []
}
