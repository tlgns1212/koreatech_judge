import sys
input = sys.stdin.readline

def PIC(first, unvisited):
    if not unvisited:
        return 1
    all = 0
    for i in range(first,N):
        if not visited[i]:
            for j in range(i + 1, N):
                if not visited[j] and isFriend[i][j]:
                    visited[i] = visited[j] = True
                    all +=PIC(i, unvisited - 2)
                    visited[i] = visited[j] = False
    return all

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    friend = list(map(int,input().split()))
    visited = [False] * N
    isFriend = [[False] * N for _ in range(N)]

    for i in range(0, len(friend), 2):
        isFriend[friend[i]][friend[i+1]] = True
        isFriend[friend[i+1]][friend[i]] = True
    print(PIC(0,N))