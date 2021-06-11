import sys
input = sys.stdin.readline

def second_max(s):
    if len(s) <= 2:
        max = s[0] if s[0] <= s[1] else s[1]
        return max
    else:
        n = 2 * len(s) - 1
        i = 0
        while len(s) < n:
            if s[i] > s[i+1]: 
                s.append(s[i])
            else: 
                s.append(s[i+1])
            i += 2
        max = s[i]
        second = []
        i -= 1
        while i > 0:
            if s[i] == max:
                second.append(s[i-1])
            elif s[i-1] == max:
                second.append(s[i])
            i -= 2
        if len(second) <= 2:
            max = second[0] if second[0] >= second[1] else second[1]
        else:
            i = 0
            n = len(second)*2-1
            while len(second) < n:
                if second[i] > second[i+1]: 
                    second.append(second[i])
                else: 
                    second.append(second[i+1])
                i += 2
            max = second[i]
        return max


T = int(input())
for _ in range(T):
    N = int(input())
    K = list(map(int,input().split()))
    second = second_max(K)
    print(second)