"""
quiz1의 앵무새 프로그램을 여기에서 수정합니다.

내가 입력한 채팅 내용을 파일로 저장합니다.


(나) > 안녕?
(앵무새) > 안녕?
(나) > 메롱
(앵무새) > 메롱
(나) > 저장 a.txt
(여태까지의 대화 내용을 a.txt 파일로 저장합니다)
(나) > 다시 안녕?
(앵무새) > 다시 안녕?
(나) > 또 메롱
(앵무새) > 또 메롱
(나) > 저장 b.txt
(여태까지의 대화 내용을 b.txt 파일로 저장합니다)
(나) > 잘가
(앵무새 프로그램을 종료합니다)


a.txt 에는

안녕?
메롱



b.txt 에는

다시 안녕?
또 메롱


위와 같이 저장해야 합니다.



"""


#

import os

outPath = os.path.join('C:\\', 'users', 'documents', 'kbs', 'test.txt')
print(outPath)

def parrot():
    flag = True
    hello = ''

    while flag:

        parrot = input("(나) > ")
        if parrot == "잘가":
            print("(앵무새가 프로그램을 종료합니다)")

            flag = False
            continue

        elif "저장" in parrot:

            parrot.replace("저장", '')

            with open(f'{parrot}.txt', 'a') as file:
                print(f"(여태까지의 대화내용을 {parrot}.txt 파일로 저장합니다)")

                file.write(hello)

        else:
            text = [print("(앵무새) > " + parrot)]
            hello += parrot
            hello += "\n"


if __name__ == '__main__':
    parrot()
