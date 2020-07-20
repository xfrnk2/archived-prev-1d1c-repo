#https://programmers.co.kr/learn/courses/30/lessons/42588?language=python3
#코딩테스트 연습/ 스택 큐 / 탑 / lv2
heights = [6,9,5,7,4]
def solution(heights):
    answer = [0]*len(heights)
    for i in reversed(range(1, len(heights))):
        target = i - 1
        while heights[target] <= heights[i] and 0 <= target:
            target -= 1
        answer[i] = target + 1

    return answer
#스택을 쓰면 그만한 메모리 할당이 생기므로 for문 내부의 지역변수로 대체


#아래는 스택으로 푼 풀이
def solution_stack(heights):
    answer = [0]*len(heights)
    stack = []
    for i in reversed(range(len(heights))):
        while stack and heights[stack[-1]] < heights[i]:
            answer[stack.pop()] = i+1
        stack.append(i)
    return answer

print(solution_stack(heights))