import sys
input = sys.stdin.readline

def promising(nums, currTotal, leftTotal, W, index):
    return currTotal + leftTotal >= W and (currTotal == W or currTotal + nums[index] <= W)

def subset_sum(nums, included, currTotal, leftTotal, W, index):
    global count
    if promising(nums, currTotal, leftTotal, W, index):
        if currTotal == W:
            count += 1
        else:
            included[index] = True
            leftTotal -= nums[index]
            subset_sum(nums, included, currTotal+nums[index], leftTotal, W, index+1)
            included[index] = False
            subset_sum(nums, included, currTotal, leftTotal, W, index+1)



T = int(input())
for _ in range(T):
    M, N = map(int,input().split())
    X = list(map(int,input().split()))
    count = 0
    X.sort()
    included = [False for _ in range(N)]
    subset_sum(X, included, 0, sum(X), M, 0)
    print(count)