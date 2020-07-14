''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    vlnstr = input().split()
    vln = []
    for e in vlnstr:
        vln.append(int(e))
    plrEnrg = input().split()
    plr = []
    for e in plrEnrg:
        plr.append(int(e))

    vln.sort()
    plr.sort()

    for i in range(n):
        if plr[i] <= vln[i]:
            print('LOSE')
            return
    print('WIN')


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        main()

