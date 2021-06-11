#import sys
#T = int(sys.stdin.readline())
#A = []
#for _ in range(T):
#    count = {}
#    N = list(map(int,sys.stdin.readline().split()))
#    for i in N:
#        try : count[i] += 1
#        except : count[i] = 1
#    print(count)
#    print(count.index(max(count.values())))

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A = []
    k = 0
    i = -1
    N = list(map(int,input().split()))
    N.sort()
    n = -1
    for j in N:
        if j == n:
            A[i].append(k)
        elif j != n:
            A.append([j])
            n = j
            i += 1
    max = -1
    answer = -1
    for j in A:
        if max < len(j):
            max = len(j)
            answer = j[0]
    print(answer)

