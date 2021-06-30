from collections import deque

a = deque((1, 2, 3, 4, 5))
a.appendleft(0)
a.append(6)
print(a)
print(list(a))
print(set(a))

