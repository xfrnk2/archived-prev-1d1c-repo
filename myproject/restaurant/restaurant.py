from random import randrange
from customer import Customer
from table import TableManager
from kitchen import Kitchen
from bill import BillManager

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
                if finished_order_queue:
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
