from collections import deque
import time


class Task():
    def __init__(self, idx):
        self.__idx = idx


class TaskManager():
    def __init__(self):
        self.__queue = deque([])

    def __str__(self):
        return self.__queue

    def simulate(self):
        for x in range(10):
            self.__queue.append(Task(x))

    def to_do(self):
        return self.__queue

tm = TaskManager()

tm.simulate()
print(tm.to_do())

print(time.clock())


for x in range(100):
    current_time = time.time()
    print(current_time)