from dataclasses import dataclass, asdict, astuple
@dataclass
class C:
    a: int = 1      # 'a' has no default value
    b: int = 0   # assign a default value for 'b'


c = C()
print(c)
assert asdict(c) == {'a': 1, 'b': 0}
print(asdict(c))
assert astuple(c) == (1, 0)
print(astuple(c))


@dataclass
class D:
    x: int
    y: 'typing.Any'
    z: int = 5

    def add_one(self):
        return self.z + 1
d = D(1, 2)
print(d.add_one())

