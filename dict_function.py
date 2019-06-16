def hello():
    print("hello!")


def bye():
    print("bye!")


dict_types = {
    "h": hello,
    "b": bye,
}


def switch(type):
    method = dict_types.get(type, None)
    if method:
        method()


switch('h')
