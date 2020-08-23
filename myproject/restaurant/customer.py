from random import randrange
from restaurant_object import RestaurantObject


class Customer(RestaurantObject):

    def __init__(self, number ,arrival_time):

        self.__arrival_time = arrival_time
        self.__maximum_waiting_time = randrange(15, 41)
        self.__customer_number = number
        self.__is_eating :bool = False
        self.__food_num = 0
        self.__elapsed_eating_time = 0
        self.__food_cooking_time = 0
        self.__waited_time_for_food = 0
        self.__food_eating_time = 0
        self.__elapsed_waiting_time = 0
        self.__required_waiting_time = 0

        self.__is_bill_waiting: bool = False
        self.__is_billing: bool = False

        self.__all_time = 0
        self.__new_left_time_to_table = 0

    def set_new_left_time_to_table(self, value):
        self.__new_left_time_to_table = value

    def get_new_left_time_to_table(self):
        return self.__new_left_time_to_table

    def set_all_time(self, value):
        self.__all_time = value

    def get_all_time(self):
        return self.__all_time

    def get_elapsed_waited_time_for_food(self):
        return self.__waited_time_for_food

    def get_required_waiting_time(self):
        return self.__required_waiting_time

    def get_elapsed_waiting_time(self)-> int:
        return self.__elapsed_waiting_time

    def get_food_cooking_time(self):
        return self.__food_cooking_time

    def get_food_eating_time(self):
        return self.__food_eating_time

    def get_elapsed_eating_time(self):
        return self.__elapsed_eating_time

    def get_customer_number(self)-> int:
        return self.__customer_number

    def set_required_waiting_time(self, required_waiting_time):
        self.__required_waiting_time = required_waiting_time

    def change_is_bill_waiting_status(self):
        self.__is_bill_waiting = not self.__is_bill_waiting

    def change_is_billing_status(self):
        self.__is_billing = not self.__is_billing

    def set_attribute(self, customer_info: tuple):
        self.__food_num, self.__food_eating_time, self.__food_cooking_time = customer_info

    def get_request(self) -> tuple:
        return self.__customer_number, self.__food_num #손님번호, 음식번호

    def get_total_required_time(self):
        return self.__food_cooking_time + self.__food_eating_time

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
        self.__elapsed_eating_time += 1
        if self.__elapsed_eating_time == self.__food_eating_time:
            return True
        return False

    def food_waiting_update(self):
        self.__waited_time_for_food += 1

    def waiting_update(self):
        self.__elapsed_waiting_time += 1

    def change_status_is_eating(self):
        self.__is_eating = not self.__is_eating

