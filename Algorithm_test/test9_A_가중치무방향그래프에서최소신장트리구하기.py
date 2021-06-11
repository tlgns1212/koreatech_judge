# PRIM 알고리즘
import sys
from heapq import *
from collections import defaultdict
input = sys.stdin.readline

def split(abc):
    a = []
    for i in range(0,len(abc),3):
        a.append([abc[i+2],abc[i],abc[i+1]])
    return a


T = int(input())
for _ in range(T):
    N, E = map(int, input().split())
    abc = list(map(int,input().split()))
    a = split(abc)
    queue = []
    graph = defaultdict(list)
    for i in a:
        graph[i[1]].append([i[0],i[2]])
        graph[i[2]].append([i[0],i[1]])
    X = set([0])
    T = graph[0]
    heapify(T)
    result = 0

    while T:
        weight, node = heappop(T)
        if node not in X:
            X.add(node)
            result += weight

            for edge in graph[node]:
                if edge[1] not in X:
                    heappush(T,edge)
    print(result)