from restaurant_object import RestaurantObject
from customer import Customer


class TableManager(RestaurantObject):


    def __init__(self, table_amount):
        self.__table_queue = [0]*(table_amount)

    def is_exist(self)-> bool:
        return any(self.__table_queue)

    def set_customer(self, customer:Customer):

        for table_number, table in enumerate(self.__table_queue):
            if not table:
                self.__table_queue[table_number] = customer
                return table_number

    def getting_food(self, info: tuple):
        table_number, customer_number, food_number = info

        if isinstance(self.__table_queue[table_number], Customer) and \
                self.__table_queue[table_number].get_request() == (customer_number, food_number):

                print(f"{customer_number}번 손님이 식사를 시작합니다.")
                self.__table_queue[table_number].change_status_is_eating()
        else:
            pass


    def is_table_full(self)-> bool:
        return all(self.__table_queue)

    def get_table_left(self)-> int:
        return len(list(filter(lambda x: x == 0, self.__table_queue)))

    def update(self)-> list:
        target_customer_queue = []

        for num in range(len(self.__table_queue)):
            if isinstance(self.__table_queue[num], Customer) and self.__table_queue[num].get_is_eating():
                    if self.__table_queue[num].update():

                        target_customer = self.__table_queue[num]
                        self.__table_queue[num] = 0

                        print(f"{target_customer.get_customer_number()}번 손님이 식사를 마쳤습니다.")
                        target_customer.change_status_is_eating()
                        target_customer_queue.append(target_customer)

        return target_customer_queue
