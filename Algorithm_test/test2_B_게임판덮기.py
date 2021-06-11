import sys
input = sys.stdin.readline

move = [[(0,0),(0,1),(1,0)], [(0,0),(0,1),(1,1)],[(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,-1)]]

def isempty():
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == ".":
                return i,j
    return -1,-1

def check(x,y,n):
    for x1,y1 in move[n]:
        x2 = x + x1
        y2 = y + y1
        if not (0 <= x2 < H and 0 <= y2 < W):
            return False
        if matrix[x2][y2] == "#":
            return False
    return True

def fill(x,y,n):
    for x1,y1 in move[n]:
        x2 = x + x1
        y2 = y + y1
        matrix[x2][y2] = "#"

def remove(x,y,n):
    for x1,y1 in move[n]:
        x2 = x + x1
        y2 = y + y1
        matrix[x2][y2] = "."

def count():
    x,y = isempty()
    if x is -1 and y is -1:
        return 1
    can = 0
    for m in range(len(move)):
        if check(x,y,m) :
            fill(x,y,m)
            can += count()
            remove(x,y,m)
    return can
T = int(input())
for _ in range(T):
    H,W = map(int,input().rstrip().split())
    matrix = []
    for _ in range(H):
        matrix.append(list(input().rstrip()))
    empty = 0
    for row in range(H):
        for col in range(W):
            if matrix[row][col] == ".":
                empty += 1
    if empty % 3 == 0:
        print(count())
    else:
        print(0)
