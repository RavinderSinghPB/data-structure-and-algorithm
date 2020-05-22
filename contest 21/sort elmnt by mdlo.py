def srt(arr,k):
    arr.sort()
    arr.sort(key= lambda x:x%k)
    print(*arr)

arr=[3, 4, 5, 10, 11, 1]
k=3

srt(arr,k)