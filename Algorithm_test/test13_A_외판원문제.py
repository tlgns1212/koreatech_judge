# import sys
# from queue import PriorityQueue
# import copy
# input = sys.stdin.readline
# INF = 1e6

# class Node :
#     def __init__(self):
#         self.level = 0
#         self.bound = 0
#         self.tour = []
        
#     def __lt__(self, other):
#         return self.bound > other.bound

#     # def findbound(self, items, W):
#     #     N = len(items)
#     #     nextIndex = self.level
#     #     bound = self.currProfit
#     #     totalWeight = self.currWeight
#     #     while nextIndex < N and totalWeight + items[nextIndex][1] <= W:
#     #         totalWeight += items[nextIndex][1]
#     #         bound += items[nextIndex][0]
#     #         nextIndex += 1
#     #     if nextIndex < N:
#     #         bound += (W-totalWeight) * items[nextIndex][2]
#     #     return bound


# def tsp(G):
#     Q = PriorityQueue()
#     root = Node()
#     root.level = 0
#     root.tour = [1]
#     root.bound = computeBound(root)                     # ?????
#     Q.put(root)
#     minLength = INF
#     while Q.empty() is not True:
#         node = Q.get()
#         if node.bound < minLength:
#             for i in range(2,len(G)):
#                 if i in node.tour:
#                     continue
#                 if G[node.tour[node.level]][i] == INF:
#                     continue
#                 next = copy.copy(node)
#                 next.level = node.level + 1
#                 next.tour.append(i)
#                 if next.level == len(G)-2:
#                     if len(next) < minLength:           # ??????
#                         minLength = len(next)
#                         solution = node.tour
#                 else:
#                     next.bound = computeBound(next)     # ????
#                     if next.bound < minLength:
#                         Q.get(next)
#     return minLength



# T = int(input())
# for _ in range(T):
#     N = int(input())
#     W = []
#     for i in range(N):
#         W.append(list(map(int,input().split())))
#     minLength = tsp(W)
#     print(minLength)


import sys
from queue import PriorityQueue
input = sys.stdin.readline
INF = 999

class SSTNode:
    def __init__ (self, level):
        self.level = level
        self.path = []
        self.bound = 0

    def contains(self, x):
        for i in range(len(self.path)):
            if (self.path[i] == x):
                return True
        return False

    def __lt__(self, other):
        return self.bound > other.bound

def travel2 (W):
    global minlength, opttour
    n = len(W) - 1
    PQ = PriorityQueue()
    v = SSTNode(0)
    v.path = [1]
    v.bound = bound(v, W)
    minlength = INF
    PQ.put((v.bound, v))
    while (not PQ.empty()):
        v = PQ.get()[1]
        if (v.bound < minlength):
            for i in range(2, n + 1):
                if (v.contains(i)):
                    continue
                u = SSTNode(v.level + 1)
                u.path = v.path[:]
                u.path.append(i)
                if (u.level == n - 2):
                    for k in range(2, n + 1):
                        if (not u.contains(k)):
                            u.path.append(k)

                    u.path.append(1)
                    if (length(u.path, W) < minlength):
                        minlength = length(u.path, W)
                        opttour = u.path[:]
                else:
                    u.bound = bound(u, W)
                    if (u.bound < minlength):
                        PQ.put((u.bound, u))


def bound(v, W):
    n = len(W) - 1
    total = length(v.path, W)
    for i in range(1, n + 1):
        if (hasOutgoing(i, v.path)):
            continue
        min = INF
        for j in range(1, n + 1):
            if (i == j): continue
            if (hasIncoming(j, v.path)): continue
            if (j == 1 and i == v.path[len(v.path) - 1]): continue
            if (min > W[i][j]): min = W[i][j]
        total += min
    return total

def length(path, W):
    total = 0
    prev = 1
    for i in range(len(path)):
        if (i != 0):
            prev = path[i - 1]
        total += W[prev][path[i]]
        prev = path[i]
    return total

def hasOutgoing(v, path):
    for i in range(0, len(path) - 1):
        if (path[i] == v):
            return True
    return False

def hasIncoming(v, path):
    for i in range(1, len(path)):
        if (path[i] == v):
            return True
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    W = []
    W.append([-1 for i in range(N)])
    for i in range(N):
        W.append(list(map(int,input().split())))
    for i in range(len(W)):
        W[i].insert(0,-1)
    for i in range(1,len(W)):
        for j in range(1,len(W)):
            if W[i][j] == -1:
                W[i][j] = INF
    opttour = None
    travel2(W)
    print(minlength)