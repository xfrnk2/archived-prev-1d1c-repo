"""
레스토랑을 시뮬레이션 해주세요.

손님은 3가지 조건이 있습니다.
도착 시간, 요리 주문 타입, 최대 대기 시간

일정 시간마다 무작위로 손님이 1명씩 도착합니다.
# TODO - 손님이 도착하면 화면에 손님이 도착했다는 문구를 출력해야 합니다.
# TODO - n번째 손님이 시각 xx 분에 레스토랑에 도착했습니다.

이 손님의 최대 대기 시간을 15분~40분까지 무작위로 설정합니다.
레스토랑의 현재 운영 상태로부터 대기 시간을 계산해서,
이 손님의 최대 대기 시간을 초과할 경우 손님은 기다리지 않고 그대로 돌아갑니다.
# TODO - 돌아갈 경우 화면에 이 손님이 돌아간다는 문구를 출력해야 합니다.
# TODO - 손님이 기다릴 수 없어 돌아갑니다.
# TODO - 현재 대기 시간 xx분 / 대기 가능 시간 xx분

손님이 최대 대기 시간 미만을 기다릴 경우, 대기 시간이 끝나면 손님은 자리에 착석을 하고
무작위로 요리를 1가지 주문합니다.
# TODO - 손님이 요리를 주문하면, 요리를 주문했다는 문구를 출력해야 합니다.
# TODO - n번 손님이 x번 테이블에 앉습니다.
# TODO - n번 손님이 i번 요리(oooo)를 주문합니다.

조리가 완료 되면 요리가 손님의 테이블에 도착하고, 손님은 식사를 시작합니다.
# TODO - 손님이 식사를 시작하면, 해당 문구를 출력해야 합니다.
# TODO - n번 손님의 i번 요리(oooo) 조리가 끝났습니다.
# TODO - n번 손님이 식사를 시작합니다.

식사가 완료 되면 손님은 계산대 앞에 가서 대기합니다.
# TODO - n번 손님이 식사를 마쳤습니다.
# TODO - n번 손님이 계산대 앞에 줄을 섭니다.

계산이 완료 되면 손님은 떠납니다.
# TODO - n번 손님이 계산을 마치고 레스토랑을 떠났습니다.


요리는 4가지 종류가 있습니다.

1. 스테이크 - 조리 시간 30분, 먹는 시간 30분
2. 스파게티 - 조리 시간 20분, 먹는 시간 20분
3. 마카로니 - 조리 시간 10분, 먹는 시간 15분
4. 그라탱   - 조리 시간 15분, 먹는 시간 10분

레스토랑에는 요리사가 3명이 있습니다.
한 요리사는 한 번에 1가지 요리를 할 수 있습니다.

레스토랑에는 테이블이 20개 있습니다.
모든 손님은 각각 한 테이블에 한 명씩 앉습니다.

계산대는 1개가 있습니다.
계산대에서는 홀 매니저가 계산을 하며 계산을 하는데는 5분이 소요 됩니다.

테이블이 비어있지 않으면 손님을 더 받을 수 없습니다.

하루 일과 시간 (720분) 동안 레스토랑의 장사를 시뮬레이션 해주세요.

모든 시간은 분 단위로 계산합니다.

이 과제는 그대로 심화 되어 다음 주로 계속 이어집니다.
언제나 코드를 작성할 때는 새로운 요구사항에 유연하게 대처 가능하도록
확장 가능하고 수정 및 유지보수가 편리하도록 고민해주세요.

"""

import random


class Guest:
    def __init__(self):
        self.arr_time = 0
        self.menu = random.randrange(1, 5)
        self.waiting_time = random.randrange(15, 41)
        self.number = 0
        self.table_number = 0
        self.eating_time = 0

    def set_eating_time(self):
        if self.menu == 1:
            self.eating_time = 30
        if self.menu == 2:
            self.eating_time = 20
        if self.menu == 3:
            self.eating_time = 15
        if self.menu == 4:
            self.eating_time = 10

    def __repr__(self):
        return self.return_menu_name()

    def return_menu_name(self):
        if self.menu == 1:
            return "스테이크"
        if self.menu == 2:
            return "스파게티"
        if self.menu == 3:
            return "마카로니"
        if self.menu == 4:
            return "그라탕"

class Chef:
    def __init__(self):
        self.time = 1
        self.table_number = 0




def simulator():
    timer = 0
    cal_wating = {}
    guest_number = 0
    guests = {}
    tables = {}
    chefs = {}
    while True:
        timer += 1
        print(f"레스토랑 시작한지 {timer}분 흘렀습니다")
        if timer == 720:
            break

        if timer % 20 == 0 and timer >= 1:

            guest_number += 1
            guests[guest_number] = Guest()
            guests[guest_number].arr_time = timer
            guests[guest_number].number = guest_number
            guests[guest_number].set_eating_time()
            print(f"{guest_number}번째 손님이 시각 {timer}분에 레스토랑에 도착하였습니다")

        for y in range(guest_number, guest_number + 1):

            target = guests.get(y)
            if target is None:
                continue
            else:
                if 20 == len(tables):
                    print(f"{target.number}번째 손님이 기다릴 수 없어 돌아갑니다")
                    del guests[guest_number]
                target.waiting_time -= 1

            for z in range(1, 21):

                if z in tables:
                    continue
                else:
                    tables[z] = target

                    target.table_number = z
                    print(
                        f"{target.number}번 손님이 {z}번 테이블에 앉습니다")
                    print(
                        f"{target.number}번 손님이 {target.menu}번 요리"
                        f" {target.return_menu_name()}을(를) 주문하였습니다")
                    del guests[y]

                    for i in range(1, 4):
                        if i in chefs:
                            continue
                        else:
                            chefs[i] = Chef()
                            chefs[i].table_number = z
                            option = tables[chefs[i].table_number]
                            if option.menu == 1:
                                chefs[i].time += 30

                            if option.menu == 2:
                                chefs[i].time += 20

                            if option.menu == 3:
                                chefs[i].time += 10

                            if option.menu == 4:
                                chefs[i].time += 15
                            break
                    break
            for i in range(1, 4):
                if i in chefs:
                    chefs[i].time -= 1
                    if chefs[i].time == 0:
                        target2 = tables[chefs[i].table_number]
                        print(
                            f"{target2.number}번 손님의 {target2.menu}번 요리"
                            f" {target2.return_menu_name()}의 조리가 끝났습니다")
                        del chefs[i]
                else:
                    pass

            break






simulator()
