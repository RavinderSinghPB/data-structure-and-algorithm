def Maximum_Sum(mat,n,k):
    stripSum=[[0]*n]*n

    for j in range(n):
        sm=0

        for i in range(k):
            sm+=mat[i][j]
        stripSum[0][j]=sm

        for i in range(1,n-k+1):
            sm+= (mat[i+k-1][j] - mat[i-1][j])
            stripSum[i][j]=sm

    max_sum=-inf


    for i in range(n-k+1):
        sm=0

        for j in range(k):
            sm+=stripSum[i][j]

        if sm>max_sum:
            max_sum=sm

        for j in range(1,n-k+1):
            sm+=(stripSum[i][j+k-1] - stripSum[i][j-1])

            if sm>max_sum:
                max_sum=sm
    return max_sum

if __name__ =='__main__':
    from mathpro.math import inf

    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        mat=[]

        for _ in range(n):
            row=[int(x) for x in input().split()]

            mat.append(row)

        k = int(input())

        #print(mat)



        print(Maximum_Sum(mat,n,k))
        print('~')