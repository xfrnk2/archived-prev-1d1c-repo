from abc import *
from random import randrange


class SimulationObject(ABC):

    @abstractmethod
    def update(self):
        pass


class Customer(SimulationObject):

    def __init__(self, number, arrival_time):
        self.__arrival_time = arrival_time
        self.__maximum_waiting_time = randrange(15, 41)
        self.__customer_number = number
        self.__is_eating: bool = False
        self.__food_num = 0
        self.__food_eating_time = 0
        self.__waited_time = -1

        self.__is_bill_waiting: bool = False
        self.__is_billing: bool = False

        self.__get_required_waiting_time = Kitchen.get_min_cooking_time()

    def get_customer_number(self):
        return self.__customer_number

    def get_required_waiting_time(self):
        return self.__get_required_waiting_time

    def change_is_bill_waiting_status(self):
        self.__is_bill_waiting = not self.__is_bill_waiting

    def set_attribute(self, customer_info: tuple):
        self.__food_num, self.__food_eating_time = customer_info

    def get_request(self) -> tuple:
        return self.__customer_number, self.__food_num  # 손님번호, 음식번호

    def get_waited_time(self):
        return self.__waited_time

    def get_maximum_waiting_time(self):
        return self.__maximum_waiting_time

    def get_order(self) -> tuple:
        return self.__customer_number, self.__food_num

    def get_arrival_time(self):
        return self.__arrival_time

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

    def change_is_eating_status(self):
        self.__is_eating = not self.__is_eating


class CashDesk(SimulationObject):

    def __init__(self, billing_time):
        self.__customer_number = None
        self.__billing_time = billing_time
        self.__elapsed_billing_time = 0
        self.__is_working = False

    def receive_customer(self, customer: Customer):
        self.__customer_number = customer.get_request()[0]

    def update(self):  # 업데이트 후 새로운 계산대 손님 배정하는 순서로 감.
        if self.__is_working:
            self.__elapsed_billing_time += 1
            if self.__billing_time <= self.__elapsed_billing_time:
                self.change_cash_desk_status()
                return True
        return False

    def is_working(self):
        return self.__is_working

    def change_cash_desk_status(self):
        self.__elapsed_billing_time = 0
        self.__is_working = not self.__is_working

    def get_customer_info(self):
        return self.__customer_number


class BillManager:
    bill_waiting_queue = None
    cash_desk_num = 0
    cash_desk_object = None

    @staticmethod
    def init(waiting_time, cash_desk):

        __class__.bill_waiting_queue = []
        __class__.cash_desk_num = cash_desk
        __class__.cash_desk_object = CashDesk(billing_time=waiting_time)

    @staticmethod
    def receive_customer(customer: Customer):
        if not customer.get_is_billing() and not customer.get_is_bill_waiting():
            print(f"{customer.get_customer_number()}번 손님이 계산대 앞에 줄을 섭니다.")

            customer.change_is_bill_waiting_status()
            __class__.bill_waiting_queue.append(customer)

    @staticmethod
    def update():
        if __class__.cash_desk_object.update():
            print(f"{__class__.cash_desk_object.get_customer_info()}번 손님이 계산을 마치고 레스토랑을 떠났습니다.")

        if __class__.bill_waiting_queue and not __class__.cash_desk_object.is_working():
            __class__.cash_desk_object.receive_customer(__class__.bill_waiting_queue.pop(0))
            __class__.cash_desk_object.change_cash_desk_status()


class TableManager:
    table_queue = None

    @staticmethod
    def init(table_amount):
        __class__.table_queue = [0] * (table_amount)

    @staticmethod
    def set_customer(customer: Customer):
        for table_number, table in enumerate(__class__.table_queue):
            if not table:
                __class__.table_queue[table_number] = customer
                return table_number

    @staticmethod
    def customer_get_food(info):
        table_number, customer_number, food_number = info
        if __class__.table_queue[table_number].get_request() == (customer_number, food_number):
            # 좌석에 앉은 손님이 식사중 상태로 바뀐다.
            print(f"{customer_number}번 손님이 식사를 시작합니다.")
            __class__.table_queue[table_number].change_status_is_eating()
            return True
        else:
            raise ValueError

    @staticmethod
    def update():

        for num in range(len(__class__.table_queue)):
            if isinstance(__class__.table_queue[num], Customer):
                if __class__.table_queue[num].get_is_eating():
                    if __class__.table_queue[num].update():
                        target_customer = __class__.table_queue[num]
                        __class__.table_queue[num] = 0

                        print(f"{target_customer.get_customer_number()}번 손님이 식사를 마쳤습니다.")
                        target_customer.change_status_is_eating()

                        BillManager.receive_customer(target_customer)


class Cook:
    def __init__(self, number):
        self.__cook_number = number
        self.__food_number = 0
        self.__cooking_time = 0
        self.__customer_number = 0
        self.__table_number = 0
        self.__is_cooking = False

    def set_request(self, request):
        self.__table_number, self.__customer_number, self.__food_number, self.__cooking_time = request
        self.__is_cooking = not self.__is_cooking

    def get_cook_number(self):
        return self.__cook_number

    def serve_food_to_customer(self):
        self.__is_cooking = not self.__is_cooking
        return self.__table_number, self.__customer_number, self.__food_number

    def reset_cook(self):
        self.__table_number, self.__food_number, self.__customer_number, self.__cooking_time = 0, 0, 0, 0

    def is_cooking(self) -> bool:
        return self.__is_cooking

    def set_is_cooking(self):
        self.__is_cooking = not self.__is_cooking

    def get_left_cooking_time(self):
        return self.__cooking_time

    def update(self) -> bool:
        if self.__is_cooking:
            self.__cooking_time -= 1
            if self.__cooking_time == 0:
                return True
        return False


