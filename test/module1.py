var = 0

def func():
    global var
    var = 1

def pr():
    func()
    print(var)