from random import randrange
from restaurant_object import RestaurantObject


class Customer(RestaurantObject):

    def __init__(self, number ,arrival_time):

        self.__arrival_time = arrival_time
        self.__maximum_waiting_time = randrange(15, 41)
        self.__customer_number = number
        self.__is_eating :bool = False
        self.__food_num = 0
        self.__food_eating_time = 0
        self.__waited_time = 0


        self.__is_bill_waiting: bool = False
        self.__is_billing: bool = False

        self.__required_waiting_time = 0

    def get_customer_number(self)-> int:
        return self.__customer_number

    def set_required_waiting_time(self, required_waiting_time):
        self.__required_waiting_time = required_waiting_time

    def get_required_waiting_time(self)-> int:
        return self.__required_waiting_time

    def change_is_bill_waiting_status(self):
        self.__is_bill_waiting = not self.__is_bill_waiting

    def set_attribute(self, customer_info: tuple):
        self.__food_num, self.__food_eating_time = customer_info

    def get_request(self) -> tuple:
        return self.__customer_number, self.__food_num #손님번호, 음식번호

    def get_waited_time(self)-> int:
        return self.__waited_time

    def get_maximum_waiting_time(self)-> int:
        return self.__maximum_waiting_time

    def get_order(self)-> tuple:
        return self.__customer_number, self.__food_num

    def get_is_eating(self) -> bool:
        return self.__is_eating

    def get_is_billing(self) -> bool:
        return self.__is_billing

    def get_is_bill_waiting(self) -> bool:
        return self.__is_bill_waiting

    def update(self):
        self.__food_eating_time -= 1
        if self.__food_eating_time == 0:
            return True
        return False

    def waiting_update(self):
        self.__waited_time += 1

    def change_status_is_eating(self):
        self.__is_eating = not self.__is_eating

