from collections import deque
def solution(begin, target, words):

    def check(s1, s2):
        res = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                res += 1
        if res >= len(s1) - 1:
            return True
        return False
    
    
    queue = deque()
    queue.append([begin, words, 0])
    
    while queue:
        
        value, path, c = queue.popleft()
        
        if value == target:
            return c
        
        for i, j in enumerate(path):
            
            if check(value, j):

                new_path = path[:]
                new_value = new_path.pop(i)
                queue.append([new_value, new_path, c + 1])
    return ans