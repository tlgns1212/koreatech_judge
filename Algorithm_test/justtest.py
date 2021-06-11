import sys

T = int(sys.stdin.readline())

for i in range(T):
    N,E = map(int, sys.stdin.readline().split())
    line = list(map(int, sys.stdin.readline().split()))

    adjMat = [[0 for i in range(N)] for i in range(N)]

    for j in range(0,E*2,2):
        adjMat[line[j]][line[j+1]] = 1
        adjMat[line[j+1]][line[j]] = 1

    visited = [False]*N
    components = []
    Q=[]
    for i in range(N):
        component=[]
        if visited[i] == False:
            visited[i] = True
            Q.append(i)
            while len(Q) > 0:
                c = Q.pop(0)
                component.append(c)
                for j in range(N):
                    if adjMat[c][j]==1 and not visited[j]:
                        visited[j] = True
                        Q.append(j)
            if len(component)!=0:
                components.append(list(component))
    max = 0
    for i in components:
        if max<len(i):
            max = len(i)
    print(len(components),max)