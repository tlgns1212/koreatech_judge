import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    if N <= 0:
        print('false')
        continue
    a = set()
    a.update(map(int,sys.stdin.readline().split(' ')))
    print('false' if len(a) == N else 'true')
