# https://www.acmicpc.net/problem/9012
# 첫 번째 풀이.
# T = int(input())
#
# for _ in range(T):
#     ps = input().rstrip()
#     stack_count = 0
#     condition = True
#
#
#     for i in ps:
#        if i == "(":
#            stack_count += 1
#        elif i == ")":
#            if stack_count <= 0:
#                condition = False
#                break
#            stack_count -= 1
#
#     if condition and stack_count == 0:
#         print("YES")
#     else:
#         print("NO")

# 두 번째 풀이. 리팩토링 해보고자 전번 코드와 다르게 수정해봤는데, 메모리나 시간적 효율 상승은 없었다..
import sys

T = int(sys.stdin.readline().rstrip())
PS = [sys.stdin.readline().rstrip() for _ in range(T)]
i = 0

output = ''
while i < T:
    answer = "NO"
    j = 0
    stack_count = 0
    for s in PS[i]:


       if s == "(":
           stack_count += 1
       else:
           if stack_count <= 0:
               break
           stack_count -= 1
       j += 1


    if j == len(PS[i]) and stack_count == 0:
        answer = "YES"

    output += answer + '\n'
    i += 1
print(output)
#
