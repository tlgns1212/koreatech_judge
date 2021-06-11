import sys
input = sys.stdin.readline


# def optimalBST(F):
#     n = len(F)
#     A = [[0 for _ in range(n+1)] for _ in range(n+2)]
#     R = [[0 for _ in range(n+1)] for _ in range(n+2)]
#     for i in range(1,n+1):
#         A[i-1][i] = 0
#         A[i][i] = F[i-1]
#         R[i][i] = i
#         R[i-1][i] = 0
#     for diagonal in range(1,n):
#         for i in range(1,n-diagonal+1):
#             j = i + diagonal
#             minval = 9999

#             for k in range(i,j+1):
#                 if (A[i][k-1] + A[k+1][j]) < minval:
#                     minval = A[i][k-1] + A[k+1][j]
#                     kmin = k
#             R[i][j] = kmin
#             sum = F[i-1]
#             for s in range(i+1,j+1):
#                 sum = sum + F[s-1]
#                 A[i][j] = minval + sum
#     max = 0
#     for i in A:
#         for j in i:
#             if max < j and j != 9999:
#                 max = j
#     return max


def optimalBST(F):
    n = len(F)
    C = [[None for _ in range(n+2)]for _ in range(n+2)]
    for i in range(1,n+2):
        C[i][i-1] = 0
    for s in range(n):
        for i in range(1,n-s+1):
            total = 0
            opt = 999999
            for r in range(i,i+s+1):
                total += F[r-1]
                opt = min(opt,C[i][r-1] + C[r+1][i+s])
            C[i][i+s] = total+opt
    return C[1][n]
    


T = int(input())
for _ in range(T):
    N = int(input())
    F = list(map(int,input().split()))
    max = optimalBST(F)
    print(max)