class Kitchen:
    cook_number = 0
    cooks = None

    @staticmethod
    def init(cook_num):
        __class__.cook_number = cook_num
        __class__.cooks = [Cook(i) for i in range(1, __class__.cook_number + 1)]

    @staticmethod
    def all_the_cooks_cooking() -> bool:
        return all(cook.is_cooking() for cook in __class__.cooks)

    @staticmethod
    def get_min_cooking_time():
        return min([cook.get_left_cooking_time() for cook in __class__.cooks])

    @staticmethod
    def get_is_not_cooking_cook():

        for cook_num, cook in enumerate(__class__.cooks):
            if not cook.is_cooking():
                return cook_num

    @staticmethod
    def update():
        if any(TableManager.table_queue) and __class__.cooks:
            for cook in Kitchen.cooks:
                if cook.update():
                    table_num, customer_num, food_num = cook.serve_food_to_customer()

                    print(f"{customer_num}번 손님의 {food_num}번 요리({RestaurantManager.food_name[food_num]}) 조리가 끝났습니다.")
                    cook.reset_cook()
                    TableManager.customer_get_food((table_num, customer_num, food_num))


class ComingCustomer:
    customer_number = 0

    @staticmethod
    def init():
        __class__.customer_number = 0

    @staticmethod
    def update(elapsed_time):
        __class__.customer_number += 1
        new_customer = Customer(__class__.customer_number, elapsed_time)
        print(f"{__class__.customer_number}번째 손님이 시각 {elapsed_time} 분에 레스토랑에 도착했습니다.")

        if RestaurantManager.check_reception(new_customer):
            RestaurantManager.receive_customer(new_customer)

        else:
            print(f"손님이 기다릴 수 없어 돌아갑니다.\n현재 대기 시간 {new_customer.get_waited_time()+1}분 / 대기 가능 시간 "
                  f"{new_customer.get_required_waiting_time()}분")


class RestaurantManager:
    food_name = {1: "스테이크", 2: "스파게티", 3: "마카로니", 4: "그라탱"}
    food_cooking_time = {1: 30, 2: 20, 3: 10, 4: 15}
    food_eating_time = {1: 30, 2: 20, 3: 15, 4: 10}

    waiting_customers = []

    @staticmethod
    def init():
        pass

    @staticmethod
    def receive_customer(customer: Customer):
        food_num = randrange(1, 5)

        customer.set_attribute((food_num, __class__.food_eating_time[food_num]))
        __class__.waiting_customers.append(customer)

    @staticmethod
    def check_reception(customer: Customer):
        if __class__.is_table_full():
            return False

        elif __class__.is_all_the_cooks_cooking():
            if customer.get_maximum_waiting_time() < customer.get_required_waiting_time():
                return False

        return True

    @staticmethod
    def update():
        if __class__.waiting_customers:
            customer_count = 0
            for customer in __class__.waiting_customers:
                customer.waiting_update()
                if customer.get_required_waiting_time() == customer.get_waited_time() and not Kitchen.all_the_cooks_cooking():
                    customer_count += 1

                    table_num = TableManager.set_customer(customer)
                    customer_number, food_number = customer.get_order()

                    print(f"{customer_number}번 손님이 {table_num}번 테이블에 앉습니다.")
                    print(f"{customer_number}번 손님이 {food_number}번 요리"
                          f" ({__class__.food_name[food_number]})를 주문합니다.")

                    RestaurantManager.assignment_customer_to_cook(customer, table_num)

            for _ in range(customer_count):
                __class__.waiting_customers.pop(0)

    @staticmethod
    def assignment_customer_to_cook(customer: Customer, table_number: int):
        for cook in Kitchen.cooks:
            if not cook.is_cooking():
                customer_num, customer_food_num = customer.get_request()
                cook.set_request(
                    (table_number, customer_num, customer_food_num, __class__.food_cooking_time[customer_food_num]))
                break

    @staticmethod
    def update_waiting_customers():
        for waiting_customer in __class__.waiting_customers:
            waiting_customer.waiting_update()

    @staticmethod
    def get_eating_time(self, food_number):
        return __class__.food_eating_time[food_number]

    @staticmethod
    def get_cooking_time(self, food_number):
        return __class__.food_cooking_time[food_number]

    @staticmethod
    def is_table_full() -> bool:
        if all(TableManager.table_queue):
            return True
        return False

    @staticmethod
    def is_all_the_cooks_cooking() -> bool:
        if Kitchen.all_the_cooks_cooking():
            return True
        return False


class Restaurant:
    # 손님 방문 주기
    visiting_period = 15
    table_quantity = 20
    cooks_num = 3
    billing_period = 5
    cash_desk_num = 1

    @staticmethod
    def init(customer_visiting_period: int):
        __class__.visiting_period = customer_visiting_period

        RestaurantManager.init()
        TableManager.init(__class__.table_quantity)
        Kitchen.init(__class__.cooks_num)
        BillManager.init(__class__.billing_period, __class__.cash_desk_num)
        ComingCustomer.init()

    @staticmethod
    def run():

        elapsed_time = 0

        while elapsed_time < 720:
            elapsed_time += 1
            print(f"{elapsed_time}분 : ")

            TableManager.update()
            Kitchen.update()
            BillManager.update()

            # 새로운 손님을 받는다.
            if elapsed_time % __class__.visiting_period == 0:
                ComingCustomer.update(elapsed_time)

            RestaurantManager.update()


if __name__ == "__main__":
    visiting_period = 15

    Restaurant.init(visiting_period)
    Restaurant.run()