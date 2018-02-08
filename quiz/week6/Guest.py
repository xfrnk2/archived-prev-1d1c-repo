# coding=utf-8

from week6.chef import Chef
from week6.menu import Menu
import random

class Guest:
    def __init__(self):
        self.__arrival_time: int = None
        self.menu_type: int = None
        self.max_waiting_time: int = None

        self.__eating_time = 0

        self.guest_number = 0

        self.__menu = Menu()
        self.__chef = Chef()

    def set_max_waiting_time(self):
        time = random.randrange(15, 41)
        self.max_waiting_time = time()

    @property
    def set_menu_type(self):
        problem = random.randrange(0, 3)
        return problem

    def guest_simulate(self):
        guest = Guest()
        guest.set_menu_type()
        value = guest.set_menu_type
        self.menu_type = value

        guest.set_max_waiting_time()

        # 도착한 현재 시간도 얻어오자

