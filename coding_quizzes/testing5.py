
def solution(number):
    if not isinstance(number, int) or not 1 <= number <= 10000:
        print("잘못된 숫자를 입력하였습니다")

    count = 0
    for num in range(1, number + 1):
        for x in str(num):
            if x in ['3', '6', '9']:
                count += 1

    return count
solution(13)
