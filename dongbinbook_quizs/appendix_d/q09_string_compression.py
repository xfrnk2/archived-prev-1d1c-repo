# https://programmers.co.kr/learn/courses/30/lessons/60057
# 통과는 했는데, 아직 지저분하고, 50분 걸려 풀었다.교재에는 풀이시간 30분으로 되어있다.

def solution(s):
    nums = [x for x in range(1, len(s) // 2 + 2)]
    results = []
    for i in nums:
        string = ''
        temp = s[:i]
        counts = 0
        for j in range(0, len(s), i):
            if temp == s[j:j + i]:
                counts += 1
            else:
                if counts > 1:
                    string += str(counts) + temp
                else:
                    string += temp

                temp = s[j:j + i]
                counts = 1
        if counts > 1:
            string += str(counts) + temp
        else:
            string += temp

        results.append(len(string))

    return min(results)