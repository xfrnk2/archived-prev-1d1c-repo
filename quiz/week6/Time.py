# coding=utf-8

from week6.chef import Chef
from week6.counter import Counter
from week6.guest import Guest
from week6.guestvisit import GuestVisit

class Time:

    def __init__(self):
        # FIXME - 대체 이 Time 이라는 클래스는 요리사, 카운터, 손님 등과 어떻게 연관 관계를 맺고 있는 걸까요.
        self.__chef = Chef()
        self.__counter = Counter()
        self.__guest = Guest()
        self.__guest_visit = GuestVisit
        self.elapsed_time = 0

    # FIXME - 방향은 나쁘지 않았습니다.
    # 매 틱마다 순차적으로 손님 / 주방장 / 카운터 등에 대한 처리를 한다는 접근은 괜찮았는데,
    # 문제는 그런 루프를 왜 Time 에서 돌리고 있을까요?
    # 과연 적절한 클래스 분배 및 클래스명 설정일까요?
    def tick(self):
        for x in range(720):
            self.elapsed_time += 1
            elapsed_time = self.elapsed_time
            print(f"현재시간 {elapsed_time}/720분)")

            self.__guest.guest_simulate()
            self.__guest_visit.add_new_guest()

            self.__chef.minus_time()
            self.__counter.minus_time()

            self.__chef.chef_simulate()
            self.__chef.reset_chef_time()
            self.__counter.simulate()

            # get 걸리는 시간을 얻어온다. 매 틱 마다 한번씩 모든 장소를 반복 실행함.
