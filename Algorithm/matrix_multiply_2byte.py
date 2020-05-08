def matrixMul2Byte(a, b):

    assert len(a[0]) == len(b), "앞 행렬의 열 갯수, 뒤 행렬의 행 갯수가 불일치"

    matrix = []
    for k in range(2):
        answer = []
        for i in range(2):
            result = 0
            for j in range(2):
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