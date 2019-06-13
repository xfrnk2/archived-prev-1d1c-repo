#https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
    arr = sorted(arr)
    length = len(arr)
    answer = [length]
    front_num = 0

    while 1 < length:
        n = arr.pop(0)

        if n == front_num:
            continue

        count = 1
        for x in arr:
            if n == x:
                count += 1

        length -= count
        answer.append(length)
        front_num = n

    return answer


print(cutTheSticks([8, 8, 14, 10, 3, 5, 14, 12]))
