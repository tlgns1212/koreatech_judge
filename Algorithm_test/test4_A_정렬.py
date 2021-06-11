import sys
input = sys.stdin.readline
import random

def quick_sort(arr):
    def sort(low, high):
        if high - low < 1:
            return
        mid = quick(low, high)
        sort(low, mid - 1)
        sort(mid + 1, high)

    def quick(low,high):
        pivot = random.randrange(low, high + 1)
        arr[pivot], arr[low] = arr[low], arr[pivot]
        pivot = arr[low]
        #print(pivot)
        L = low
        R = low + 1
        while R <= high:
            if arr[L] <= pivot and arr[R] < pivot :
                if R - L == 1 :
                    L += 1
                    R += 1
                else :
                    L += 1
                    arr[R], arr[L] = arr[L], arr[R]
                    R += 1
                #print(L,R,"1")
            else :
                R += 1
                #print(L,R,"3")
            #elif arr[R] > pivot:
            #    R += 1
        arr[low], arr[L] = arr[L], arr[low]
        return L
    return sort(0, len(arr) - 1)


T = int(input())
for _ in range(T):
    N = int(input())
    K = list(map(int,input().split()))
    quick_sort(K)
    for i in K:
        print(i,end = " ")