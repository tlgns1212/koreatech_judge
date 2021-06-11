
#     # A는 염기
#     # B는 슬라이드,
#     # C는 



import sys
input = sys.stdin.readline

def SequenceAlignment(X,Y,gap,miss):
    def isa(i,j):
        if X[j] == Y[i]:
            return 0
        # elif X[j] == "0" or Y[i] == "0":
        #     return gap
        else:
            return miss
        
    m = len(X)
    n = len(Y)
    while len(X) < len(Y):
        X += " "
    while len(Y) < len(X):
        Y += " "
    m2 = len(X)
    n2 = len(Y)
    A = [[0 for _ in range(m2 + 1)] for _ in range(n2 + 1)]
    for i in range(n2+1):
        A[i][0] = i * gap
    for j in range(m2+1):
        A[0][j] = j * gap
    for i in range(1,n2+1):
        for j in range(1,m2+1):
            A[i][j] = min(A[i-1][j-1] + isa(i-1,j-1), A[i-1][j] + gap, A[i][j-1] + gap)
    return A[n][m]



T = int(input())
for _ in range(T):
    S1 = input()
    S2 = input()
    answer = SequenceAlignment(S1,S2,1,1)
    print(max(len(S1),len(S2)) - answer - 1)