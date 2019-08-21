#https://www.hackerrank.com/challenges/cavity-map/problem

from src.hackerrank.Problem_Solving.Cavity_Map import cavityMap
class TestClass(object):
    def test_func(self):
        assert cavityMap([[1, 2],[1, 2]]) == [[1, 2],[1, 2]], "연산을 잘 수행한다."
        assert cavityMap([[1, 1, 1,  2], [1, 9, 1, 2], [1, 8, 9, 2], [1, 2, 3, 4]])\
               == [[1, 1, 1, 2], [1, "X", 1, 2], [1, 8, "X", 2], [1, 2, 3, 4]], "테스트가 잘 동작한다"
