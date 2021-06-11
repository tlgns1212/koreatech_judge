import sys
input = sys.stdin.readline
import random

def quick_sort(arr,k):
    def sort(low, high):
        if low == high:
            return arr[low]
        mid = quick(low, high)
        if mid > k:
            return sort(low, mid - 1)
        elif mid < k:
            return sort(mid + 1, high)
        else :
            return arr[mid]
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
    N,k = map(int,input().split())
    s = list(map(int,input().split()))
    answer = quick_sort(s,k - 1)
    print(answer)
    