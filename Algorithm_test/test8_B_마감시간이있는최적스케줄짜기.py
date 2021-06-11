import sys
input = sys.stdin.readline

def schedule(DP):
    def sort_lower():
        D = []
        k = 1
        for i in range(0,len(DP),2):
            D.append([k,DP[i],DP[i+1]])
            k += 1
        max1 = 0
        for i in D:
            if i[1] > max1:
                max1 = i[1]
        S = [False for _ in range(max1+1)]
        D.sort(key = lambda x: x[2], reverse = True)
        return D, S
    
    def find_deadline():
        D,S = sort_lower()
        scheduled = []
        S[D[0][1]] = True
        scheduled.append(D[0][0])
        for i in range(1,len(D)):
            for j in range(D[i][1],0,-1):
                if not S[j]:
                    S[j] = True
                    scheduled.append(D[i][0])
                    break
        return scheduled
    return find_deadline()

T = int(input())
for _ in range(T):
    N = int(input())
    DP = list(map(int,input().split()))
    D = schedule(DP)
    a_len = len(D)
    D.sort()
    for i in range(len(D)):
        if i + 1 == a_len:
            print(D[i])
        else:
            print(D[i], end = " ")