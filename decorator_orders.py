def makeBold(f):
    def wrapper():
        return "<b>" + f() + "</b>"
    return wrapper


def makeItalic(f):
    def wrapper():
        return "<i>" + f() + "</i>"
    return wrapper


@makeBold
@makeItalic
def report():
    return "Hello World!"


print(report())
