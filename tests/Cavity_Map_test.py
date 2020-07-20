from src.Cavity_Map import cavityMap


class TestClass(object):

    def test_func(self):
        assert cavityMap(0) == 0, "연산을 잘 수행한다"
