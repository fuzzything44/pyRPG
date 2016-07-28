def frozen(obj, delta_time):
    obj.X = obj.attributes["stuckX"]
    obj.Y = obj.attributes["stuckY"]

def unfreeze(obj):
    del obj.attributes["stuckX"]
    del obj.attributes["stuckY"]
