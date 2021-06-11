import sys
sys.stdin.readline
# 메모이제이션
def canSum(M, X, Memo):
    if M < 0:
        return False
    if M == 0:
        return True
    if M in Memo:
        return Memo[M]
    for x in X:
        if canSum(M-x,X,Memo):
            Memo[M] = True
            return True
    Memo[M] = False
    return False

# 테뷸레이션
def canSum1(M,X):
    table = [False for _ in range(M+1)]
    table[0] = True
    for i in range(M-1):
        if table[M]: return True
        if table[i]:
            for x in X:
                if i+x <= M:
                    table[i+x] = True
        
                    
    return table[M]

T = int(input())
for _ in range(T):
    M,N = map(int,input().split())
    X = list(map(int,input().split()))
    Memo = {0:True}
#    a = canSum(M,X,Memo)
    a = canSum1(M,X)
    if a:
        print("true")
    else:
        print("false")

