import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hackerrank.Interview_Preparation_Kit.String_Manipulation.Alternating_Characters import alternatingCharacters


class TestClass(object):
    def test_func(self):
        assert alternatingCharacters("AABBAABB") == 4, "문제없이 동작한다"
        assert alternatingCharacters("ABABABAA") == 1, "문제없이 동작한다"
        assert alternatingCharacters("") == 0, "매개변수가 아무것도 없어도 잘 동작한다"
        assert alternatingCharacters([1]) == 0, "인자값이 string이 아닌 다른 값이라면 0을 리턴"
        assert alternatingCharacters(35) == 0, "인자값이 string이 아닌 다른 값이라면 0을 리턴"
