import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hackerrank.Problem_Solving.Service_Lane import serviceLane


class TestClass(object):
    def test_func(self):
        assert serviceLane(0, [(0,3), (1, 4)]) == 0, "width 그룹의 길이가 2 이상이다. 아닌 경우 에러 발생"
        assert serviceLane(5, [(0, 6), (1, 4)]) == 0, "cases의 case 범위의 상한이 width를 초과하지 않는다. 초과하는 경우 에러 발생"
        