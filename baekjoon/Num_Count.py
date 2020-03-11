#https://www.acmicpc.net/problem/2577
#읽을거리
# https://stackoverflow.com/questions/14132545/itertools-accumulate-versus-functools-reduce
"""
You can see in the documentation what the difference is. reduce returns a single result,
 the sum, product, etc., of the sequence. accumulate returns an iterator over all the intermediate results.
  Basically, accumulate returns an iterator over the results of each step of the reduce operation.

아래는 표현예시
sum(accumulate(arr, add))
reduce(arr)
"""
#eval('*'.join([input() for _ in range(3)]))
#reduce(lambda x, y : x*y, arr)

from collections import Counter

arr = eval(f'{input()}*{input()}*{input()}')
value = Counter(str(arr))
for x in range(10):
    print(value[str(x)])

