# coding=utf-8

from week6.counter import Counter
from week6.menu import Menu


class Chefs:
    chefs = 3


class Chef:
    def __init__(self: int):
        self.__chef_first = None
        self.__chef_second = None
        self.__chef_third = None
        self.__works = [0 for _ in range(Chefs.chefs)]
        self.__menu = Menu()
        self.__counter = Counter()

    @staticmethod
    def print_finished_cooking():
        print("n번 손님의 i번 요리(oooo) 조리가 끝났습니다")
        print("n번 손님이 식사를 시작합니다")

    @staticmethod
    def print_finished_eating():
        print(" n번 손님이 식사를 마쳤습니다.")
        print(" n번 손님이 계산대 앞에 줄을 섭니다.")

    def reset_chef_time(self):
        if self.__chef_first == 0:
            self.__chef_first = None
            __class__.print_finished_eating()
            self.__counter.status_of_counter = True
        if self.__chef_second == 0:
            self.__chef_second = None
            __class__.print_finished_eating()
            self.__counter.status_of_counter = True
        if self.__chef_third == 0:
            self.__chef_third = None
            __class__.print_finished_eating()
            self.__counter.status_of_counter = True

        else:
            pass

    def minus_time(self):
        if self.__chef_first > 0:
            self.__chef_first -= 1
        if self.__chef_second > 0:
            self.__chef_second -= 1
        if self.__chef_third > 0:
            self.__chef_third -= 1
        else:
            __class__.reset_chef_time(self)

    def chef_simulate(self):

        chef = Chefs.chefs

        works = self.__works

        group = [self.__chef_first, self.__chef_second,
                 self.__chef_third]

        value = self.__menu.get_cooking_time()

        for x in range(chef):
            if works[x] == 1:
                continue
            if x == chef - 1:
                if works[x] == 1:
                    # 꽉 찼다
                    pass
                else:
                    works[x] = 1

                    group[x] = value

            else:
                works[x] = 1

                group[x] = value
