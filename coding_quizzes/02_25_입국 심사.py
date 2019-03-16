# 입국 심사 링크 : https://programmers.co.kr/learn/courses/30/lessons/43238
# Description
# n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
#
# 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
#
# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
#
# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
# 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
# 심사관은 1명 이상 100,000명 이하입니다.
# 입출력 예
# n	times	return
# 6	[7, 10]	28
# 입출력 예 설명
# 가장 첫 두 사람은 바로 심사를 받으러 갑니다.
#
# 7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.
#
# 10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.
#
# 14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.
#
# 20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.

# 100분
import random
n = random.randrange(1, 10)
times = [x for x in range(1, random.randrange(2, 6))]

# 1. 사람이 할 일 : 숫자만 있음 됨
# 2. 심사대가 할 일 : 비어있는지 여부 보존(true와 false로), 남은 시간을 가지고 있기. 걸리는 시간 보존

class examination:
    def __init__(self):
        #비어있으면 False, 차있으면 True
        self.__data = False
        self.__left_time = 0

    def get_information(self):
        return self.__data

    def check_time(self):
        self.__left_time -= 1
        if self.__left_time == 0:
            self.__data = False

    def set_time(self, time):
        self.__left_time = time


def solution(n, times):

    sims = []
    time_tick = 0

    for i in range(len(times)):
        sim = examination()
        sim.set_time(times[i])
        sims.append(sim)





    flag = True
    while flag:
        n_count = 1
        for x in sims:
            x.check_time()
            if not x.get_information():
                print(f"{time_tick}분이 지났을 때, {sims.index(x)}번째 심사대가 비고, {n_count}번째 사람이 심사를 받습니다")
                n_count += 1

        if n_count >= 120:
            flag = False

        time_tick += 1

solution(n, times)
#
# 우아한테크코스 1기 온라인 코딩테스트 for 김범석
# 문의하기(채팅)
# 도움말
# Python3 레퍼런스
# 컴파일 옵션
# 테스트 종료
# 프로그래밍1
# 프로그래밍2
# 프로그래밍3
# 프로그래밍4
# 프로그래밍5
# 프로그래밍6
# 프로그래밍7
# 문제 설명
# 성공한 덕후로서 연예 기획사에 입사를 하게 된 배달이는 첫 프로젝트로 콘서트 티켓팅을 진행하게 되었습니다. 기존에는 팬으로서 참여했던 티켓팅을 운영자로서 참여하게 되어서 감회가 새로운 배달이었지만 한편으로 팬들의 마음을 누구보다도 잘 알았기 때문에 그들의 힘듦을 최소화해주고 싶다는 책임감에 잠 못 이루었습니다. 결국 티켓팅 시뮬레이션을 통해 적절한 솔루션을 찾기 위해 테스트 시뮬레이션을 만들기로 하였습니다.
#
# 총 티켓 수 totalTicket과 접속/취소 로그 배열 logs가 주어질 때, 아래의 시뮬레이션 설명을 참고하여 티켓팅에 성공한 유저의 아이디 목록을 추출하여 return 하도록 solution 메서드를 완성해주세요.
#
# 시뮬레이션 설명
# 접속 시도를 하면 request 로그가 남고 접속 후 1분 이내 접속을 종료하면 leave 로그가 남는다. (09:00:00에 request 후 09:00:59에 leave 시 구매 실패, 09:00:00에 request 후 09:01:00에 leave 시 구매 성공)
# 이미 한 유저가 접속한 상태라면 다른 유저들은 접속을 할 수 없으며 다시 접속을 시도해야 한다.
# 티켓을 구매하기 위해서는 서버 접속 후 1분을 유지해야 한다.
# 티켓 구매를 성공한 유저는 접속은 가능하지만 다시 구매는 할 수 없다.
# KakaoTalk_Image_2019-03-15-09-37-55.png
#
# case 1
# 09:12:29에 request 한 woni는 1분 동안 접속을 유지하여 티켓 구매에 성공함.
# case 2
# 09:23:11에 request 한 brown은 1분 동안 접속을 유지하지 못하고 09:23:44초에 접속을 종료하여 leave 로그가 남으며 티켓 구매에 실패함.
# case 3
# jason과 jun과 cu가 접속을 시도하였지만 가장 빨리 접속 시도를 한 jason이 접속을 하였고 그 이후로 접속 시도한 jun과 cu는 접속을 실패함.
# 구매 성공
# 구매 중인 유저가 없을 때 request 하여 1분 동안 접속 유지(leave 로그가 없음)
# 구매 실패
# 접속 후 1분을 유지하지 못한 경우(leave 로그 있음)
# 다른 유저가 접속한 상태에서 request 한 경우
# 제한사항
# 티켓팅 시간은 9시부터 10시이다. (10시 0분 0초에 서버가 종료된다)
# 같은 시간(시분초)의 로그는 발생하지 않습니다.
# 로그는 request 유형과 leave 유형만 존재합니다.
# 총 티켓 수는 0부터 10,000까지 정수입니다.
# id는 소문자 알파벳만 가능합니다.
# id는 오름차순으로 정렬해 return 해주세요.
# 입력
# 총 티켓 수
# 접속 시도/취소 로그 배열 (id, action[request/leave], 시분초 hh:mm:ss)
# input sample
# totalTicket = 2000
# logs = [
#     "woni request 09:12:29",
#     "brown request 09:23:11",
#     "brown leave 09:23:44",
#     "jason request 09:33:51",
#     "jun request 09:33:56",
#     "cu request 09:34:02"
# ]
# 출력
# 티켓팅 성공한 id 배열
#
# output sample
# [
#     "jason",
#     "woni"
# ]
# solution.py
# 1
# def solution(totalTicket, logs):
# 2
#     answer = []
# 3
#     return answer
# 실행 결과
# 실행 결과가 여기에 표시됩니다.
# 종료까지
# 00:00:03
