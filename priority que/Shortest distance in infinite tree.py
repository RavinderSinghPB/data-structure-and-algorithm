def dist(x,y):
    c=0

    while x!=y:
        if x>y:
            x= x//2
            c+=1
        else:
            y=y//2
            c+=1
    return c



if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        x,y=[int(x) for x in input().split()]
        print(dist(x,y))