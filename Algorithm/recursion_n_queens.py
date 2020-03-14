n = 8
cols = [x for x in range(n+1)]

def queens(level) -> bool:
    if not promising(level):
        return False
    elif level == n:
        return True
    else:
        for i in range(1, n+1):
            cols[level+1] = i
            if queens(level+1):
                return True
        return False



def promising(level)-> bool:
    for i in range(1, level+1):
        if cols[i]==cols[level]:
            return False
        elif level-1 == abs(cols[level-cols[i]]):
            return False
    return True

queens(0)
print(cols)