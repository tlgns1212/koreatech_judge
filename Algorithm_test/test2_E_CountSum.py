import sys
input = sys.stdin.readline

def countSum(M,N):
    if M < 0:
        return 0
    elif M == 0:
        return 1
    count = 0
    for x in X:
        count += countSum(M-x,X)
    return count

T = int(input())
for _ in range(T):
    M, N = map(int,input().split())
    X = list(map(int,input().split()))
    print(reversed(countSum(M,X)))