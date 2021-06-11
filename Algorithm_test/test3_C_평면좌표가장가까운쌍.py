#import sys
#from decimal import *
#import math
#input = sys.stdin.readline


#def dist(x1, x2):
#    return (x1[0] - x2[0])**2 + (x1[1] - x2[1])**2

#def solve(coords, N):
#    if(N == 2):
#        return dist(coords[0], coords[1])
#    elif(N == 3):
#        return min(dist(coords[0], coords[1]), dist(coords[1], coords[2]), dist(coords[0], coords[2]))
    
#    mid = (coords[N//2][0] + coords[N//2-1][0]) // 2
#    d = min(solve(coords[:N//2], N//2), solve(coords[N//2:], math.ceil(N/2)))
#    short_check = []
#    for subset in coords:
#        if((mid - subset[0])**2 <= d):
#            short_check.append(subset)
#    short_check.sort(key = lambda x:x[1])
#    if(len(short_check) == 1):
#        return d
#    else:
#        y_check = d
        
#        for i in range(len(short_check) - 1):
#            for j in range(i+1, len(short_check)):
#                if(short_check[i][1] - short_check[j][1]) ** 2 > d:
#                    break
#                elif(short_check[i][0] < mid and short_check[j][0] < mid):
#                    continue
#                elif(short_check[i][0] > mid and short_check[j][0] > mid):
#                    continue
#                y_check = min(y_check, dist(short_check[i], short_check[j]))
                
#    return y_check
#T = int(input())
#for _ in range(T):
#    N = int(input())
#    coord = list(map(int, input().split()))
#    coords = [[coord[i], coord[i+1]] for i in range(0,len(coord),2)]

#    coords_set = list(set(map(tuple,coords)))
#    if len(coords_set) != len(coords):
#        print("0.00")
#    else:
#        coords_set.sort()
#        a = solve(coords_set, N)
#        a = math.sqrt(a)
#        print(Decimal(str(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))



import sys
import math
from decimal import *
input = sys.stdin.readline

def dist(x1, x2):
    return (x1[0] - x2[0])**2 + (x1[1] - x2[1])**2

def solve(arr):
    px = arr
    py = list(arr)
    py.sort(key = lambda x:x[1])
    def closestPair(px,py):
        if len(px) == 2:
            return dist(px[0],px[1])
        elif len(px) == 3:
            return min(dist(px[0],px[1]), dist(px[1],px[2]), dist(px[0],px[2]))
        N = len(px)//2
        pxL, pxR = px[:N],px[N:]
        set = []
        pyL = list(pxL)
        pyR = list(pxR)
        pyL.sort(key = lambda x : x[1])
        pyR.sort(key = lambda x : x[1])

        delta = min(closestPair(pxL,pyL),closestPair(pxR,pyR))
        return closestSplitPair(px,py,delta)
    
    def closestSplitPair(px,py,delta):
        N = len(px) // 2
        medianX = px[N][0]
        candidates = []
        print("px, py = ",px,"\n",py)
        for i in range(len(px)) :
            print(i, "medianX - px ** 2 = ",(medianX - px[i][0])**2,"\ndelta = ",delta)
            if (medianX - px[i][0]) ** 2 <= delta :
                if py[i] in px[i:]:
                    candidates.append(py[i])
        print("candidates = ", candidates)
        if (len(candidates) == 1):
            print("delta1 = ",delta)
            return delta
        else :
            for i in range(len(candidates) - 1):
                for j in range(i+1, len(candidates)):
                    if(candidates[i][1] - candidates[j][1]) ** 2 > delta:
                        break
                    elif(candidates[i][0] < medianX and candidates[j][0] < medianX):
                        continue
                    elif(candidates[i][0] > medianX and candidates[j][0] > medianX):
                        continue
                    delta = min(delta, dist(candidates[i], candidates[j]))
        print("delta2 = ",delta)
        return delta
    return closestPair(px,py)

T = int(input())
for _ in range(T):
    N = int(input())
    ar = list(map(int, input().split()))
    arrs = [[ar[i], ar[i+1]] for i in range(0,len(ar),2)]

    arr = list(set(map(tuple,arrs)))
    if len(arr) != len(arrs):
        print("0.00")
    else:
        arr.sort()
        a = solve(arr)
        a = math.sqrt(a)
        print(Decimal(str(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
      