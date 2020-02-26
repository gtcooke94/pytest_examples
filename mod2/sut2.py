from mod.sut import return_name
from mod.constants import DEFAULT_NAME

def hello():
    x = return_name(DEFAULT_NAME)
    return "Hello {}".format(x)

