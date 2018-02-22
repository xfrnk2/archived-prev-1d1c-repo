"""
Task Class 를 만듭니다.

이 클래스는 run( value : int ) 을 호출하면 자신의 식별 번호와 인자로 전달 받은 value 를 출력합니다.
# TODO - 아래와 같이 출력합니다. ( x = 자신의 식별 번호, y = value )
x  : y

이 클래스는 출력 한 시점부터 1초 동안 쉬고, 1초 뒤 다시 일 할 수 있습니다.



TaskManager Class 를 만듭니다.

이 매니저 클래스 내부에는

 1. 대기 중인 Task 만 모아둔 큐 자료구조
 2  일하거나 일 한 후 1초간 쉬는 Task 만 모아둔 큐 자료구조

이렇게 두 개가 존재합니다.
초기에 1번 큐에 Task 를 10개 채워 놓습니다.


외부에서 do_job( value : int ) 함수를 호출하면
 1번 큐에서 Task 를 하나 꺼내 2번 큐로 옮기고 해당 Task 의 run(value) 를 호출해야 합니다.




"""

from raven import Client
from collections import deque


class Task:
    # TODO - 적절히 채워주세요.

    def __init__(self, idx: int):
        self.__idx = idx
        self.__waiting_tick = 0

    def run(self, value: int):
        # TODO - 아래와 같이 출력한 이후 적절히 1초가 지난 시점에 TaskManager 의 대기 큐로 돌아가야 합니다.
        idx = self.__idx
        print(f'{idx} : {value}')

    @property
    def waiting(self) -> bool:

        if self.__waiting_tick > 1:
            return True
        if self.__waiting_tick == 0:
            return True
        else:
            return False

    def tick(self):
        self.__waiting_tick += 1


class TaskManager:

    # TODO - 적절히 채워주세요.

    def __init__(self):
        # TODO - 아래의 리스트를 큐로 바꿔주세요.
        # TODO - 다음 링크를 보고 공부해주세요 https://docs.python.org/2/library/collections.html

        self.__stand_by_queue = deque([])
        self.__working_queue = deque([])

    def do_job(self, value: int):
        # TODO - 요구 명세에 맞춰 구현해 주세요.
        to_be_relocated = self.__stand_by_queue[0]
        self.__working_queue.append(to_be_relocated)
        self.__stand_by_queue.popleft()

        self.__working_queue[-1].run(value)

    def change_tick(self):
        for task in self.__stand_by_queue, self.__working_queue:
            task.tick()

    def append_task(self):
        for x in range(10):
            self.__stand_by_queue.append(Task(x))

    def check(self):
        to_be_returned = []

        # 다시 일 할 수 있는 Task 만 모아서
        for task in self.__working_queue:
            if task.waiting:
                to_be_returned.append(task)

        # 일단 2번 큐(일 하는 중인 큐)에서 제거하고
        for task in to_be_returned:
            self.__working_queue.remove(task)

        # 1번 큐(대기 큐)로 반납
        self.__stand_by_queue.extend(to_be_returned)

    @property
    def enable(self) -> bool:
        return len(self.__stand_by_queue) > 0


client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException

    try:
        tm = TaskManager()
        tm.append_task()
        for x in range(100):

            if tm.enable:
                tm.do_job(x)
            else:
                tm.check()

    except Exception:
        client.captureException()



"""
잠시 보관
    def add_tasks(self):
            self.__stand_by_queue.append(Task(x))
            
            
if x < 10:
    tm.add_tasks()
    continue
    
     for task in self.__stand_by_queue:

            self.__working_queue.append(task)
            self.__stand_by_queue.remove(task)
            task.run(value)
    
    
    
   """
