#실패

#def fibonacci(n):
#    if n == 1: return 1
#    elif n == 2: return 3
#    elif n == 3: return 5 
#    else: return fibonacci(n-1) + (2 * fibonacci(n-2))

#T = int(input())
#for _ in range(T):
#    N = int(input())
#    sum = fibonacci(N)
#    sum %= 1000000007
#    print(sum)


T = int(input())
for _ in range(T):
    N = int(input())
    a = []
    sum = 1
    if N == 2:
        sum = 3
    else:
        for i in range(1,N):
            a.append(sum)
            sum += 2*a[i-2]
    sum %= 1000000007
    print(sum)

