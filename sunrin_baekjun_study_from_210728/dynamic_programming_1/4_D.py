# https://www.acmicpc.net/problem/2747
# 첫 번째 풀이
# n = int(input())
# num = [0] * (n+1)
# num[1] = 1
# for i in range(2, n+1):
#     num[i] = num[i-2] + num[i-1]
# print(num[n])

# 두 번째 풀이(최적화 시키기)
# prev, current = 0, 1
# for _ in range(int(input())):
#     prev, current = current, current + prev
# print(prev)

#3번째 풀이, 생각난 모듈을 사용해서 풀어보기 (functools reduce)
'''
이런 2중 람다문도 있다.
아래의 reduce에 0, 1, 2순에서 1, 2번째 인자는 각각 범위와 생성자이다.
https://docs.python.org/3/library/functools.html

-> functools.reduce(function, iterable[, initializer])

If the optional initializer is present, it is placed before the items of
 the iterable in the calculation, and serves as a default when the iterable
  is empty. If initializer is not given and iterable contains only one item,
   the first item is returned.


'''
# from functools import reduce
# n = int(input())
# f =lambda w: reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0, 1])[0]
# print(f(10))


# 4번째 풀이. 재귀와 람다식
# n = int(input())
# fib = lambda x : x if x < 2 else fib(x-1) + fib(x-2)
# print(fib(n))
'''
By the way, it's rarely seen because it's confusing, 
and in this case it is also inefficient. It's much better to write 
it on multiple lines:
'''
#5번째 코드
fib = lambda n:pow(2<<n,n+1,(4<<2*n)-(2<<n)-1)%(2<<n)
print(fib(int(input())))
# 출처 : https://stackoverflow.com/questions/4935957/fibonacci-numbers-with-an-one-liner-in-python-3
# 출처 : https://blog.paulhankin.net/fibonacci/

'''
결론적으로 메모리와 시간의 효율은 for문을 사용한 것(1번)이 가장 좋았다. 
사실 5번째 코드와는 효율 차이가 없었다.(동일)
'''