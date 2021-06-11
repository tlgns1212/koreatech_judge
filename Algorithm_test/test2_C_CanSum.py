import sys
input = sys.stdin.readline

def canSum(M,N):
    if M < 0:
        return False
    elif M == 0:
        return True
    for x in X:
        if canSum(M-x,N):
            return True
    return False

T = int(input())
for _ in range(T):
    M, N = map(int,input().split())
    X = list(map(int,input().split()))
    print("true" if canSum(M,X) else "false")