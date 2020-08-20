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

        if __class__.table_quantity <= len(self.__waiting_customers):

            n = len(self.__waiting_customers) - __class__.table_quantity
            table_detail = []

            for waiting_customer in self.__waiting_customers:
                left_waiting_time = waiting_customer.get_required_waiting_time() - waiting_customer.get_elapsed_waiting_time()
                total_required_time = waiting_customer.get_total_required_time()
                table_detail.append(left_waiting_time + total_required_time)



            required_waiting_time = sorted(table_detail)[n]

        else:
            n = len(self.__waiting_customers)

            table_detail = []
            for customer in self.__table_manager.get_table_queue():
                if customer.get_is_eating():
                    table_detail.append(customer.get_food_eating_time() - customer.get_elapsed_eating_time())

                else:
                    #########
                    # result = 0
                    # waiting_copy = self.__waiting_customers
                    # group = sorted(self.__kitchen.get_cooks_current_cooking_time())
                    # waiting_copy += [new_customer.get_cooking_time()]
                    # while waiting_copy:
                    #     target= group.pop(0)
                    #     result += target
                    #     group = [i - target for i in group]
                    #     group.append(waiting_copy.pop(0))
                    #     group.sort()

                    ############



                    # print(customer.get_waited_time_for_food())에서 사단이 난다..

                    table_detail.append(customer.get_food_cooking_time() + customer.get_food_eating_time() - customer.get_waited_time_for_food() )
            required_waiting_time = sorted(table_detail)[n]

        if new_customer.get_maximum_waiting_time() < required_waiting_time:
            print(f"대기를 못하니 돌아간다. 대기가능시간 {required_waiting_time}")
            return False

        # TODO - 현재 손님을 포함하지 않고 대기자수(n)을 계산한다면, 0명-> 0번째인덱스, 1명 -> 1번째 인덱스로 가능
        # TODO - 만약 현 대기자의 수가 테이블의 갯수 이상인 경우, xxx(현존 대기자 - 테이블수)번째xxx 현존 대기자의 남은 대기시간+
        # TODO -  요리시간+식사시간 중 최소값을 반환 -> 남은 대기자들의 (남은 대기시간+(요리+식사의 시간))을 구하여 그중 최소값 반환
        #
        # TODO - 만약 21번째 대기자인 경우라면 현존 대기자들의 요리시간+식사시간 중 1번째 인덱스 값을 반환
        #
        # TODO-1. 현재 손님을 포함하지 않고 대기자수(n)를 계산, 테이블에 착석중인 손님들의
        # TODO-  일어나기까지의 시간을 구한 오름차순 정렬 리스트에서 (n)번째의 인덱스에 해당하는 값만큼 기다리게 한다.

        else:
            new_customer.set_required_waiting_time(required_waiting_time)
            print(f"대기가능시간 {required_waiting_time}")
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

        print(f"{customer_number}번 손님이 {table_num}번 테이블에 앉습니다.")
        print(f"{customer_number}번 손님이 {food_num}번 요리"
              f" ({self.__food_name[food_num]})를 주문합니다.")
        self.__kitchen.assign_customer_to_cook(customer, table_num)

    def receive_customer(self, customer : Customer):
        self.__waiting_customers.append(customer)


    def waiting_update(self):
        if self.__waiting_customers:
            customer_count = 0

            for customer in self.__waiting_customers:
                customer.waiting_update()

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
                    if self.is_possible_to_wait(new_customer):
                        self.receive_customer(new_customer)

                    else:
                        #손님은 돌아감
                        print("기다릴 수 없어서 돌아갑니다")
                        #print(f"대기시간 : 00분, 대기가능시간 : {required_waiting_time}")

                else:
                    self.customer_entrance(new_customer)




