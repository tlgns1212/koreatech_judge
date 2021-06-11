import sys
input = sys.stdin.readline

def max_min(s):
    max = 0
    min = 0
    n = len(s)
    if s[0] < s[1]:
        max = s[1]
        min = s[0]
    else:
        min = s[1]
        max = s[0]
    i = 2
    while i <= n - 1:
        if i == len(s) - 1:
            if s[i] < min: min = s[i]
            if s[i] > max: max = s[i]
        elif s[i] < s[i + 1]:
            if s[i] < min: min = s[i]
            if s[i+1] > max: max = s[i+1]
        else:
            if s[i+1] < min: min = s[i+1]
            if s[i] > max: max = s[i]
        i += 2
    return max,min

T = int(input())
for _ in range(T):
    N = int(input())
    K = list(map(int,input().split()))
    max,min = max_min(K)
    print(max,min)