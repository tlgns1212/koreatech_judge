import sys
input = sys.stdin.readline

def cache_go(NKV,C):
    def divide_by_putget():
        i = 1
        a = []
        while i < len(NKV):
            if NKV[i] == 0:
                a.append([0,NKV[i+1],NKV[i+2]])
                i += 3
            elif NKV[i] == 1:
                a.append([1,NKV[i+1]])
                i += 2
        return a 

    def put(q1,q2,K,V):
        if len(q1) < C and K not in q2:
            q1.append([K,V])
        elif K in q2:
            a = q2.index(K)
            q1.pop(a)
            q1.append([K,V])
        else:
            q1.pop(0)
            q1.append([K,V])

    def get(q1,q2,K):
        if K in q2:
            b = q2.index(K)
            a = q1.pop(b)
            q1.append(a)
            return a[1]
        else :
            return -1
        return -1

    def LRU():
        KV = divide_by_putget()
        q1 = []
        answer = []
        for i in range(len(KV)):
            q2 = []
            for j in q1:
                q2.append(j[0])
            if KV[i][0] == 0:
                put(q1,q2,KV[i][1],KV[i][2])
            elif KV[i][0] == 1:
                answer.append(get(q1,q2,KV[i][1]))
        return answer
    return LRU()

T = int(input())
for _ in range(T):
    C, N = map(int, input().split())
    NKV = list(map(int,input().split()))
    NKV.insert(0,0)
    answer = cache_go(NKV,C)
    a_len = len(answer)
    for i in range(len(answer)):
        if i + 1 == a_len:
            print(answer[i])
        else:
            print(answer[i], end = " ")