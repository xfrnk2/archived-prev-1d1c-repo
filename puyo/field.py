from block import Block

width = 6
height = 12



class PrintField():
    def __init__(self):
        self.__width = width
        self.__height = height
        self.__original = [Block()for _ in range(width)for _ in range(height)]


    def test(self):

        print(str(self.__original))