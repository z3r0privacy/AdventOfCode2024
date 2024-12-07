import math

def read_input(lines):
    ll = []
    rl = []
    for l in lines:
        p = l.split(" ")
        ll.append(int(p[0]))
        rl.append(int(p[-1]))
    return ll, rl

if __name__ == "__main__":
    ll, rl = read_input(open("inputs/day01.txt").readlines())
    ll.sort()
    rl.sort()
    d = 0
    for i in range(len(ll)):
        d += abs(ll[i]-rl[i])
    print(d)

    d = 0
    for n in ll:
        d += n*len([_n for _n in rl if _n==n])
    print(d)