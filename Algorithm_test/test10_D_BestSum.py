import sys
input = sys.stdin.readline
# from random import *

# Memoization
def bestSum(M,X,Memo):
    if M < 0:
        return None
    elif M == 0:
        return []
    elif M in Memo:
        return Memo.get(M)
    best = None
    for x in X:
        list1 = bestSum(M-x,X,Memo)
        if list1 != None:
            if best == None or len(best) > len(list1) + 1:
                next = list(list1)
                next.append(x)
                best = next
                Memo[M] = best
    return best


# Tabulation
def bestSum1(M,X):
    table = [[None] for _ in range(M+1)]
    table[0] = []
    # if M == 0:  
    #     return [None]
    for i in range(M):
        if table[i] != [None]:
            for x in X: 
                if i + x <= M:
                    best = table[i+x]
                    if best == [None] or (len(best) > (len(table[i]) + 1)):
                        next = list(table[i])
                        next.append(x)
                        table[i+x] = next
    return table[M]


T = int(input())
for _ in range(T):
    M,N = map(int,input().split())
    X = list(map(int,input().split()))
    # Memo = {0:0}
    # a = bestSum(M,X,Memo)
    a = bestSum1(M,X)
    if a == [None] or a == None:
        print(-1)
    else:
        print(len(a), end = " ")
        for i in a:
            print(i, end = " ")
        print()

# T = randint(1,1001)
# print("T",T)
# for _ in range(T):
#     M = randint(0,1001)
#     print("M",M)
#     N = randint(2,101)
#     print("N",N)
#     X_list = []
#     for _ in range(N):
#         X = randint(1,201)
#         while X in X_list:
#             X = randint(1,201)
#         X_list.append(X)
#     print("X",X_list)
#     a = bestSum1(M,X_list) 
#     if a == None:
#         print(-1)
#     else:
#         max = 0
#         for i in a:
#             print(i, end = " ")
#             max += i
#         print()
#         print("M - max",M - max)
