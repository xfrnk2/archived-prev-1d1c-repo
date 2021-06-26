'''
어디까지나 기억에 의존한 대략적인 문제 내용을 아래에 적고, 코드를 짰다.


bool, short, long, int, long
1, 2, 4, 8, 16

8byte의 한칸을 '#' 또는 ','이 차지할 수 있다.
데이터 자료형의 크기만큼 '#'로 채워지고, 그 사이를 패딩이라고 부르는 ','로 채운다.

패딩을 ','이라고 정의하고, 각 데이터의 크기만큼 '#'
bool 다음 숏이나 롱이 올 경우 각각 1, 3개의 패딩을 붙여야 한다.

모두 8자리씩 나뉘어 져야 하고, 예를 들어 int, longlong ,longlong이 온다면
[########, ########, ########, ########, ########] 이 될 것임.

현재 8개 비트 범위 내에서 다음으로 올 것의 크기가 8을 초과한다면 패딩 처리 후 해당 갯수만큼 #로 채운다.
'''


items = {'bool': '#', 'short' : "##", 'long' : "####", 'int' : "########", 'longlong': "########,########"}

def func(param0):
    prev = False
    answer = ''
    buffer = ''
    for data in param0:

        d = len(items[data])

        c_temp = ''
        p_temp = 0

        if prev:

            if 2 <= d <= 4:
                p_temp += d - 1
            elif 8 <= d and buffer != '':
                p_temp += 8 - len(buffer)
        else:
            if 8 - len(buffer) < d: # 현재 남아있는 공간이 들어가려고 하는 데이터 크기보다 작을 때
                p_temp += 8 - len(buffer)

        while 0 < p_temp and len(buffer) < 8:
            buffer += ','
            p_temp -= 1

        c_temp += items[data]
        buffer += c_temp

        if len(buffer) == 8:
            buffer += ','
            answer += buffer
            buffer = ''
        prev = d == 1

    return answer[:-1]
print(func(['int', 'bool', 'long']))
'''
1. 이전 값이 bool인지 확인하여 그렇다면 short~long이라면 패딩의 갯수를 -1개 만큼 함.
- 필요한 변수 : 패딩의 갯수 : 구하는 방법 : 전체 버퍼 크기와 현재 데이터의 크기의 차가 존재하여 그 값이 c라고 할 때 그것을 카운트 해서 갯수를 넘지 
않는 선에서 임시 변수 내에(temp) 추가 가능
 
2. 이전 값이 bool인지 확인하여 그렇다면 short~long이 아니라면 그대로 뒤에 붙이는데, 만약 8 이상의 크기라면
전체 버퍼 크기와 현재 데이터의 크기의 차만큼 패딩을 임시 변수 내에(temp) 추가

3. 이전 값이 bool이 아니라면 현재 전체 데이터 버퍼 크기와 이미 버퍼에 들어차있는 데이터의 크기의 차이가 현재 데이터의 크기보다 작을 경우
남은 칸을 패딩으로 채움

4. 임시 변수 temp에 패딩의 양을 담았고, 먼저 전체 버퍼의 크기에서 현재 차있는 데이터의 크기의 차 보다 현재 데이터의 크기가 작거나 같다면
버퍼에 현재 데이터를 추가

5. 위에서 구한 패딩의 값을 버퍼에 더함

6. 만약 버퍼의 길이가 8 이상일 경우 ,을 붙임  

7. 현재 값이 bool인 경우 변수 prev를 True로 만듦

'''
