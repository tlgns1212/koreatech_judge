import sys
input = sys.stdin.readline()
T = int(input())
for _ in range(T):
    L = int(input())
    sum = 8*(2 ** (N-2)) + 9*(3 ** (N-2)) + 8*(4 ** (N-2)) + 1*(1 ** (N-2))
    answer = sum % 1000000007
   
    print(int(answer))

    # 하는중