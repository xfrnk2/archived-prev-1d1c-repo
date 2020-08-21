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

    def is_possible_to_wait(self, new_customer: Customer)-> bool:

        required_waiting_time = 0

        waiting_copy = [c.get_food_cooking_time() for c in self.__waiting_customers]
        group = self.__kitchen.get_cooks_current_cooking_time()
        waiting_copy += [new_customer.get_food_cooking_time()]
        while waiting_copy:
            group.sort()
            target = group.pop(0)
            required_waiting_time += target
            group = [i - target for i in group]
            group.append(waiting_copy.pop(0))

        new_customer.set_required_waiting_time(required_waiting_time)

        if new_customer.get_maximum_waiting_time() < required_waiting_time:
            return False

        else:
            return True
            # 착석 후 주문

    def customer_visiting(self, elapsed_time: int):
        self.__number_of_customers += 1
        new_customer = Customer(self.__number_of_customers, elapsed_time)

        print(f"{self.__number_of_customers}번째 손님이 시각 {elapsed_time} 분에 레스토랑에 도착했습니다.")
        return new_customer


    def customer_entrance(self, customer: Customer):
        # 착석후 주문

        food_num = randrange(1, 5)
        food_eating_time = self.__food_eating_time[food_num]
        food_cooking_time = self.__food_cooking_time[food_num]
        customer.set_attribute((food_num, food_eating_time, food_cooking_time))
        # 손님 주문 정보 설정

        table_num = self.__table_manager.set_customer(customer)
        customer_number = customer.get_customer_number()

        ####
        q = self.__kitchen.get_order_queue()
        q = [self.__food_cooking_time[o[2]] for o in q]
        group = self.__kitchen.get_cooks_current_cooking_time()
        q.append(0)
        result = 0
        while q:
            group.sort()
            target = group.pop(0)
            result += target
            group = [i - target for i in group]

            group.append(q.pop(0))
            print(group)

        print(result)
        print(f"요리사에게 배당되기까지의 시간{result}")

        #####





        print(f"{customer_number}번 손님이 {table_num}번 테이블에 앉습니다.")
        print(f"{customer_number}번 손님이 {food_num}번 요리"
              f" ({self.__food_name[food_num]})를 주문합니다.")
        #예상소요시간 출력하기, 키친의 대기큐에 넣어두기
        self.__kitchen.get_order_from_new_customer(customer, table_num)
        #self.__kitchen.start_cooking_update()
        #self.__kitchen.assign_customer_to_cook(customer, table_num)

    def receive_customer(self, customer : Customer):
        self.__waiting_customers.append(customer)


    def waiting_update(self):
        if self.__waiting_customers:
            customer_count = 0

            for customer in self.__waiting_customers:
                customer.waiting_update()

                print("웨이팅업데이트이후,")
                print(f"{customer.get_elapsed_waiting_time()}")
                print(f"{customer.get_required_waiting_time()}")
                print([c.get_customer_number() for c in self.__waiting_customers])
                if customer.get_elapsed_waiting_time() == customer.get_required_waiting_time() and not self.__table_manager.is_table_full():

                    self.customer_entrance(customer)
                    customer_count += 1

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

                if self.__table_manager.is_table_full():
                    print("테이블이 꽉차서 돌아갑니다.")
                else:
                    if self.is_possible_to_wait(new_customer):


                        
                        if self.__waiting_customers:
                            print(f"대기가능시간 {new_customer.get_required_waiting_time()}")
                            print("먼저 대기하시는 분이 있으니 대기큐로 집어넣는다")
                            self.receive_customer(new_customer)
                        else:
                            print("대기하시는 분이 없으므로 테이블에 착석하여 주문한다")
                            self.customer_entrance(new_customer)
                            # q = self.__kitchen.get_order_queue()
                            # q = [self.__food_cooking_time[o[2]] for o in q]
                            # group = self.__kitchen.get_cooks_current_cooking_time()
                            # q.append(0)
                            # result = 0
                            # while q:
                            #     group.sort()
                            #     target = group.pop(0)
                            #     result += target
                            #     group = [i - target for i in group]
                            #
                            #     group.append(q.pop(0))
                            #     print(group)
                            #
                            # print(result)
                            # print(f"요리사에게 배당되기까지의 시간{result}")



                    else:
                        #손님은 돌아감
                        print(f"손님이 기다릴 수 없어 돌아갑니다.\n현재 대기 시간 {new_customer.get_elapsed_waiting_time()}분 / 대기 가능 시간 "
                              f"{new_customer.get_required_waiting_time()}분")
                        print(f"손님 최대 대기시간 : {new_customer.get_maximum_waiting_time()}")

                # else:
                #      self.customer_entrance(new_customer)

            self.__kitchen.start_cooking_update()


