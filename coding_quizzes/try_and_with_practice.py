# 참고 링크 https://cjh5414.github.io/python-with/
# https://cjh5414.github.io/python-with/
# https://soooprmx.com/archives/4079

def testing():
    f = open("try_and_with_practice_.txt", 'w')

    try:
        f.write("만나서 반갑습니다")
        for x in range(9):
            f.write(f"{x}를 입력합니다 \n")
        f.close()
        f = open("try_and_with_practice_.txt", 'r')
        print(f.read())

    finally:
        f.close()


testing()

# class testing2():
#
#     def __enter__(self):
#         open("try_and_with_practice_.txt", 'r')
#
#     def __exit__(self):
#         pass

with open("try_and_with_practice_.txt", 'r') as f:
    for x in f:
        print(x, end='')


class testing2:
    def __init__(self):
        self.w = open("try_and_with_practice_2.txt", 'w')
        self.r = open("try_and_with_practice_2.txt", 'r')

        self.w.write("with문 연습\n")
        for y in range(5):
            self.w.write(f"{y}를 입력합니다\n")

    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.w.close()
        self.r.close()


with testing2().r as thing:
    for x in thing:
         print(x,end='')
