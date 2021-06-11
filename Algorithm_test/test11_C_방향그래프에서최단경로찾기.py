import sys
input = sys.stdin.readline
INF = 1e6

def floyd(N,W):

    D = [[INF for _ in range(N)]for _ in range(N)]
    for i in W:
        D[i[0]][i[1]] = i[2]
    for i in range(len(D)):
        D[i][i] = 0
    n = len(D)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    for i in range(n):
        if D[i][i] < 0:
            return -1
    max = 0
    lindex = []
    for i in range(n):
        for j in range(n):
            if max < D[i][j] and D[i][j] < 100000:
                max = D[i][j]
    for i in range(n):
        for j in range(n):
            if max == D[i][j]:
                lindex.append([i,j,max])
    return lindex



T = int(input())
for _ in range(T):
    N, E = map(int,input().split())
    SDW = list(map(int,input().split()))
    line = []
    for i in range(0,len(SDW),3):
        line.append([SDW[i],SDW[i+1],SDW[i+2]])
    A = floyd(N,line)
    if A == -1:
        print(-1)
    else:
        print(A[0][0], A[0][1], A[0][2])
    