# coding=utf-8

from week6.Chef import Chef

class Counter:
    def __init__(self):
        self.__own_time = 0
        self.status_of_counter = None
        self.__chef = Chef()

    def simulate(self):
        if self.status_of_counter is True:

            self.__own_time += 5
        else:
            pass

    def minus_time(self):
        if self.__own_time > 0:

            self.__own_time -= 1

        else:
            print("n번 손님이 계산을 마치고 레스토랑을 떠났습니다.")
            self.status_of_counter = False
