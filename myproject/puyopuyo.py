import time
import os

def func():
    arr = ['□' * 6 for _ in range(12)]
    c = 0
    while True:
        os.system('cls')

        for i in arr:
            print(i)

        time.sleep(0.3)
        c += 1
        print(c)




if __name__ == '__main__':
    func()
