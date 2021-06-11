# import sys
# from queue import PriorityQueue
# import copy
# input = sys.stdin.readline

# class Node :
#     def __init__(self):
#         self.level = -1
#         self.currProfit = 0
#         self.currWeight = 0
#         self.bound = self.findbound(items, W)
        
#     def __lt__(self, other):
#         return self.bound > other.bound

#     def findbound(self, items, W):
#         N = len(items)
#         nextIndex = self.level
#         bound = self.currProfit
#         totalWeight = self.currWeight
#         while nextIndex < N and totalWeight + items[nextIndex][1] <= W:
#             totalWeight += items[nextIndex][1]
#             bound += items[nextIndex][0]
#             nextIndex += 1
#         if nextIndex < N:
#             bound += (W-totalWeight) * items[nextIndex][2]
#         return bound

# def promising(node, items, W, maxProfit):
#     if node.currWeight >= W:
#         return False
#     else:
#         nextIndex = node.level
#         bound = node.currProfit
#         totalWeight = node.currWeight
#         while nextIndex < len(items) and totalWeight + items[nextIndex][1] <= W:
#             totalWeight += items[nextIndex][1]
#             bound += items[nextIndex][0]
#             nextIndex += 1
#         if nextIndex < len(items):
#             bound += (W - totalWeight) * items[nextIndex][2]
#         node.bound = bound
#         return bound > maxProfit

# # def knapsack(items, W):
# #     maxProfit = 0
# #     Q = PriorityQueue()
# #     root = Node()# 루트 노드
# #     Q.put(root)
# #     while Q.empty() is not True:
# #         node = Q.get()
# #         if node.bound > maxProfit:
# #             node.level += 1
# #             if node.level >= len(items):
# #                 continue
# #             node.currWeight += items[node.level][1]
# #             node.currProfit += items[node.level][0]
# #             if node.currWeight <= W and node.currProfit > maxProfit:
# #                 maxProfit = node.currProfit
# #             node.bound = node.findbound(items,W)
# #             if node.bound > maxProfit:
# #                 Q.put(copy.copy(node))
# #             node.currWeight -= items[node.level][1]
# #             node.currProfit -= items[node.level][0]
# #             node.bound = node.findbound(items,W)
# #             if node.bound > maxProfit:
# #                 Q.put(copy.copy(node))
# #     return maxProfit


# # def knapsack(items, W):
# #     maxProfit = 0
# #     Q = PriorityQueue()
# #     root = Node()# 루트 노드
# #     Q.put(root)
# #     while Q.empty() is not True:
# #         node = Q.get()
# #         node.level += 1
# #         if node.level >= len(items):
# #             continue
# #         node.currWeight += items[node.level][1]
# #         node.currProfit += items[node.level][0]
# #         if promising(node, items, W, maxProfit):
# #             if node.currWeight <= W and node.currProfit > maxProfit:
# #                 maxProfit = node.currProfit
# #             Q.put(copy.copy(node))
# #         node.currWeight -= items[node.level][1]
# #         node.currProfit -= items[node.level][0]
# #         if promising(node, items, W , maxProfit):
# #             Q.put(copy.copy(node))
# #     return maxProfit


# def knapsack(items, W):
#     maxProfit = 0
#     Q = PriorityQueue()
#     root = Node()# 루트 노드
#     Q.put(root)
#     while Q.empty() is not True:
#         node = Q.get()
#         node.level += 1
#         if node.level >= len(items):
#             continue
#         node.currWeight += items[node.level][1]
#         node.currProfit += items[node.level][0]
#         node.bound = node.findbound(items,W)
#         if node.bound > maxProfit:
#             if node.currWeight <= W and node.currProfit > maxProfit:
#                 maxProfit = node.currProfit
#             Q.put(copy.copy(node))
#         node.currWeight -= items[node.level][1]
#         node.currProfit -= items[node.level][0]
#         node.bound = node.findbound(items,W)
#         if node.bound > maxProfit:
#             Q.put(copy.copy(node))
#     return maxProfit


# T = int(input())
# for _ in range(T):
#     W, N = map(int,input().split())
#     vw = list(map(int,input().split()))
#     items = []
#     for i in range(0,len(vw),2):
#         items.append([vw[i],vw[i+1],vw[i]/vw[i+1]])
#     items.sort(key = lambda x : x[2], reverse=True)
#     a = knapsack(items,W)
#     print(a)




import sys
from queue import PriorityQueue
input = sys.stdin.readline


class SSTNode:
    def __init__ (self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = 0

    def __lt__(self, other):
        return self.bound > other.bound


def knapsack4 (p, w, W):
    PQ = PriorityQueue()
    v = SSTNode(-1, 0, 0)
    maxprofit = 0
    v.bound = bound(v, p, w)
    PQ.put((-v.bound, v))
    while (not PQ.empty()):
        v = PQ.get()[1]
        if (v.bound > maxprofit):
            level = v.level + 1
            weight = v.weight + w[level]
            profit = v.profit + p[level]
            u = SSTNode(level, profit, weight)
            if (u.weight <= W and u.profit >= maxprofit):
                maxprofit = u.profit
            u.bound = bound(u, p, w)
            if (u.bound > maxprofit):
                PQ.put((-u.bound, u))
            u = SSTNode(level, v.profit, v.weight)
            u.bound = bound(u, p, w)
            if (u.bound > maxprofit):
                PQ.put((-u.bound, u))
    return maxprofit

def bound(u, p, w):
    n = len(p) - 1
    if (u.weight >= W):
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while (j <= n and totweight + w[j] <= W):
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if (k <= n):
            result += (W - totweight) * p[k] / w[k]
        return result

T = int(input())
for _ in range(T):
    W, N = map(int,input().split())
    profit = []
    weight = []
    vw = list(map(int,input().split()))
    items = []
    for i in range(0,len(vw),2):
        items.append([vw[i],vw[i+1],vw[i]/vw[i+1]])
    items.sort(key = lambda x : x[2], reverse=True)
    for i in range(len(items)):
        profit.append(items[i][0])
        weight.append(items[i][1])
    maxprofit = knapsack4(profit,weight,W)
    print(maxprofit)