T = int(input())
for _ in range(T):
    N = int(input())
    a = []
    sum = 1
    if N == 2:
        sum = 2
    else:
        for i in range(1,N):
            a.append(sum)
            sum += a[i-2]
    sum %= 1000000007
    print(sum)