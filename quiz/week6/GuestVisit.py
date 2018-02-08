# coding=utf-8

from week6.Guest import Guest
from week6.Table import TableManager

class GuestVisit:
    def __init__(self):
        self.__GuestElapsedTime = 0
        self.__data = Guest()

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

        number = self.__data.guest_number
        time = Time.elapsed_time
        print(f"{number}번째 손님이 시각 '{time}' 분에 레스토랑에 도착했습니다.")

