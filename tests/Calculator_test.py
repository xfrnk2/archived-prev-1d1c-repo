from Calculator import parse
class TestClass(object):
    def test_parse(self):
        assert parse("1 + 3") == (1, "+", 3), "공백을 잘 처리한다"