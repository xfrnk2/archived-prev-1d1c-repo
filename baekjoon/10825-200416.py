#문제 : 10825번 국영수
#주소 : https://www.acmicpc.net/problem/10825
#실마리 얻은곳 : https://dailyheumsi.tistory.com/67
# https://wayhome25.github.io/python/2017/03/07/key-function/

if __name__ == '__main__':
    student_count = int(input())
    students_list = []

    for _ in range(student_count):
        student = input().split()
        student = student[:1] + list(map(int, student[1:]))
        students_list.append(student)

    students_list = sorted(students_list, key = lambda student : (-student[1], student[2], -student[3], student[0]))

    for x in students_list:
        print(x[0])

