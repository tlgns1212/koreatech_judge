import sys
from queue import PriorityQueue
import copy
input = sys.stdin.readline
INF = 1e6

class Node :
    def __init__(self, G):
        self.level = -1
        self.tour = []
        self.bound = self.computeBound(G)
        
    def __lt__(self, other):
        return self.bound > other.bound

    def computeBound(self, G):
        G1 = list(G)
        nextIndex = self.level
        tour = self.tour
        notvisited = [True for i in range(len(G1))]
        for i in tour:
            if i in notvisited:
                notvisited[i] = False
        bound = 0
        for i in tour:
            bound += G1[nextIndex][i]
        for i in tour:
            G1[nextIndex][i] = INF
        for i in range(len(notvisited)):
            if notvisited[i]:
                bound += min(G1[i])
        return bound




def knapsack(G):
    global n
    Q = PriorityQueue()
    root = Node(G)# 루트 노드
    root.tour = [1]
    minLength = INF
    Q.put(root)
    while Q.empty() is not True:
        node = Q.get()
        if node.bound < minLength:
            for i in range(2,n):
                if i in node.tour:
                    continue
                if G[node.tour[node.level]][i] == INF:
                    continue
                next = copy.copy(node)
                next.level = node.level + 1
                next.tour.append(i)
                if next.level == n-1:
                    #
                    if len(next) < minLength:
                        minLength = len(next)
                        solution = node.tour
                else:
                    next.bound = next.computeBound(G)
                    if(next.bound < minLength):
                        Q.put(next)
    return minLength






T = int(input())
for _ in range(T):
    n = int(input())
    S = []
    for _ in range(n):
        S.append(list(map(int,input().split())))
    a = knapsack(S)
    print(a)
    