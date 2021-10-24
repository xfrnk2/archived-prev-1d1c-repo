# 1번 문제
# 성공 실패 결정 요인: 좌표1=(x1, y1) < 좌표2=(x2, y2)가 보장되어야 하고, * 집합은 ((0, 0), (1, 1))과 ((1, 1), (0, 0))을 다른 요소로 취급한다.

def solution(dirs):

    curX = 0
    curY = 0

    visits = set()
    
    for d in dirs:
        
        if d == 'U' and curY < 5:
            visits.add(((curY, curX),(curY + 1, curX)))
            curY += 1
        elif d == 'D' and curY > -5:
            visits.add(((curY - 1, curX),(curY, curX)))
            curY -= 1
        elif d == 'R' and curX < 5:
            visits.add(((curY, curX),(curY, curX + 1)))
            curX += 1
        elif d == 'L' and curX > -5:
            visits.add(((curY, curX - 1),(curY, curX)))
            curX -= 1
    return len(visits)
    
    
# 2번 문제

def solution(n):
    prev = 1
    cur = 1
    
    for _ in range(n - 2):
        temp = prev + cur 
        prev, cur = cur, temp
    
    return cur % 1234567