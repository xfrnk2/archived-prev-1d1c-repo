import itertools

iterable0 = 'A'
iterable1 = 'B'
iterable2 = 'xy'
iterable3 = '12'
iterable4 = 'ABCD'

print(list(itertools.product(iterable0, iterable1, iterable2, repeat=2)))
#result = [('A', 'B', 'x'), ('A', 'B', 'y')]

print(list(itertools.product(iterable0, iterable1, iterable2, repeat=2)))
#result = [('A', 'B', 'x', 'A', 'B', 'x'), ('A', 'B', 'x', 'A', 'B', 'y'), ('A', 'B', 'y', 'A', 'B', 'x'), ('A', 'B', 'y', 'A', 'B', 'y')]

print(list(itertools.product(iterable1, iterable2, repeat=2)))
#result = [('B', 'x', 'B', 'x'), ('B', 'x', 'B', 'y'), ('B', 'y', 'B', 'x'), ('B', 'y', 'B', 'y')]

print(list(itertools.product(iterable4, repeat=2)))
#result = [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D')]

#repeat의 의미는 무엇일까? 자릿수?