def matrixReshape(mat, r, c):

    m=len(mat)
    n=len(mat[0])
    if 1<=m and n<=100:
        if 1<=r and c<=300:
            print(m)
            print(n)
    return [m, n]


output= matrixReshape([[4,3,2,6,],[4,3,2]],2,2)
print(output)