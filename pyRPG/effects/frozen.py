def frozen(obj, delta_time):
    try:
        obj.X = obj.attributes["stuckX"]
        obj.Y = obj.attributes["stuckY"]
    except:
        pass

def unfreeze(obj):
    try:
        del obj.attributes["stuckX"]
        del obj.attributes["stuckY"]
    except:
        pass