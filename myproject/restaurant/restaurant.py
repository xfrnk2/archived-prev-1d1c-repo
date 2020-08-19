from abc import *
from random import randrange

class SimulationObject(ABC):

    @abstractmethod
    def update(self):
        pass



class Customer(SimulationObject):

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



class CashDesk(SimulationObject):


    def __init__(self, billing_time):
        self.__customer_number = None
        self.__billing_time = billing_time
        self.__elapsed_billing_time = 0
        self.__is_working = False

    def receive_customer(self, customer : Customer):
        self.__customer_number = customer.get_request()[0]

    def update(self):
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


class BillManager(SimulationObject):

    def __init__(self, waiting_time, cash_desk):

        self.__bill_waiting_queue = []
        self.__cash_desk_num = cash_desk
        self.__cash_desk_object = CashDesk(billing_time = waiting_time)


    def receive_customer(self, customer: Customer):
        if not customer.get_is_billing() and not customer.get_is_bill_waiting():
            print(f"{customer.get_customer_number()}번 손님이 계산대 앞에 줄을 섭니다." )

            customer.change_is_bill_waiting_status()
            self.__bill_waiting_queue.append(customer)

    def update(self):
        if self.__cash_desk_object.update():
            print(f"{self.__cash_desk_object.get_customer_info()}번 손님이 계산을 마치고 레스토랑을 떠났습니다.")

        if self.__bill_waiting_queue and not self.__cash_desk_object.is_working():
            self.__cash_desk_object.receive_customer(self.__bill_waiting_queue.pop(0))
            self.__cash_desk_object.change_cash_desk_status()



class TableManager(SimulationObject):


    def __init__(self, table_amount):
        self.__table_queue = [0]*(table_amount)

    def is_exist(self)-> bool:
        return any(self.__table_queue)

    def set_customer(self, customer:Customer):

        for table_number, table in enumerate(self.__table_queue):
            if not table:
                self.__table_queue[table_number] = customer
                return table_number
        return

    def getting_food(self, info: tuple):
        table_number, customer_number, food_number = info
        #table_number = int(table_number)

        if isinstance(self.__table_queue[table_number], Customer) and \
                self.__table_queue[table_number].get_request() == (customer_number, food_number):

                print(f"{customer_number}번 손님이 식사를 시작합니다.")
                self.__table_queue[table_number].change_status_is_eating()
        return

    def is_table_full(self)-> bool:
        if all(self.__table_queue):
            return True
        return False

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


class Cook(SimulationObject):
    def __init__(self, number):
        self.__cook_number = number
        self.__food_number = 0
        self.__cooking_time = 0
        self.__customer_number = 0
        self.__table_number = 0
        self.__is_cooking = False

    def set_request(self, request):
        self.__table_number, self.__customer_number, self.__food_number, self.__cooking_time = request
        self.__is_cooking= not self.__is_cooking

    def serve_food_to_customer(self)-> tuple:
        return int(self.__table_number), int(self.__customer_number),  int(self.__food_number)

    def reset_status(self):
        self.__table_number, self.__food_number, self.__customer_number, self.__cooking_time = 0, 0, 0, 0

    def is_cooking(self)-> bool:
        return self.__is_cooking

    def set_is_cooking(self):
        self.__is_cooking = not self.__is_cooking

    def get_left_cooking_time(self)-> int:
        return self.__cooking_time

    def update(self)-> bool:
        if self.__is_cooking:
            self.__cooking_time -= 1
            if self.__cooking_time == 0:
                self.__is_cooking = not self.__is_cooking
                return True
        return False



class Kitchen(SimulationObject):

    def __init__(self, cook_num):

        self.__cook_number = cook_num
        self.__cooks = [Cook(i) for i in range(1, cook_num+1)]
        self.__food_cooking_time = {1: 30, 2: 20, 3: 10, 4: 15}
        self.__food_name = {1: "스테이크", 2: "스파게티", 3: "마카로니", 4: "그라탱"}

    def all_the_cooks_cooking(self)-> bool:
        return all(cook.is_cooking() for cook in self.__cooks)

    def get_food_cooking_time(self, num)-> int:
        return self.__food_cooking_time[num]

    def get_cooks_current_cooking_time(self)-> list:
        return [cook.get_left_cooking_time() for cook in self.__cooks]

    def assign_customer_to_cook(self, customer : Customer, table_number : int):
        for cook in self.__cooks:
            if not cook.is_cooking() :
                customer_num, customer_food_num = customer.get_request()
                cook.set_request((table_number, customer_num, customer_food_num, self.__food_cooking_time[customer_food_num]))
                break



    def update(self)-> list:

        finished_order_queue = []

        for cook in self.__cooks:
            if cook.update():
                info = cook.serve_food_to_customer()
                table_num, customer_num, food_num = info

                print(f"{customer_num}번 손님의 {food_num}번 요리({self.__food_name[food_num]}) 조리가 끝났습니다.")
                cook.reset_status()

                finished_order_queue.append(info)

        return finished_order_queue


