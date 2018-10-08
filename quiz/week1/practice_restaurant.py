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

메뉴 순서 1 2 3 4번
 먹는 시간 10 15 20 25
요리시간 10 15 20 25
손님 대기시간과 오는 시간 수정해놈
테이블 비었는지 확인하기
"""

import random


def tic(minute):
    print(minute, "분이 지났습니다")

def anounce(guest_number):
    print(guest_number, "번 손님이 도착했어요")



class Guest():
    def __init__(self):
        self.my_number = None
        self.menu = None
        self.eating_time = None
        self.can_waiting_time = 10
        self.eating_or_not_eating = False
        self.table_number = None

    def minus_time(self):
        self.can_waiting_time -= 1


class Cooker:
    def __init__(self):
        self.cooking_time = None
        self.what_is_number = None
        self.table_number = None
def main():
    tick = 1
    guest_go_you_number = 1
    guest_box = []
    waiting_guest_box = {}
    table_box = {}
    table_cooking_waiting_box = {}
    cooker_box = {}

    while tick <= 720:



        for i in range(50):  # 게스트숫자만큼 리스트 순회
            if i in waiting_guest_box:
                waiting_guest_box[i].can_waiting_time -= 1  # 대기시간 감소시키기


            if i in waiting_guest_box:
                if waiting_guest_box[i].can_waiting_time == -1:
                    print(f"{waiting_guest_box[i].my_number}번 손님이 기다릴 수 없어 돌아갑니다")
                    # 다되면 집에보내기
                    waiting_guest_box.pop(i)

            if len(table_box) < 5:
                for x in range(5):
                    if x not in table_box:
                        for z in range(50):
                            if z in waiting_guest_box:
                                table_box[x] = waiting_guest_box[z]  # 일단 더해주고
                                waiting_guest_box.pop(z)  # 다음은 원래 자리에서 제거해준다

                                table_box[x].table_number = x  # 테이블 넘버를 저장해줌

                                table_box[x].menu = random.randrange(1, 5)
                                if len(cooker_box) < 3:

                                    for y in range(3):
                                        if y not in cooker_box:
                                            cooker_box[y] = (Cooker())
                                            if table_box[x].menu == 1:
                                                table_box[x].eating_time = 11
                                                cooker_box[
                                                    y].cooking_time = 11  # 요리시간 추가
                                                cooker_box[y].what_is_number = \
                                                table_box[x].my_number
                                                cooker_box[y].table_number = x
                                            if table_box[x].menu == 2:
                                                table_box[x].eating_time = 16
                                                cooker_box[y].cooking_time = 16
                                                cooker_box[y].what_is_number = \
                                                table_box[
                                                    x].my_number
                                                cooker_box[y].table_number = x
                                            if table_box[x].menu == 3:
                                                table_box[x].eating_time = 21
                                                cooker_box[y].cooking_time = 21
                                                cooker_box[y].what_is_number = \
                                                table_box[
                                                    x].my_number
                                                cooker_box[y].table_number = x
                                            if table_box[x].menu == 4:
                                                table_box[x].eating_time = 26
                                                cooker_box[y].cooking_time = 26
                                                cooker_box[y].what_is_number = \
                                                table_box[
                                                    x].my_number
                                                cooker_box[y].table_number = x

                                    print(
                                        f"{table_box[x].my_number}번 손님이 {x}번 테이블에 앉아 {table_box[x].menu}번 메뉴를 주문했어요")
                                    break
                                if len(cooker_box) == 3:
                                    print(
                                        f"{x}번 테이블에 앉은 {table_box[x].my_number}번 손님은 기다려야해! 요리사가 모두 요리중")
                                    for i in range(0, 50):  # 최대 대기 가능 인원 50명
                                        if i not in table_cooking_waiting_box:
                                            table_cooking_waiting_box[i] = table_box[x]
                                            break

                                break
                        break
                    else:
                        pass



        tic(tick)


        for i in range(len(table_cooking_waiting_box)):
            if i in table_cooking_waiting_box:
                for j in range(3):
                    if j not in cooker_box:
                        cooker_box[j] = (Cooker())

                        target = table_box[table_cooking_waiting_box[i].table_number]

                        if target.menu == 1:
                            target.eating_time = 11
                            cooker_box[j].cooking_time = 11  # 요리시간 추가
                            cooker_box[j].what_is_number = target.my_number
                            cooker_box[j].table_number = target.table_number
                        if target.menu == 2:
                            target.eating_time = 16
                            cooker_box[j].cooking_time = 16  # 요리시간 추가
                            cooker_box[j].what_is_number = target.my_number
                            cooker_box[j].table_number = target.table_number
                        if target.menu == 3:
                            target.eating_time = 21
                            cooker_box[j].cooking_time = 21  # 요리시간 추가
                            cooker_box[j].what_is_number = target.my_number
                            cooker_box[j].table_number = target.table_number
                        if target.menu == 4:
                            target.eating_time = 26
                            cooker_box[j].cooking_time = 26  # 요리시간 추가
                            cooker_box[j].what_is_number = target.my_number
                            cooker_box[j].table_number = target.table_number
                        print(f"기다리던 {target.my_number}번 손님의 요리가 요리되기 시작했어요")
                        table_cooking_waiting_box.pop(i)

                        break


        if tick % 5 == 0:  # 손님은 10분에 한명 도착
            guest_box.append(Guest())
            guest_box[-1].my_number = guest_go_you_number
            guest_go_you_number += 1  # 새로운 손님 등록, 게스트 고유 넘버를 증가

            anounce(guest_box[-1].my_number)

            if len(table_box) == 5:
                # 테이블이 꽉차면 기다려야지
                for z in range(50):
                    if z not in waiting_guest_box:
                        waiting_guest_box[z] = (guest_box[-1])
                        guest_box.pop(-1)
                        print(f"{waiting_guest_box[z].my_number}번 손님은 대기하기로 해요")
                        break
            elif len(table_box) < 6:  # 테이블 자리가 있을때

                for x in range(5):
                    if x not in table_box:
                        table_box[x] = guest_box[-1]  # 일단 더해주고
                        guest_box.pop(-1)  # 다음은 원래 자리에서 제거해준다

                        table_box[x].table_number = x # 테이블 넘버를 저장해줌
                        table_box[x].menu = random.randrange(1, 5)

                        if len(cooker_box) < 3:
                            for y in range(3):
                                if y not in cooker_box:
                                    cooker_box[y] = (Cooker())
                                    if table_box[x].menu == 1:
                                        table_box[x].eating_time = 11
                                        cooker_box[y].cooking_time = 11  # 요리시간 추가
                                        cooker_box[y].what_is_number = table_box[x].my_number
                                        cooker_box[y].table_number = x
                                    if table_box[x].menu == 2:
                                        table_box[x].eating_time = 16
                                        cooker_box[y].cooking_time = 16
                                        cooker_box[y].what_is_number = table_box[
                                            x].my_number
                                        cooker_box[y].table_number = x
                                    if table_box[x].menu == 3:
                                        table_box[x].eating_time = 21
                                        cooker_box[y].cooking_time = 21
                                        cooker_box[y].what_is_number = table_box[
                                            x].my_number
                                        cooker_box[y].table_number = x
                                    if table_box[x].menu == 4:
                                        table_box[x].eating_time = 26
                                        cooker_box[y].cooking_time = 26
                                        cooker_box[y].what_is_number = table_box[
                                            x].my_number
                                        cooker_box[y].table_number = x

                                    break
                            print(
                                f"{table_box[x].my_number}번 손님이 {x}번 테이블에 앉아 {table_box[x].menu}번 메뉴를 주문했어요")
                            break
                        if len(cooker_box) == 3:

                            print(f"{x}번 테이블에 앉은 {table_box[x].my_number}번 손님은 기다려야해! 요리사가 모두 요리중")
                            for i in range(0, 50): # 최대 대기 가능 인원 50명
                                if i not in table_cooking_waiting_box:
                                    table_cooking_waiting_box[i] = table_box[x]
                                    break
                        break
                    else:
                        pass



        for i in range(3):
            if i in cooker_box:
                cooker_box[i].cooking_time -= 1
                if cooker_box[i].cooking_time == -1:
                    #요리완료
                    table_box[cooker_box[i].table_number].eating_or_not_eating = True
                    print(table_box[cooker_box[i].table_number].my_number,"번 손님 요리 완료되었어요")

        for z in range(3):
            if z in cooker_box:
                if table_box[cooker_box[z].table_number].eating_or_not_eating is True:
                    cooker_box.pop(z)


        for j in range(5):

            if j in table_box:
                if table_box[j].eating_or_not_eating is True:
                    table_box[j].eating_time -= 1

                if table_box[j].eating_time == 0:
                    print(f"{table_box[j].my_number}번째 손님이 {j}번 테이블에서 {table_box[j].menu}번째 요리를 다 먹었네요?")
                    table_box.pop(j)

        tick += 1


main()
