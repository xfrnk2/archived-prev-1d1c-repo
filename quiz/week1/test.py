class Test():

    def __init__(self):
        self.__x = 0
        self.__y = 0

    def get_pos(self):
        return self.__x, self.__y


doing = Test()
print(doing.get_pos())