# coding=utf-8

"""
하노이의 탑
- https://namu.wiki/w/하노이의%20탑

하노이의 탑을 구현해 봅시다.

이런, 프로그램을 작성하다 중간에 멈췄네요.
적당히 완성시켜 봅시다.

"""


def hanoi( first: int, second: int, third: int, amount: int ):
    tags = [ "첫번째", "두번째", "세번째" ]

    # 종료 조건
    # TODO - 종료 조건을 적당히 수정해 주세요
    if amount <= 1 :
        # 가장 아래의 것(=amount)이 1개 남았을 경우, 현재 위치에서 목표 위치로 옮기고 종료
        print( f"원반 {amount}번을 {tags[first]} 고리에서 {tags[third]} 고리로 옮깁니다." )

    else:
        # 가장 아래의 것(=amount)의 바로 위 전체(amount-1부터 1까지)를 목표의 옆으로 옮기고
        hanoi( first, third, second, amount - 1 )

        # 가장 아래의 것(=amount)를 목표로 옮기고
        print( f"원반 {amount}번을 {tags[first]} 고리에서 {tags[third]} 고리로 옮깁니다." )

        # 아까 목표 옆에 치워뒀던 나머지(amount-1부터 1까지)를 옆에서 목표로 옮긴다.
        # TODO - 아래 부분을 수정해 주세요.
        hanoi( second , first, third , amount - 1 )



if __name__ == '__main__':
    x = 5

    hanoi( 0, 1, 2, x )
