def sumMatrix(a, b):

    ar, ac = len(a), len(a[0])
    br, bc = len(b), len(b[0])
    assert ar == br and ac == bc, "행과 열의 갯수가 불일치"

    matrix = []
    #00 01 10 11 ....
    for i in range(ar):
        answer = []
        for j in range(ac):
            result = a[i][j] + b[i][j]
            print(f"i : {i}, j : {j} \n a[i][j] : {a[i][j]}, b[i][j] : {b[i][j]} \n sum : {result}")
            answer.append(result)
        matrix.append(answer)


    return matrix


print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
print("===============")
print(sumMatrix([[1,3,5], [2,4,6]], [[2,4,7],[1,5,3]]))