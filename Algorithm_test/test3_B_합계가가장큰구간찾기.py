import sys
input = sys.stdin.readline

def bighalf(K):
    sz = len(K)

    def look(low, high):
        if low == high:
            return K[low]
        mid = (low + high) // 2
        left = look(low,mid)
        right = look(mid + 1, high)

        i = 0
        left_side = -1000000000
        for j in range(mid,low - 1, -1):
            i += K[j]
            left_side = max(left_side,i)

        i = 0
        right_side = -1000000000
        for j in range(mid + 1, high + 1):
            i += K[j]
            right_side = max(right_side,i)

        return max(left,right,left_side + right_side)
    return look(0,N-1)

T = int(input())
for _ in range(T):
    N = int(input())
    K = list(map(int,input().split()))
    print(bighalf(K))