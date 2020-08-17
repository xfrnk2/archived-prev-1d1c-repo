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
        #다시 생각
        self.__is_bill_waiting: bool = False
        self.__is_billing: bool = False
        self.__bill_waiting_time = None
        self.__possible_waiting_time = None # 0?

    def change_is_billing_status(self):
        self.__is_billing = not self.__is_billing

    def change_is_bill_waiting_status(self):
        self.__is_bill_waiting = not self.__is_bill_waiting

    def set_waiting_time(self, value):
        self.__bill_waiting_time = value

    def set_possible_waiting_time(self, value):
        self.__possible_waiting_time = value

    def set_attribute(self, customer_info: tuple):
        self.__customer_number, self.__food_num, self.__food_eating_time = customer_info

    def get_request(self) -> tuple:
        return self.__customer_number, self.__food_num #손님번호, 음식번호

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

    def get_is_billing(self) -> bool:
        return self.__is_billing

    def get_is_bill_waiting(self) -> bool:
        return self.__is_bill_waiting

    def update(self):
        if self.__is_eating:
            self.__food_eating_time -= 1
            if self.__food_eating_time == 0:
                # 손님이 음식을 다 먹음
                return True
        return False



    def change_is_eating_status(self):
        self.__is_eating = not self.__is_eating


class CashDesk:


    def __init__(self, billing_time):
        self.__customer_number = None
        self.__billing_time = billing_time
        self.__elapsed_billing_time = 0
        self.__is_working = False

    def receive_customer(self, customer : Customer):
        self.__customer_number = customer.get_request()[0]

    def update(self): #업데이트 후 새로운 계산대 손님 배정하는 순서로 감.
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
    bill_waiting_time = None
    cash_desk_num = None
    cash_desk_object = None

    @staticmethod
    def init(waiting_time, cash_desk):

        __class__.bill_waiting_queue = []
        __class__.bill_waiting_time = waiting_time
        __class__.cash_desk_num = cash_desk
        __class__.cash_desk_object = CashDesk(billing_time = waiting_time)

    @staticmethod
    def receive_customer(customer):
        if not customer.get_is_billing() and not customer.get_is_bill_waiting():

            customer.change_is_bill_waiting_status()
            customer.set_waiting_time(__class__.bill_waiting_time)
            __class__.bill_waiting_queue.append(customer)

    @staticmethod
    def update():
        if __class__.cash_desk_object.update():
            print(f"{__class__.cash_desk_object.get_customer_info}번 손님 내보내기")

        if __class__.bill_waiting_queue and not __class__.cash_desk_object.is_working():
            __class__.cash_desk_object.receive_customer(__class__.bill_waiting_queue.pop(0))
            __class__.cash_desk_object.change_cash_desk_status()





class TableManager:

    table_queue = None

    @staticmethod
    def init(table_amount):
        __class__.table_queue = [0]*(table_amount) # 1번 테이블에서부터 시작하기 위해 0번은 비워두기로 했다.



    @staticmethod
    def set_customer(customer:Customer):
        for table_number, table in enumerate(__class__.table_queue):
            if table:
                __class__.table_queue[table_number] = customer
                return table_number

    @staticmethod
    def customer_get_food(info):
        table_number, customer_number, food_number = info
        if __class__.table_queue[table_number].get_request() == (customer_number, food_number):
            #좌석에 앉은 손님이 식사중 상태로 바뀐다.
            __class__.table_queue[table_number].change_is_eating_status()
            return True
        else:
            return False

    @staticmethod
    def update():
        for customer in __class__.table_queue:
            if customer.update():
                #손님이 음식을 다먹었음
                customer.change_is_eating_status()

                BillManager.receive_customer(customer)
                #계산대로 가자.



