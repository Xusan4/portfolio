import math
n = int(input("Введите число неизвестных + 1: "))
matric = [0] * (n - 1)
for i in range(n-1):
    matric[i] = [0] * n
for i in range(n-1):
    for j in range(n):
        matric[i][j] = float(input("введите"))
print(matric)
for i in range(n-1):
    # print(matric[i][i], end='^')
    if matric[i][i] != 1:
        delitel = matric[i][i]
        for j in range(n):
            # print(matric[i][j], end='-')
            matric[i][j] /= delitel
            # print(matric[i][j])
    for j in range(i+1, n-1):
        if matric[j][i] != 0:
            for k in range(n):
                mnojitel = matric[j][i]
                matric[j][k] -= matric[i][k] * mnojitel  
print(matric)


new_mat = [0] * (n - 1)
for i in range(n-1):
    new_mat[i] = [0] * n
for i in range(n-1):
    for j in range(n):
        if j < n-1:
            new_mat[i][j] = matric[-i-1][-j-2]
        else:
            new_mat[i][j] = matric[i][j]
for i in range(n-1):
    for j in range(i+1, n-1):
        if new_mat[j][i] != 0:
            for k in range(n):
                mnojitel = new_mat[j][i]
                new_mat[j][k] -= new_mat[i][k] * mnojitel
print(new_mat)
for i in range(n-1):
    print(f'X_{i+1} = {matric[i][-1]}')
