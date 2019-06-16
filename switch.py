class switch(object):
    def __init__(self, moden):
        self.li = {
            'a': self.__a,
            'b': self.__b
        }
        function = self.li.get(moden, self.__other)
        function()

    def __a(self):
        print("This is function a!")

    def __b(self):
        print("This is function b!")

    def __other(self):
        print("This is other function!")


switch('a')
