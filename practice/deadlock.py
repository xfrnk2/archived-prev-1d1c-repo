import threading
class Player:
    def __init__(self):
        self.lock = threading.Lock()
        self.hp = 100

    def drain(self, target):
        self.lock.acquire()
        target.lock.acquire()
        self.hp += 5
        target.hp -= 5
        target.lock.release()
        self.lock.release()

A = Player()
B = Player()
C, D, E, F, G, H = Player(), Player(), Player(), Player(), Player(), Player()
A.drain(B)
B.drain(A)
H.drain(A)
E.drain(B)

print(A.lock)
print(A.hp)
print(B.lock)
print(B.hp)

