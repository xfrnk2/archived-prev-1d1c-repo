#문제 : 1026번 보물
#주소 : https://www.acmicpc.net/problem/1026

if __name__ == '__main__':
    get_input = lambda:sorted(map(int, input().split()))
    get_input()
    print(sum(list(map(lambda x, y : x * y, get_input(), get_input()[::-1]))))