class Restaurant:

    def __init__(self, customer_visiting_period : int):
        billing_period = 5
        cash_desk_num = 1
        cooks_num = 3
        table_quantity = 20

        self.__visiting_period = customer_visiting_period
        self.__table_manager = TableManager(table_quantity)
        self.__kitchen = Kitchen(cooks_num)
        self.__bill_manager = BillManager(billing_period, cash_desk_num)

        self.__number_of_customers = 0
        self.__waiting_customers = []

        self.__food_name = {1: "스테이크", 2: "스파게티", 3: "마카로니", 4: "그라탱"}
        self.__food_eating_time = {1: 30, 2: 20, 3: 15, 4: 10}

    def customer_visiting(self, elapsed_time: int):
        self.__number_of_customers += 1
        new_customer = Customer(self.__number_of_customers, elapsed_time)

        print(f"{self.__number_of_customers}번째 손님이 시각 {elapsed_time} 분에 레스토랑에 도착했습니다.")
        return new_customer


    def receive_customer(self, customer : Customer):
        # food_num = randrange(1, 5)
        #
        # customer.set_attribute((food_num, self.__food_eating_time[food_num]))
        self.__waiting_customers.append(customer)


    def waiting_update(self):
        if self.__waiting_customers:
            customer_count = 0

            for customer in self.__waiting_customers:
                customer.waiting_update()
                if customer.get_required_waiting_time() <= customer.get_waited_time()  and not self.__kitchen.all_the_cooks_cooking():
                    customer_count += 1

                    table_num = self.__table_manager.set_customer(customer)
                    customer_number, food_number = customer.get_order()

                    print(f"{customer_number}번 손님이 {table_num}번 테이블에 앉습니다.")
                    print(f"{customer_number}번 손님이 {food_number}번 요리"
                          f" ({self.__food_name[food_number]})를 주문합니다.")

                    self.__kitchen.assign_customer_to_cook(customer, table_num)

            for _ in range(customer_count):
                self.__waiting_customers.pop(0)

    def run(self):

        elapsed_time = 0

        while elapsed_time < 720:

            elapsed_time += 1
            print(f"{elapsed_time}분 : 잔여 테이블 수 {self.__table_manager.get_table_left()}")
            print(f"현재 대기손님 : {len(self.__waiting_customers)}")

            current_number_of_cooks_cooking = len(list(
                filter(lambda cooking_time: 0 < cooking_time, self.__kitchen.get_cooks_current_cooking_time())))
            print(f"현재 요리중인 요리사 : {current_number_of_cooks_cooking}")

            table_target_customer_queue = self.__table_manager.update()
            for customer in table_target_customer_queue:
                self.__bill_manager.receive_customer(customer)

            self.__bill_manager.update()

            if self.__table_manager.is_exist():
                finished_order_queue = self.__kitchen.update()
                for order in finished_order_queue:
                    self.__table_manager.getting_food(order)

            self.waiting_update()

            if elapsed_time % self.__visiting_period == 0:
                new_customer = self.customer_visiting(elapsed_time)
                food_num = randrange(1, 5)
                new_customer.set_attribute((food_num, self.__food_eating_time[food_num]))

                required_time = 0


                if self.__waiting_customers:
                    pivot = len(self.__waiting_customers)

                    food_num = new_customer.get_order()[1]
                    food_cooking_time = self.__kitchen.get_food_cooking_time(food_num)

                    required_time = min([food_cooking_time] + sorted(self.__kitchen.get_cooks_current_cooking_time())[pivot:])

                else:
                    required_time = min(self.__kitchen.get_cooks_current_cooking_time())


                new_customer.set_required_waiting_time(required_time)
                checking = new_customer.get_maximum_waiting_time() < new_customer.get_required_waiting_time()

                if self.__table_manager.is_table_full() or (checking and self.__kitchen.all_the_cooks_cooking()):
                    print(f"손님이 기다릴 수 없어 돌아갑니다.\n현재 대기 시간 {new_customer.get_waited_time()}분 / 대기 가능 시간 "
                          f"{new_customer.get_required_waiting_time()}분")

                else:
                    print(f"기다릴 것으로 결정했고, {new_customer.get_required_waiting_time()}분 기다려야 합니다.")

                    if not self.__kitchen.all_the_cooks_cooking() and not self.__waiting_customers:

                        table_num = self.__table_manager.set_customer(new_customer)
                        assert type(table_num) is not None

                        customer_number, food_number = new_customer.get_order()

                        print(f"{customer_number}번 손님이 {table_num}번 테이블에 앉습니다.")
                        print(f"{customer_number}번 손님이 {food_number}번 요리"
                              f" ({self.__food_name[food_number]})를 주문합니다.")

                        self.__kitchen.assign_customer_to_cook(new_customer, table_num)

                    else:
                        self.receive_customer(new_customer)


if __name__ == "__main__":
    visiting_period = 5

    restaurant = Restaurant(visiting_period)
    for _ in range(1):
        restaurant.run()