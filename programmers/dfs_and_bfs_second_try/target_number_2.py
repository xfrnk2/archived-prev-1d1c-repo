def solution(numbers, target):
    answer = 0

    def dfs(v, cnt):
        nonlocal answer
        if cnt == len(numbers) - 1:
            if v == target:
                answer += 1
            return

        if cnt == 0:
            dfs(-v + numbers[cnt + 1], cnt + 1)
            dfs(-v - numbers[cnt + 1], cnt + 1)
        dfs(v + numbers[cnt + 1], cnt + 1)
        dfs(v - numbers[cnt + 1], cnt + 1)

    dfs(numbers[0], 0)
    return answer

