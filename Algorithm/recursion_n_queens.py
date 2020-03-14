
n = 8
cols = [0 for _ in range(n)]
def queens(level):
    print(cols)
    if not promising(level):
        return False
    elif level==n:
        return True
    else:
        for i in range(1, n+1):
            cols[level+1] = i
            if queens(level+1):
                return True
        return False

def promising(level):
    for x in range(1, level):
        if cols[x] == cols[level]: #x는 말의 번호이다. level번째 말과 열이 겹치는지 확인한다.
            return False
        elif level-x == abs(cols[level]-cols[x]): # level-x는 곧 행의 차이다.
            return False
    return True

queens(n)
print(cols)
