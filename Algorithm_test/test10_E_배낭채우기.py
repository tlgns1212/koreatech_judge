import sys
input = sys.stdin.readline

def separate_vw(vw):
    product = [[-1,0,0]]
    num = 0
    for i in range(0,len(vw),2):
        product.append([num,vw[i],vw[i+1]])
        num += 1
    return product



def tabu_bag(W,N,product):
    table = [[None for _ in range(N+1)] for _ in range(W+1)]
    for i in range(W+1):
        table[i][0] = 0
    for i in range(1,N+1):
        for x in range(W+1):
            if product[i][2] > x:
                table[x][i] = table[x][i-1]
            else:
                table[x][i] = max(table[x][i-1],table[x - product[i][2]][i-1] + product[i][1])
    return table[W][N]

T = int(input())
for _ in range(T):
    W, N = map(int,input().split())
    vw = list(map(int,input().split()))
    product = separate_vw(vw)
    answer = tabu_bag(W,N,product)
    print(answer)
