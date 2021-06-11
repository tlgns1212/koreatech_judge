import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(N, start, end, graph):
    q = []
    dist = [INF] * N
    dist[start-1] = 0
    count = 1
    heapq.heappush(q,[start-1, 0])

    while q:
        pos, value= heapq.heappop(q)
        for p, v in graph[pos]:
            v += value
            count += 1
            if v < dist[p]:
                dist[p] = v
                heapq.heappush(q, [p, v])
    return dist[end-1]



T = int(input())
for _ in range(T):
    b = list(map(int,input().split()))
    N, E, S, K, d = b[0], b[1], b[2], b[3], b[4:]
    a = list(map(int,input().split()))
    graph = [[]for _ in range(N)]
    answer = []
    for i in range(0,len(a),3):
        u, v, w = a[i], a[i+1], a[i+2]
        graph[u-1].append([v-1,w])
        print("u,v,w",u,v,w)
        print(graph[u-1],u-1)
    print(graph)
    for i in d:
        answer.append(dijkstra(N,S,i,graph))
    for i in answer:
        if i == INF :
            print(-1,end = " ")
        else:
            print(i,end = " ")
    print()