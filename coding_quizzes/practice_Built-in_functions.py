all_p = all([1, 2, 3, 0])
any_p = any([1, 2, 3, 0])
if all_p:
    print("all은 참이다")
else:
    print("all은 거짓이다")

if any_p:
    print("any은 참이다")
else:
    print("any은 거짓이다")

# all 은 전부가 참일때 True을 반환
# any는 하나라도 참일때 True을 반환한다.

# dir은 객체가 가진 변수나 함수를 보여준다
print(dir([1, 2, 3]))

# 7을 3으로 나눈 결과의 값과 나머지를 튜플 형태로 반환..
print(divmod(7, 3))

# 열거하다의 뜻을 가진 enumerate
for i, name in enumerate(["beomseok", "taewoo", "sanghwan"]):
    print(i, name)

# eval은 실행 가능한 문자열을 입력받아 결과값을 리턴하는 함수다

print(eval("'hi' + ' everyone'"))
print(eval('1+23'))
print(divmod(7, 3))

# filter는 리턴값이 참인것만 걸러내준다
expression = [1, 2, 3, 4, -5, -6]


def another_function(x):
    result_list = []
    for i in x:
        if i > 0:
            result_list.append(i)
    return result_list


def testing_function(x):
    return x > 0


# another_function으로 구현된 내용을 filter 함수는 간단히 수행할수 있게 한다.
# 대신 filter(함수, 반복 가능한 값)에서 함수의 괄호 내 인자가 생략되는데 그 인자가 뒤로 온다)

print(another_function(expression))
print(list(filter(testing_function, expression)))

# id의 사용, 고유의 주소값을 리턴
value_a = 3
value_b = value_a

print(id(value_a))
print(id(value_b))

# 참조복사의 비교
# 파이썬에서 변수는 값을 담는 그릇이 아니다. 그냥 값에 대한 라벨링 정도?


value_a = 5

print(id(value_a))
print(id(value_b))


# insistance : isinstance(인스턴스, 클래스) 인스턴스가 두번째 인자로 온 클래스의 인스턴스이면 True를 반환한다.
class Person:   pass


person = Person()
print(isinstance(person, Person))

# map 첫번째 인자로 함수를, 두번째 인자로 반복가능한 값을 받아서 그 값이 함수로 수행된 결과값을 재반환하는 함수다.
# map을 사용하지 않은 경우와 그것을 map으로 코딩했을때 어떻게 다른지 아래에 작성해본다.

# 리스트의 원소 값들에 각각 *2해서 리턴하는 함수
expression2 = [1, 2, 3, 4, 5, 6]


def testing_function2(num_list):
    result = []
    for i in num_list:
        result.append(i * 2)
    return result


print(testing_function2(expression2))


def two_times(x):
    return x * 2


print(list(map(two_times, expression2)))


#pow는 제곱한 결과를 리턴한다

print(pow(2,10))
print(pow(15,2))


#round 함수는 숫자를 입력받아 반올림 해주는 함수다.
print(round(4.6))
print(round(5.223, 2 )) #2번째 자리까지만


#sorted

print(sorted(['a', 'b', 'd', 'c']))


#sum 은 모든값을 합해 리턴하는 함수다. 리스트나 튜플의 모든 요소..
print(sum([1,2,3,4]))