class Cook:
    def __init__(self, number):
        self.__cook_number = number
        self.__food_number = None
        self.__cooking_time = None
        self.__customer_number = None
        self.__table_number = None
        self.__is_cooking = False

    def set_request(self, request): #업데이트보다 나중에 와야함
        self.__table_number, self.__customer_number, self.__food_number, self.__cooking_time = request
        self.__is_cooking= not self.__is_cooking

    def get_cook_number(self):
        return self.__cook_number

    def update(self)-> bool: #업데이트가 True면 serve_food_to_custonmer를 실행
        if self.__is_cooking:
            self.__cooking_time -= 1
            if self.__cooking_time == 0:

                return True

        return False

    def serve_food_to_customer(self):
        self.__is_cooking = not self.__is_cooking
        self.reset_cook()
        return self.__table_number, self.__customer_number,  self.__food_number
        #다시 작성 필요

    def reset_cook(self):
        self.__table_number, self.__food_number, self.__customer_number, self.__cooking_time = None, None, None, None

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
            return print(f"손님이 기다릴 수 없어 돌아갑니다.\n현재 대기 시간 {customer.get_waited_time()}분 / 대기 가능 시간 "
                  "0분")

        if __class__.is_all_the_cooks_cooking():

            waiting_time = customer.get_food_waiting_time() + Kitchen.get_min_cooking_time()
            if customer.get_maximum_waiting_time() < waiting_time:
                return print(f"손님이 기다릴 수 없어 돌아갑니다.\n현재 대기 시간 {customer.get_waited_time()}분 / 대기 가능 시간 "
                      f"{waiting_time}분")
            else:
                customer.set_possible_waiting_time = waiting_time
                return __class__.waiting_customers.append(customer)

        #일반적인 경우라면.
        #테이블배정 / 요리사 지정



    @staticmethod
    def assignment_customer_to_cook(customer : Customer):
        table_num = TableManager.set_customer(customer)

        for cook in Kitchen.cooks:
            if not cook.is_cooking():
                customer_num, customer_food_num = customer.get_request()
                cook.set_request((table_num, customer_num, customer_food_num, __class__.food_cooking_time[customer_num]))
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


class Restaurant:

    # 손님 방문 주기
    visiting_period = 15
    table_amount = 20
    cooks_number = 3
    billing_period = 5
    cash_desk_number = 1

    @staticmethod
    def init(customer_visiting_period : int):
        __class__.visiting_period = customer_visiting_period

    @staticmethod
    def run():
        RestaurantManager.init()
        TableManager.init(__class__.table_amount)
        Kitchen.init(__class__.cooks_number)
        BillManager.init(__class__.billing_period, __class__.cash_desk_number)

        elapsed_time = 0



        while elapsed_time <= 720:
            elapsed_time += 1


            TableManager.update()


            #대기큐의 손님들 대기 시간을 +1 시킨다.
            if RestaurantManager.waiting_customers:
                RestaurantManager.update_waiting_customers()
            #요리사가 비어있다면 대기큐의 손님의 대기시간
            if Kitchen.cooks:
                for cook in Kitchen.cooks:
                    if cook.update(): #요리를 하고 있는지 확인해서 하고 있다면 조리시간이 0이 되었을 경우 True를 리턴한다.
                        table_and_customer_info = cook.serve_food_to_customer() #전달할 손님과 테이블에 대한 정보를 얻어온다.

                        if TableManager.customer_get_food(table_and_customer_info): #테이블 손님과 요리사의 info간의 값이 일치하는지 확인한다.

                            # 손님의 식사시간이 줄어들수 있도록 한다.

                            #RestaurantManager.assignment_customer_to_cook(customer)??



                #TODO-대기 시간만을 +1해주는 것이 아닌 매 순회마다 요리사가 비어있는지를 체크해서 요리사에게 요청을 전달하도록 하기.
            # 새로운 손님을 받는다.
            if elapsed_time % __class__.visiting_period == 0:
                new_customer = RestaurantManager.receive_customer(Customer(elapsed_time))


            # #어디 붙일지 필요/ 필요 없을듯...
            # if not Kitchen.all_the_cooks_cooking():
            #     for cook in Kitchen.cooks:
            #         if not cook.is_cooking():
            #             cook.set_is_cooking()


Restaurant.init(15)
Restaurant.run()