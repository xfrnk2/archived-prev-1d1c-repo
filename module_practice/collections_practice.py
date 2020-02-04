import collections

Person = collections.namedtuple('Person', 'name age gender')

print ('Type of Person:', type(Person))

bob = Person(name='Bob', age=30, gender='male')
print ('\nRepresentation:', bob)


jane = Person(name='Jane', age=29, gender='female')
print ('\nField by name:', jane.name)

print ('\nFields by index:')
for p in [ bob, jane ]:
    print ('%s is a %d year old %s' % p)


    try:
        collections.namedtuple('Person', 'name class age gender')
    except ValueError as err:
        print(err)

    try:
        collections.namedtuple('Person', 'name age gender age')
    except ValueError as err:
        print(err, '\n')


#rename 옵션을 True로 줄 시 중복 필드명의 이름을 바꿔버림
with_class = collections.namedtuple('Person', 'name class age gender', rename=True)
print(with_class._fields)

two_ages = collections.namedtuple('Person', 'name age gender age', rename=True)
print(two_ages._fields, '\n\n\n')






#.name과 위치[offset]으로 접근 가능한 튜플의 서브클래스 네임드튜플
Duck = collections.namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck, '\n')

#딕셔너리로 키워드 인자**kwargs를 사용하여 네임드 튜플을 만들 수 있다.
duck = {'bill' : 'wide orange', 'tail' : 'long' }
dict_duck = Duck(**duck)
print(dict_duck, '\n')

#네임드튜플은 불변속성이나 필드를 바꿔서 다른 네임드 튜플을 반환할 수 있다.
duck = Duck('wide orange', 'long')
duck2 = duck._replace(tail='magnificent', bill='crushing')
print(duck, duck2)
