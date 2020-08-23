from random import randrange
from customer import Customer
from table import TableManager
from kitchen import Kitchen
from bill import BillManager
import sys

class Restaurant:
    table_quantity = 20

    def __init__(self, customer_visiting_period : int):
        billing_period = 5
        cash_desk_num = 1
        cooks_num = 3


        self.__visiting_period = customer_visiting_period
        self.__table_manager = TableManager(__class__.table_quantity)
        self.__kitchen = Kitchen(cooks_num)
        self.__bill_manager = BillManager(billing_period, cash_desk_num)

        self.__number_of_customers = 0
        self.__waiting_customers = []

        self.__food_name = {1: "스테이크", 2: "스파게티", 3: "마카로니", 4: "그라탱"}
        self.__food_eating_time = {1: 30, 2: 20, 3: 15, 4: 10}
        self.__food_cooking_time = {1: 30, 2: 20, 3: 10, 4: 15}

    def is_possible_to_wait(self, new_customer: Customer):
        n = 0
        group = []
        group2 = []
        for table in self.__table_manager.get_table_queue():
            left_time = table.get_all_time() - (table.get_elapsed_waited_time_for_food() + table.get_elapsed_eating_time())

            if left_time < new_customer.get_maximum_waiting_time():
                n += 1
                group.append(left_time)
            else:
                group2.append(left_time)
        print(f"n : {n}, group : {group}, group2 : {group2}")
        if self.__waiting_customers:
            if len(self.__waiting_customers) < n:
                new_customer.set_new_left_time_to_table(sorted(group)[len(self.__waiting_customers)])
                return True

        else:
            if 1 <= n:
                new_customer.set_new_left_time_to_table(min(group))
                return True

        # new_customer.set_new_left_time_to_table(group2[len(self.__waiting_customers) - n])
        v = sorted(group2)[len(self.__waiting_customers) - n]
        new_customer.set_new_left_time_to_table([v])
        return False

        #
        # if new_customer.get_maximum_waiting_time() < required_waiting_time:
        #     return False
        #
        # else:
        #     return True
            # 착석 후 주문


    def customer_visiting(self, elapsed_time: int):
        self.__number_of_customers += 1
        new_customer = Customer(self.__number_of_customers, elapsed_time)

        print(f"{self.__number_of_customers}번째 손님이 시각 {elapsed_time} 분에 레스토랑에 도착했습니다.")
        return new_customer

    def get_time_until_being_allocated_to_cook(self):
        result = 0
        q = self.__kitchen.get_order_queue()
        if q:
            q = [self.__food_cooking_time[o[2]] for o in q]
            group = self.__kitchen.get_cooks_current_cooking_time()
            q.append(0)

            while q:
                group.sort()
                target = group.pop(0)
                result += target
                group = [i - target for i in group]

                group.append(q.pop(0))
        return result

    def customer_entrance(self, customer: Customer):
        # 착석후 주문

        food_num = randrange(1, 5)
        food_eating_time = self.__food_eating_time[food_num]
        food_cooking_time = self.__food_cooking_time[food_num]
        customer.set_attribute((food_num, food_eating_time, food_cooking_time))
        # 손님 주문 정보 설정

        table_num = self.__table_manager.set_customer(customer)
        customer_number = customer.get_customer_number()

        result = self.get_time_until_being_allocated_to_cook()
        print(f"요리사에게 배당되기까지의 시간{result}")

        customer.set_all_time(result+customer.get_food_cooking_time() + customer.get_food_eating_time())


        print(f"{customer_number}번 손님이 {table_num}번 테이블에 앉습니다.")
        print(f"{customer_number}번 손님이 {food_num}번 요리"
              f" ({self.__food_name[food_num]})를 주문합니다.")

        self.__kitchen.get_order_from_new_customer(customer, table_num)

    def receive_customer(self, customer : Customer):
        self.__waiting_customers.append(customer)
    def pop_queue(self, value):
        if value == 0:
            pass
        else:
            for _ in range(value):
                print("지워진다~")
                self.__waiting_customers.pop(0)
    
    def waiting_update(self):
        if self.__waiting_customers:
            customer_count = 0

            for customer in self.__waiting_customers:
                customer.waiting_update()
                print(f"{customer.get_customer_number()}번 손님인데")

                print(f"{customer.get_elapsed_waiting_time()} 만큼 기다렸꼬")
                print(f"{customer.get_new_left_time_to_table()}가 처음 대기 남은시간이다")
            for customer in self.__waiting_customers:


                print([c.get_customer_number() for c in self.__waiting_customers])
                print(f"{customer.get_customer_number()}번 손님인데")
                print(f"{customer.get_elapsed_waiting_time()} 만큼 기다렸꼬")
                print(f"{customer.get_new_left_time_to_table()}가 처음 대기 남은시간이다")
                if customer.get_elapsed_waiting_time() < customer.get_new_left_time_to_table():
                    print("때가 아니거늘.")
                    break
                if customer.get_elapsed_waiting_time() > customer.get_new_left_time_to_table():
                    print("웃기지마라!!")




                if customer.get_elapsed_waiting_time() == customer.get_new_left_time_to_table() and not self.__table_manager.is_table_full():
                    print(f"그캄 테이블 얼마나 남았나?{self.__table_manager.get_table_left()}")
                    self.customer_entrance(customer)
                    customer_count += 1
                    print(f"지금 테이블 꽉찻나?{self.__table_manager.is_table_full()}")
                    print(f"그캄 테이블 얼마나 남았나?{self.__table_manager.get_table_left()}")

            print("커스토머카운트는")
            print(customer_count)
            self.pop_queue(customer_count)

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

                if self.__table_manager.is_table_full():
                    if self.is_possible_to_wait(new_customer):

                        print(f"대기가능시간 {new_customer.get_new_left_time_to_table()}")
                        self.receive_customer(new_customer)
                    else:
                        #self.customer_entrance(new_customer)
                        #손님은 돌아감
                        print(f"손님이 기다릴 수 없어 돌아갑니다.\n현재 대기 시간 {new_customer.get_elapsed_waiting_time()}분 / 대기 가능 시간 "
                              f"{new_customer.get_new_left_time_to_table()}분")
                        print(f"손님 최대 대기시간 : {new_customer.get_maximum_waiting_time()}")
                else:
                    self.customer_entrance(new_customer)

            self.__kitchen.start_cooking_update()


