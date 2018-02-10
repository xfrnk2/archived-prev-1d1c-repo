# coding=utf-8

from week6.guest import Guest
from week6.table import TableManager
from week6.time import Time
import random


class GuestVisit:
    def __init__(self):
        self.__GuestElapsedTime = 0
        self.__data = Guest()
        self.__time = Time()

    @staticmethod
    def checking_visited_guest() -> bool:

        machine = random.randrange(5)
        if machine == 2 or 3:
            return True

        else:
            return False

    def add_new_guest(self):

        self.checking_visited_guest()
        value = self.checking_visited_guest()
        if value is True:

            self.__data.guest_number += 1

            self.when_guest_visited()

            table = TableManager()
            table.simulate()

        else:
            pass

    def when_guest_visited(self):
        # FIXME - 여러가지 역할을 하는 복합 함수가 미묘하게 적당하지 않은 이름으로 정의 돼 있네요.

        number = self.__data.guest_number
        time = self.__time.elapsed_time
        print(f"{number}번째 손님이 시각 '{time}' 분에 레스토랑에 도착했습니다.")

