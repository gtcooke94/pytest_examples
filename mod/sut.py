from mod.constants import DEFAULT_NAME

def hello():
    x = return_name(DEFAULT_NAME)
    return "Hello {}".format(x)

def return_name(name=DEFAULT_NAME):
    return name
