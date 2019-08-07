import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hackerrank.Problem_Solving.The_Time_In_Words import timeInWords


class TestClass(object):
    def test_func(self):
        assert timeInWords(5, 47) == "thirteen minutes to six", "연산을 잘 수행한다"
        assert timeInWords(3, 00) == "three o' clock", "연산을 잘 수행한다"
