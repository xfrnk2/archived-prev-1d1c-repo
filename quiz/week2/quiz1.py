# coding=utf-8

"""
앵무새를 만듭니다.

프로그램을 실행 시키면 아래와 같이 나오고 입력을 받습니다.

(나) >

각 입력을 완료하는 방법은 엔터키 입력 입니다.




(나) > 안녕?
(앵무새) > 안녕?
(나) > 메롱
(앵무새) > 메롱
(나) > 잘가
(앵무새 프로그램을 종료합니다)


잘가 라고 입력하고 엔터를 치면 프로그램이 종료 됩니다.
잘가 라는 입력으로 프로그램을 종료하기 전까지 앵무새는 무한히 내가 하는 말을 따라합니다.

"""
while True:
    parrot = input("(나) > ")
    if parrot == "잘가":
        print("(앵무새가 프로그램을 종료합니다)")
        break
    else:
        print("(앵무새) > " + parrot)
        continue