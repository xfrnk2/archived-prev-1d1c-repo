# 이해를 도와준 사이트 : https://rednooby.tistory.com/81

def matrixMul2Byte(a, b):

    ar, ac = len(a), len(a[0])
    br, bc = len(b), len(b[0])

    assert ac == br, "앞 행렬의 열 갯수, 뒤 행렬의 행 갯수가 불일치"

    matrix = []
    for k in range(ac):
        answer = []
        for i in range(ar):
            result = 0
            for j in range(ac):
                mul = a[k][j] * b[j][i]
                print(f"k : {k}, i : {i}, j : {j}")
                print(f"a[k][j] : {a[k][j]}, b[j][i] : {b[j][i]}, mul : {mul}")

                result += mul
                print(f"result = {result}")
                print("======================")
            answer.append(result)
        matrix.append(answer)
    return matrix




a = [ [ 1, 2 ], [ 3, 4 ]]
b = [[ 5, 6], [7, 8]]
print(f"{matrixMul2Byte(a, b)}")