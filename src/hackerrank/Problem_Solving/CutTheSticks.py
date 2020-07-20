#https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
    a2 = sorted(arr)
    size = len(a2)
    ans = [size]
    target = -1
    numCount = 1

    for x in a2:
        if target == -1:
            target = x
            continue

        if target == x:
            numCount += 1

        else:
            size -= numCount
            if size == 1:
                ans.append(1)
                break
            target = x
            numCount = 1
            ans.append(size)

    return ans
