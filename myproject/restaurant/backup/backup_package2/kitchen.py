from restaurant_object import RestaurantObject
from customer import Customer
from cook import Cook

class Kitchen(RestaurantObject):

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

