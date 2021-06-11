import sys
input = sys.stdin.readline

def howSum(M,N):                    
    if M < 0:                       # 0보다 작으면 틀림
        return None
    elif M == 0:                    # 0이면 맞음
        return []                   # 1) 리스트 생성
    for x in X:                     # x 개의 서로 다른 정수 X
        list = howSum(M-x,X)        # 재귀(x 만큼 뺀 상태로)
        if list!= None:             # 1) 적용 됐으면 실행
            list.append(x)          # 리스트에 값 추가
            return list             # 리스트 반환
    return None

T = int(input())
for _ in range(T):
    M, N = map(int,input().split()) 
    X = list(map(int,input().split()))
    A = howSum(M,X)
    if M == 0 or M == 1:
        print(-1)
    elif A is not None:
        print(len(A)," ".join(str(i) for i in A))  # 출력 형식은 채점번호 46879(문제 F)와 동일
    else:
        print(-1) 



        