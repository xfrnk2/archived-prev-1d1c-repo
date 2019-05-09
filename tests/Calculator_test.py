from Calculator import parse, eval
import pytest
class TestClass(object):
    def test_parse(self):
        assert parse("1 + 3") == ("+", 1, 3), "공백을 잘 처리한다"
        assert parse("1 * 3") == ("*", 1, 3)
        assert parse("1/ 3") == ("/", 1, 3)
        assert parse("1-3") == ("-", 1, 3), "공백이 없을 경우에도 파싱 성공한다."

    def test_eval(self):
        assert eval(("+", 1, 2)) == 3,"에러"
        assert eval(("-", 1, 2)) == -1,"에러"
        assert eval(("*", 1, 2)) == 2,"에러"
        assert eval(("/", 1, 2)) == 0.5,"에러"
        with pytest.raises(ZeroDivisionError):
            eval(("/", 1, 0))