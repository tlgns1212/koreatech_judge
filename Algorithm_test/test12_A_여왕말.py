import sys
input = sys.stdin.readline

def drawqueen(sol, N):
    a = []
    for i in range(N):
        for j in range(N):
            if sol[i] == j:
                print("Q", end = "")
            else:
                print("X", end = "")
        print()

def nqueen(sol,N):
    global count
    if len(sol) == N:
        count += 1
        drawqueen(sol,N)
        return 0
    candidate = list(range(N))
    for i in range(len(sol)):
        if sol[i] in candidate:
            candidate.remove(sol[i])
        distance = len(sol) - i
        if sol[i] + distance in candidate:
            candidate.remove(sol[i] + distance)
        if sol[i] - distance in candidate:
            candidate.remove(sol[i] - distance)
    if candidate != []:
        for i in candidate:
            sol.append(i)
            nqueen(sol, N)
            sol.pop()
    else :
        return 0


T = int(input())
for _ in range(T):
    count = 0
    N = int(input())
    for i in range(N):
        nqueen([i],N)
    if count == 0:
        print()
