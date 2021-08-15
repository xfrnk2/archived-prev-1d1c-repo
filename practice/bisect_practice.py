from bisect import bisect_left, bisect_right
'''
용도 : 요약 - "정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때" 효과적으로 사용할 수 있다.
1. O(log n)의 시간으로 특정 데이타를 찾고 싶을 때
2. 값의 범위가 정해져 있을 때 해당 범위에 있는 데이터의 개수를 출력하고자 할 때
'''

a = [1, 2, 3, 4, 4, 4, 5, 6]
# 데이터 리스트 a에 속한 4의 갯수 구하는 방법
print(bisect_left(a, 4))
print(bisect_right(a, 4))

count_data = bisect_right(a, 4) - bisect_left(a, 4)
print('count :', count_data)

# 데이터 리스트 a에 속한 원소 중 2에서 5 사이인 값을 가진 원소의 갯수 구하는 법
count_two_to_five = bisect_right(a, 5) - bisect_left(a, 2)
print('2~5사이의 원소 갯수', count_two_to_five)


'''
카운트 하거나
일정 범위안에 있는 원소 갯수
'''
# https://velog.io/@peterpictor/Python-bisect-%ED%99%9C%EC%9A%A9%ED%95%B4-%EB%B2%94%EC%9C%84-%ED%83%90%EC%83%89%ED%95%98%EA%B8%B0

