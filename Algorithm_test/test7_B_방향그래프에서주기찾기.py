import sys
input = sys.stdin.readline

def dfs(graph,s,visited,answer,real):
    visited[s] = True
    answer.append(s)
    for i in range(len(graph[s])):
        if graph[s][i] == 1 and i in answer:
            real[0] = True
            return
        if graph[s][i] == 1 and visited[i] == False:
            dfs(graph,i,visited,answer,real)
            if real[0] == True:
                return
            answer.pop()
    return


T = int(input())
for _ in range(T):
    N, E = map(int,input().split())
    visited = [False for _ in range(N)]
    a = list(map(int,input().split()))
    count_list = []
    graph = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(0,len(a),2):
        graph[a[i]][a[i+1]] = 1
    answer = []
    real = [False]
    for i in range(N):
        if not visited[i]:
            dfs(graph,i,visited,answer,real)
            answer = []
            if real[0] is True:
                break
    if real[0]:
        print('true')
    else:
        print('false')
    #print("true" if real[0] is True else "false")