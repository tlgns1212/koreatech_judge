import sys
input = sys.stdin.readline


def promising(items, W, currProfit, currWeight, maxProfit, ind):
    global N
    if currWeight >= W:
        return False
    else:
        nextIndex = ind + 1
        bound = currProfit
        totalWeight = currWeight
        while nextIndex < N and totalWeight + items[nextIndex][1] <= W:
            totalWeight += items[nextIndex][1]
            bound += items[nextIndex][0]
            nextIndex += 1
        if nextIndex < N:
            bound += (W-totalWeight) * items[nextIndex][2]
        return bound > maxProfit[0]


def knapsack(items, inc, W, currProfit, currWeight, maxProfit, ind):
    if currWeight <= W and currProfit > maxProfit[0]:
        maxProfit[0] = currProfit
        solution = inc
    if promising(items, W, currProfit, currWeight, maxProfit, ind):
        inc[ind + 1] = True
        knapsack(items, inc, W ,currProfit+items[ind+1][0], \
            currWeight+items[ind+1][1], maxProfit, ind + 1)
        inc[ind+1] = False

        knapsack(items, inc, W, currProfit, currWeight, maxProfit, ind+1)

T = int(input())
for _ in range(T):
    items = []
    W, N = map(int,input().split())
    vw = list(map(int,input().split()))
    for i in range(0,len(vw),2):
        items.append([vw[i], vw[i+1], vw[i]/vw[i+1]])
    items.sort(key = lambda x : x[2], reverse = True)
    inc = [False for _ in range(N)]
    maxprofit = [0]
    max1 = 0
    i = 0
    while max1 == W:
        if vw[i][1] + max1 <= W:
            maxprofit[0] += vw[i][0]
            max1 += vw[i][1]
            i += 1
        else:
            need = W - max1
            max1 += need
            maxprofit[0] += vw[i][2] * need
    count = 0
    knapsack(items,inc,W,0,0,maxprofit,-1)
    print(maxprofit[0])
    