
def search(arr,low,high):
    # Base cases
    if low>high:
        return 0

    if low == high:
        return arr[low]

    # Find the middle point
    mid = (low+high)//2

    # If mid is even and element next to mid is
    #   same as mid, then output element lies on
    #   right side, else on left side
    if mid%2==0:
        if arr[mid] == arr[mid+1]:
            return search(arr,mid+2,high)
        else:
            return search(arr,low,mid)

    # If mid is odd
    else:
        if arr[mid] == arr[mid-1]:
            return search(arr,mid+1,high)
        else:
            return search(arr,low,mid-1)

def appearsOnce(arr,n):

    return search(arr,0,n-1)

if __name__ == '__main__':
    T=int(input())

    for _ in range(T):
        n=int(input())
        arr=[int(x) for x in input().split()]

        print(appearsOnce(arr,n))
