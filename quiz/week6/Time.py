# coding=utf-8

from week6.chef import Chef
from week6.counter import Counter
from week6.guest import Guest
from week6.guestvisit import GuestVisit

class Time:

    def __init__(self):
        self.__chef = Chef()
        self.__counter = Counter()
        self.__guest = Guest()
        self.__guest_visit = GuestVisit
        self.elapsed_time = 0

    def tick(self):
        for x in range(720):
            self.elapsed_time += 1
            elapsed_time = self.elapsed_time
            print(f"현재시간 {elapsed_time}/720분)")

            self.__guest.guest_simulate()
            self.__guest_visit.add_new_guest()

            self.__chef.minus_time()
            self.__counter.minus_time()

            self.__chef.chef_simulate()
            self.__chef.reset_chef_time()
            self.__counter.simulate()

            # get 걸리는 시간을 얻어온다. 매 틱 마다 한번씩 모든 장소를 반복 실행함.
