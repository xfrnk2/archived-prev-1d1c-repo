class Test():

    def __init__(self):
        self.__x = 0
        self.__y = 0

    def get_pos(self):
        return self.__x, self.__y


doing = Test()
print(doing.get_pos())


def calculator():
    while True:

        value = input("게산을 입력하세요 예) a+b, a-b, a*b, a/b")
        value2 = list(value)

        if '+' in value2:
            x = value2.index('+')
            result = int(value2[x - 1]) + int(value[x + 1])
            print(result)

        elif '-' in value2:
            x = value2.index('-')
            result = int(value2[x - 1]) + int(value[x + 1])
            print(result)

        elif '*' in value2:
            x = value2.index('*')
            result = int(value2[x - 1]) * int(value[x + 1])
            print(result)

        elif '/' in value2:
            x = value2.index('/')
            result = int(value2[x - 1]) / int(value[x + 1])
            print(result)


calculator()
