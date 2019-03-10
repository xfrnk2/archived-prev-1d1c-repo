try:
    a = [1,2]
    print(a[3])
    b = 4/0

#2개 이상의 에러를 동시에 처리하기 위해서는 아래와 같이 한다.
except(ZeroDivisionError, IndexError) as e:
    print(e)

except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

    #아래의 경우는 어떤 종류의 에러던지 에러가 발생했을때 except 블록을 수행한다.
except:
    print("에러는 발생했는데 어떤 에러인지는 모른다")



#2

try:
    f = open("없는파일이다", 'r')
except FileNotFoundError:
    # print("없는 파일이야")
    pass



#3
#각종에러와 예외 발생 코드 종류
#https://docs.python.org/ko/3/library/exceptions.html

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):

    # 추상 메서드나 클래스를 재정의 하기 위해서, 또는 실제 구현이 필요할 때 예외를 발생시킨다. notimplementederror
    def fly(self):
        print("very fast bird")
    # pass
    #에러 발생

eagle = Eagle()
eagle.fly()

#4

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == "바보":
        raise MyError
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않은 별명입니다")


#5 : result의 최종 값은? 문제....

result = 0
try:
    value = [1, 2, 3][3]
    value2 = "a"+ 1
    value3 = 4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)

#indexerror가 발생 후 finally 구문의 += 4 코드가 수행되서 result의 최종 결과값은 7이 된다.