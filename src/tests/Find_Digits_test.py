import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hackerrank.Problem_Solving.Find_Digits import findDigits

class TestClass(object):
    def test_func(self):
        assert findDigits(12) == 2, "연산을 잘 수행한다"
        assert findDigits(1012) == 3, "연산을 잘 수행한다"

