import sys
input = sys.stdin.readline

# Memoization
def countSum(M,X,Memo):
    if M < 0:
        return 0
    elif M == 0:
        return 1
    elif M in Memo:
        return Memo.get(M)
    count = 0
    for x in X:
        count += countSum(M-x,X,Memo)
        Memo[M] = count
    return count

# Tabulation
def countSum1(M,X):
    table = [0 for _ in range(M+1)]
    table[0] = 1
    for i in range(M):
        if table[i] != 0:
            for x in X:
                if i + x <= M:
                    table[i+x] += table[i]
    return table[M]




T = int(input())
for _ in range(T):
    M,N = map(int,input().split())
    X = list(map(int,input().split()))
    Memo = {0:0}
    # a = countSum(M,X,Memo)
    a = countSum1(M,X)
    print(a)
    