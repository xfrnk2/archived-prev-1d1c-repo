# coding=utf-8

from week6.guest import Guest


class Menu:
    def __init__(self):  # , '스파게티','마카로니','그라탱':'15'
        self.__CookingTime = {'스테이크': 30, '스파게티': 20, '마카로니': 10, '그라탱': 15}
        self.__EatingTime = {'스테이크': 30, '스파게티': 20, '마카로니': 15, '그라탱': 10}
        self.__menu = {0: "스테이크", 1: "스파게티", 2: "마카로니", 3: "그라탱"}
        self.__order = None
        self.__guest = Guest()

    def get_cooking_time(self):
        getvalue = self.__CookingTime
        if self.__order == 0:
            return getvalue.get('스테이크')
        if self.__order == 1:
            return getvalue.get('스파게티')
        if self.__order == 2:
            return getvalue.get('마카로니')
        if self.__order == 3:
            return getvalue.get('그라탱')
        else:
            pass

    def get_eating_time(self):
        getvalue = self.__EatingTime
        if self.__order == 0:
            return getvalue.get('스테이크')
        if self.__order == 1:
            return getvalue.get('스파게티')
        if self.__order == 2:
            return getvalue.get('마카로니')
        if self.__order == 3:
            return getvalue.get('그라탱')

        else:
            pass

    def set_menu(self):
        menu_number = self.__order
        return self.__menu.get(menu_number)
        # 메뉴의 이름을 반환

    def get_order_number(self):
        return self.__order

    def place_order(self):

        menu = self.__guest.menu_type

        self.__order = menu

