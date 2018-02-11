# coding=utf-8


from week6.guest import Guest
from week6.menu import Menu


# FIXME - Chef 와 Chefs 의 관계에 대해서 해당 파일에 적어놓은 주석을 참고하세요.
class Table:
    table = 20


class TableManager:

    def __init__(self):

        self.__tables = [0 for _ in range(Table.table)]
        self.__menu = Menu()
        self.__data = Guest()

    def simulate(self):
        number = self.__data.guest_number
        menu = self.__menu.set_menu
        order_number = self.__menu.get_order_number

        tables = self.__tables

        for y in range(Table.table):
            if tables[y] == 1:
                continue
            if y == Table.table - 1:
                if tables[y] == 1:
                    pass
                # TODO - 더이상 손님을 받을 수 없는 상황이 발생.
                # TODO - 요리사와 계산대의 소요 시간을 합산하여 총 대기시간을 계산한다.
                else:
                    tables[y] = 1
                    self.__menu.place_order()
                    print(f"{number}번 손님이 f{y}번 테이블에 앉습니다.")

                    print(f"{y}번 손님이 {order_number}번 요리{menu})를 주문합니다.")

            # FIXME - 이와 같이 코드를 작성하고 실제 실행하면 무슨 일이 벌어질까요?
            else:

                tables[y] = 1
                self.__menu.place_order()

                print(f"{number}번 손님이 {y}번 테이블에 앉습니다.")

                print(f"{y}번 손님이 {order_number}번 요리{menu}를 주문합니다.")
