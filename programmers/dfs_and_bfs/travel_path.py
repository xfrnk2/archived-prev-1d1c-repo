from collections import defaultdict

# 참고한 다른사람 코드 <- https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/
# 손코딩 & stack을 사용한 dfs, 좀 난해해서 다음에 같은 맥락의 문제를 마주친다면 재귀로 풀 가능성이 높겠단 생각이 든다. 그래도 알아두면 유용하겠다.

def solution(tickets):
    def init_graph():

        graph = defaultdict(list)

        for key, destination in tickets:
            graph[key].append(destination)

        return graph

    def dfs():
        stack = ['ICN']
        path = []
        while len(stack) > 0:
            top = stack[-1]
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    answer = dfs()

    return answer

# 재귀를 사용한 풀이  - 조금의 비교(참고 코드)를 거쳐 가며 손코딩

from collections import defaultdict

def solution(tickets):
    def init_graph():

        graph = defaultdict(list)

        for key, destination in tickets:
            graph[key].append(destination)

        return graph

    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            return path

        for idx, dst in enumerate(routes[airport]):
            routes[airport].pop(idx)

            fp = path[:] # 배정구문을 사용한 리스트형 깊은 복사
            fp.append(dst)
            ret = dfs(dst, fp)
            if ret:
                return ret

            routes[airport].insert(idx, dst)




    routes = init_graph()
    for r in routes:
        routes[r].sort()
    answer = dfs('ICN', ['ICN'])
    return answer