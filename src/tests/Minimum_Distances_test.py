import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hackerrank.Problem_Solving.Minimum_Distances import minimumDistances

#https://www.hackerrank.com/challenges/minimum-distances/problem

class TestClass(object):
    def test_func(self):
        assert minimumDistances([7, 1, 3, 4, 1, 7]) == 3, "연산을 잘 수행한다"
        assert minimumDistances([1, 2, 3, 4, 10]) == -1, "쌍을 이루는 원소가 없으니 -1을 반환한다"
        assert minimumDistances([1, 2, 1, 4, 10, 1, 10]) == 2, "쌍을 이루는 원소가 3개 이상이지만 연산을 잘 수행한다"
