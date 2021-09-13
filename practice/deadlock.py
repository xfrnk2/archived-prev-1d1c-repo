from random import randrange
import threading
import time
class Player:
    def __init__(self, num):
        self.number = num
        self.lock = threading.Lock()
        self.hp = 100

    def drain(self, target):
        self.lock.acquire()
        try:
            self.hp += 5
        finally:
            self.lock.release()

        target.lock.acquire()
        try:
            target.hp -= 5
        finally:
            target.lock.release()

players = [Player(i) for i in range(1000)]
final_hosts = []
final_targets = []

def execute(number) :
    """
    쓰레드가 실행할 함수
    """
    host = players[randrange(1000)]
    target = players[randrange(1000)]
    host.drain(target)

    final_hosts.append(host.number)
    final_targets.append(target.number)
    return print(threading.currentThread().getName() , number,  host.number, target.number)

if __name__ == "__main__" :
    for i in range(1, 51 ) :
        my_thread = threading.Thread( target=  execute , args = (i, ))
        my_thread.start()


    hh = []
    tt = []
    for h, t in zip(final_hosts, final_targets):
        x, y = players[h], players[t]

        hh.append((x.number, x.hp))
        tt.append((y.number, y.hp))
    print(hh)
    print(tt)

#
# num_threads = threading.activeCount()
# print(num_threads)