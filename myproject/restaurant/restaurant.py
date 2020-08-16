from abc import *
from random import randrange

class SimulationObject(ABC):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass


class Customer:

    def __init__(self, arrival_time):

        self.__arrival_time = arrival_time
        self.__maximum_waiting_time = randrange(15, 41)
        self.__customer_number = None
        self.__is_eating :bool = False
        self.__food_num = None
        self.__food_eating_time = None
        self.__waited_time = 0



    def set_attribute(self, customer_info: tuple):
        self.__customer_number, self.__food_num, self.__food_eating_time = customer_info

    def get_waited_time(self):
        return self.__waited_time

    def get_food_waiting_time(self):
        return self.__food_waiting_time

    def set_food_waiting_time(self, value: int):
        self.__food_waiting_time = value

    def get_maximum_waiting_time(self):
        return self.__maximum_waiting_time

    def get_food_num(self):
        return self.__food_num

    def get_arrival_time(self):
        return self.__arrival_time

    def get_is_eating(self) -> bool:
        return self.__is_eating

    def waiting_update(self):
        self.__waited_time += 1
        
                
    def eating_update(self):
        if self.__is_eating:
            pass


class TableManager:

    table_queue = None

    @staticmethod
    def init(table_amount):
        __class__.table_queue = [0]*(table_amount+1) # 1번 테이블에서부터 시작하기 위해 0번은 비워두기로 했다.

    @staticmethod
    def update():
        for customer in __class__.table_queue:
            customer.update()


class Cook:
    def __init__(self, number):
        self.__cook_number = number
        self.__food_number = None
        self.__cooking_time = None
        self.__customer_number = None
        self.__is_cooking = False

    def set_request(self, request: tuple):
        self.__food_number, self.__cooking_time, self.__customer_number = request

    def get_cook_number(self):
        return self.__cook_number

    def update(self)-> bool:
        if self.__is_cooking:
            self.__cooking_time -= 1
            if self.__cooking_time == 0:
                return True

        return False

    def is_cooking(self)-> bool:
        return self.__is_cooking

    def set_is_cooking(self):
        self.__is_cooking = not self.__is_cooking

    def get_left_cooking_time(self):
        return self.__cooking_time

class Kitchen:

    cook_number = 0
    cooks = None

    @staticmethod
    def init(cook_num):
        __class__.cook_number = cook_num
        __class__.cooks = [Cook(i) for i in range(1, __class__.cook_number+1)]

    @staticmethod
    def all_the_cooks_cooking()-> bool:
        return all(cook.is_cooking() for cook in __class__.cooks)

    @staticmethod
    def get_min_cooking_time():
        return min([cook.get_left_cooking_time() for cook in __class__.cooks])

class RestaurantManager:

    food_name = {1: "스테이크", 2: "스파게티" , 3: "마카로니", 4:"그라탱"}
    food_cooking_time = {1: 30, 2: 20, 3: 10, 4: 15}
    food_eating_time =  {1: 30, 2: 20, 3: 15, 4: 10}
    customer_ordinal_number = 0
    waiting_customers= []

    @staticmethod
    def init():
        pass

    @staticmethod
    def receive_customer(customer : Customer):
        __class__.customer_ordinal_number += 1
        food_number = randrange(1, 5)
        print(f"{__class__.customer_ordinal_number}번째 손님이 시각 {customer.get_arrival_time()}분에 레스토랑에 도착했습니다.")
        customer.set_attribute((__class__.customer_ordinal_number, food_number, __class__.food_eating_time[food_number]))

        if __class__.is_table_full():
            print(f"손님이 기다릴 수 없어 돌아갑니다.\n현재 대기 시간 {customer.get_waited_time()}분 / 대기 가능 시간 "
                  "0분")

        if __class__.is_all_the_cooks_cooking():

            waiting_time = customer.get_food_waiting_time() + Kitchen.get_min_cooking_time()
            if customer.get_maximum_waiting_time() < waiting_time:
                return print(f"손님이 기다릴 수 없어 돌아갑니다.\n현재 대기 시간 {customer.get_waited_time()}분 / 대기 가능 시간 "
                      f"{waiting_time}분")
            else:
                __class__.waiting_customers.append(customer)

        #일반적인 경우라면.
        #테이블배정 / 요리사 지정

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
    def is_table_full()-> bool:
        if all(TableManager.table_queue):
            return True
        return False

    @staticmethod
    def is_all_the_cooks_cooking() -> bool:

        # 모든 요리사가 요리중인지 확인한다
        if Kitchen.all_the_cooks_cooking():
          return True
        return False

    def update(self):
        pass


class Restaurant:

    # 손님 방문 주기
    visiting_period = 15
    table_amount = 20
    cooks_number = 3

    @staticmethod
    def init(customer_visiting_period : int):
        __class__.visiting_period = customer_visiting_period

    @staticmethod
    def run():
        RestaurantManager.init()
        TableManager.init(__class__.table_amount)
        Kitchen.init(__class__.cooks_number)
        elapsed_time = 0
        while elapsed_time <= 720:
            elapsed_time += 1

            if Kitchen.cooks:
                for cook in Kitchen.cooks:
                    if cook.update():
                        Kitchen.cooks[cook.get_cook_number()-1].set_is_cooking()


            if RestaurantManager.waiting_customers:
                RestaurantManager.update_waiting_customers()

                #TODO-대기 시간만을 +1해주는 것이 아닌 매 순회마다 요리사가 비어있는지를 체크해서 요리사에게 요청을 전달하도록 하기.

            if elapsed_time % __class__.visiting_period == 0:
                new_customer = RestaurantManager.receive_customer(Customer(elapsed_time))


            # #어디 붙일지 필요/ 필요 없을듯...
            # if not Kitchen.all_the_cooks_cooking():
            #     for cook in Kitchen.cooks:
            #         if not cook.is_cooking():
            #             cook.set_is_cooking()


Restaurant.init(15)
Restaurant.run()