# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
from functools import reduce

def solution(A):
    return reduce(lambda acc, cur : acc ^ cur, A, 0)



