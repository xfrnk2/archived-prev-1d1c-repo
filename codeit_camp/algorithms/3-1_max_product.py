# 풀고 보니, 브루트 포스 알고리즘 기준에서 풀해설에 나온 답안은 2중 for문으로 소개가 되어있다. 내 생각에 이게 조금더 효율적인 방법일 것 같아서 아래와 같이 코드를 작성했다.
def max_product(left_cards, right_cards):
    # 코드를 작성하세요.

   lm, ln = max(left_cards), min(left_cards)
   rm, rn = max(right_cards), min(right_cards)
   
   return max(lm*rm, ln*rn)
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))