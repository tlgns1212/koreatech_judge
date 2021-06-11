import sys
input = sys.stdin.readline

# Memoization
def howSum(M,X,Memo):
    if M < 0:
        return None
    elif M == 0:
        return []
    elif M in Memo:
        return Memo.get(M)
    for x in X:
        list1 = howSum(M-x,X,Memo)
        if list1 != None:
            list1.append(x)
            Memo[M] = list1
            return list1
    Memo[M] = None
    return None


# Tabulization
def howSum1(M,X):
    table = [[None] for _ in range(M+1)]
    table[0] = []
    for i in range(M):
        if table[i] != [None]:
            for x in X:
                if i + x <= M and table[i+x] == [None]:
                    list1 = []
                    list1 = list(table[i])
                    list1.append(x)
                    table[i+x] = list1
        if table[M] != [None]:
            return table[M]
    return table[M]




T = int(input())
for _ in range(T):
    M,N = map(int,input().split())
    X = list(map(int,input().split()))
    # Memo = {0:0}
    # a = howSum(M,X,Memo)
    a = howSum1(M,X)
    if a == [None] or a == None:
        print(-1)
    else:
        print(len(a),end = " ")
        for i in a:
            print(i,end = " ")
        print()


    