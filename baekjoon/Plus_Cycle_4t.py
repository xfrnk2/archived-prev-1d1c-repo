#https://www.acmicpc.net/problem/1110

def function(num):
    if num <= 0:
        return 0

    num_count = 0
    original_num = num

    while num_count < 999:
        num_count += 1
        num = num % 10 * 10 + eval('+'.join(str(num))) % 10
        if original_num == num:
            break

    if 999 <= num_count:
       return print("사이클이 999회에 도달하였으므로 정확한 연산을 할 수 없습니다. ")
    return num_count

if __name__ == "__main__":
    num = int(input())
    if num < 10:
        num *= 10
    print(function(num))
