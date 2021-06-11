import sys
from queue import Queue
input = sys.stdin.readline

def bfs(s):
    count = 1
    que = Queue()
    visited[s] = True
    que.put(s)
    while que.qsize() != 0:
        v = que.get()
        for w in range(len(graph[v])):
            if not visited[w] and graph[v][w] == 1:
                visited[w] = True
                count += 1
                que.put(w)
    return count

T = int(input())
for _ in range(T):
    N, E = map(int,input().split())
    visited = [False for _ in range(N)]
    a = list(map(int,input().split()))
    count_list = []
    graph = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(0,len(a),2):
        graph[a[i]][a[i+1]] = 1
        graph[a[i+1]][a[i]] = 1
    for i in range(N):
        if not visited[i]:
            count_list.append(bfs(i))
    print(len(count_list),max(count_list))

    
    