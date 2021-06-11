import sys
input = sys.stdin.readline

def bestSum(M,N):
    if M < 0:
        return None
    elif M == 0:
        return []
    best = None
    for x in X:
        list = bestSum(M-x,X)
        if list!= None:
            if best == None or len(best) > len(list)+1:
                list.append(x)
                best = list
    return best

T = int(input())
for _ in range(T):
    M, N = map(int,input().split())
    X = list(map(int,input().split()))
    A = bestSum(M,X)
    if A is not None:
        print(len(A)," ".join(str(i) for i in A))
    else:
        print(-1)