# fun to find direction/step to move
def adj(i,j,m,n):
    i=[i+1,i,i-1]  #
    j=j+1
    ad=[]
    for ai in i:
        if 0<=ai<m and 0<=j<n:      #checking for boundry condition, to avoid index out of range
            ad.append((ai,j))
    return ad

def gold_mine(arr,m,n):

    for j in range(n-2,-1,-1):  # starting from second last column
        for i in range(m):      #for each column processing every row top to bottom
            mx=0
            ad=adj(i,j,m,n)     # array of step/direction to move from a particular point

            for ai,aj in ad:
                if arr[ai][aj]>mx:      # finding max of all reachable step
                    mx=arr[ai][aj]

            arr[i][j]+=mx               #updating maximum value that can be obtained from this point

    mx=0
    for i in range(m):                  #finding maximum from first column for answer
        if arr[i][0]>mx:
            mx=arr[i][0]

    return mx


if __name__=="__main__":
    t= int(input())
    for _ in range(t):
        m,n=[int(x) for x in input().split()]
        tarr= [int(x) for x in input().split()]
        arr=[]
        j=0
        for i in range(m):
            arr.append(tarr[j:j + n])
            j = j + n

        gold_mine(arr,m,n)