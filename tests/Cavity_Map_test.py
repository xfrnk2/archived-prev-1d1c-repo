#https://www.hackerrank.com/challenges/cavity-map/problem

from src.hackerrank.Problem_Solving.Cavity_Map import cavityMap
class TestClass(object):
    def test_func(self):
        assert cavityMap(['9']) == ['9'], "인자로 받아온 리스트의 길이가 2 이하의 조건에서 연산을 잘 수행한다"
        assert cavityMap(['144932', '502912']) == ['144932', '502912'], "인자로 받아온 리스트의 길이가 2 이하의 조건에서 연산을 잘 수행한다"
        assert cavityMap(['12','12', '12']) == ['12','12', '12'], "인자로 받아온 리스트의 원소의 길이가 2 이하일 때 연산을 잘 수행한다"
        assert cavityMap(['1112', '1912','1892', '1234'])\
               == ['1112', '1X12','18X2', '1234'], "연산을 잘 수행한다"
        assert cavityMap(['1111', '1111', '1111']) == ['1111', '1111', '1111'], "리스트내의 원소의 값이 모두 동일할때 연산을 잘 처리한다"