def solution(numbers, hand):
    answer = ''
    pad = [0] * 13
    lhs, rhs = 10, 12

    if hand == "right":
        hand = 'R'
    else:
        hand = 'L'

    for x in numbers:
        if x == 0:
            x = 11

        if x % 3 == 0:
            rhs = x
            answer += 'R'
        elif (x - 1) % 3 == 0:
            lhs = x
            answer += 'L'
        else:

            a = abs(x - lhs)
            b = abs(x - rhs)

            if a % 3 == 0:
                a //= 3
            if b % 3 == 0:
                b //= 3

            if 2 <= a <= 4:
                a = 2
            if 2<= b <= 4:
                b = 2

            if 5 <= a <= 7:
                a = 3
            if 5 <= b <= 7:
                b = 3

            if 8 <= a <= 10:
                a = 3
            if 8 <= b <= 10:
                b = 3

            result = ''
            if a < b:
                lhs = x
                answer += 'L'
            elif a > b:
                rhs = x
                answer += 'R'
            else:
                if hand == 'R':
                    rhs = x
                    answer += 'R'
                else:
                    lhs = x
                    answer += 'L'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"))
print(solution([5],	"right"))
# 정답 LRLLLRLLRRL
