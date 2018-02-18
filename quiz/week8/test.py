"""
import os
import time

class simulate():

    def __init__(self):
        self.__bull = None

    def set_bull(self):
        if __class__.test is True:
            self.__bull = True
        else:
            self.__bull = False

    def test(self):
        a = os.times()

        if a[0] >= 1:
            return True
        else:
            return False

    def timer(self):
            __class__.set_bull(self)

    def printing(self):
        if self.__bull:
            print(True)
        else:
            print(False)

test = simulate()

for x in range(5):
    time.sleep(1)

    test.timer()
    test.printing()
"""