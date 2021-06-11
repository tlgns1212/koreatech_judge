# Kruskal 알고리즘
import sys
input = sys.stdin.readline

def split(abc):
    a = []
    for i in range(0,len(abc),3):
        a.append([abc[i+2],abc[i],abc[i+1]])
    return a

def find(u):
    if u != P[u]:
        P[u] = find(P[u])
    return P[u]

def union(u,v):
    root1 = find(u)
    root2 = find(v)
    P[root2] = root1


T = int(input())
for _ in range(T):
    N, E = map(int, input().split())
    abc = list(map(int,input().split()))
    graph = split(abc)
    graph.sort(key = lambda x : x[0])

    X = []
    P = [0]

    for i in range(1, N+1):
        P.append(i)

    
    edges = 0
    result = 0

    while True:
        if edges == N-1:
            break
        weight, u, v = graph.pop(0)
        if find(u) != find(v):
            union(u,v)
            X.append([u,v])
            result += weight
            edges += 1
    
    print(result)