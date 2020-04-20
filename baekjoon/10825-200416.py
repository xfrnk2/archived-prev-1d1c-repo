#문제 : 10825번 국영수
#주소 : https://www.acmicpc.net/problem/10825
#실마리 얻은곳 : https://dailyheumsi.tistory.com/67
# https://wayhome25.github.io/python/2017/03/07/key-function/
from operator import itemgetter
if __name__ == '__main__':

    student_list = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(int(input()))]
    student_list.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))
    # key=itemgetter(-1, 2, -3, 0)도 가능하다.
    for x in student_list: print(x[0])

