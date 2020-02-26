from mod.sut import return_name

def hello():
    x = return_name()
    return "Hello {}".format(x)
